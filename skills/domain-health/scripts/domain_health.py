#!/usr/bin/env python3
"""
domain-health: email authentication and deliverability posture for a domain.

Two modes, same DNS primitives:

  audit     Domains you own. Full posture, sender inventory, readiness score,
            prioritised remediation. Use before tightening DMARC or before
            starting outbound from a domain.

  prospect  Domains you are targeting. CSV with gap tags, for enriching a
            cold-outbound list. Backwards compatible with the older
            dns_dmarc_check.py output columns.

Usage:
    python3 domain_health.py --domain example.com
    python3 domain_health.py --domain example.com --json
    python3 domain_health.py --mode prospect domains.txt > signals.csv
    python3 domain_health.py --domain example.com --blacklist

Requires only `dig` and the standard library. No API key, no paid tool.

HONESTY CONSTRAINTS (these are load-bearing, do not relax them):
  * DKIM cannot be enumerated from DNS. A selector sweep that finds nothing
    means "no key on the selectors we tried", never "DKIM is absent". Some
    providers use per-account random selectors that are unguessable.
  * Apex verification tokens prove a domain was verified with a provider at
    some point. They do NOT prove that provider currently sends mail as the
    domain. Treat inferred senders as leads to confirm, not facts.
  * A prospect's primary domain is a proxy. Teams doing cold outbound properly
    send from a separate domain to protect the primary. Never state a DMARC
    finding about a prospect as a confirmed claim about their outbound.
  * Blacklist results for a domain on hosted email describe the PROVIDER's
    shared infrastructure, not the domain's own reputation.
"""

import argparse
import json
import os
import re
import socket
import subprocess
import sys
import csv

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "selectors.json"), encoding="utf-8") as fh:
    SIG = json.load(fh)

SEND_SUBDOMAINS = ["newsletter", "mail", "email", "send", "smtp", "mg", "bounce",
                   "em", "news", "marketing", "notifications", "link", "click", "track"]

DNSBLS = ["zen.spamhaus.org", "bl.spamcop.net", "b.barracudacentral.org", "dnsbl.sorbs.net"]


# ---------------------------------------------------------------- dns helpers

def dig(name, rtype="TXT"):
    """Return a list of answer strings, or [] on any failure. Never raises."""
    try:
        out = subprocess.run(["dig", "+short", rtype, name],
                             capture_output=True, text=True, timeout=10)
        return [l.strip() for l in out.stdout.splitlines() if l.strip()]
    except Exception:
        return []


def txt_join(records):
    """dig splits long TXT strings; strip quotes and rejoin."""
    return [re.sub(r'"\s+"', "", r).strip('"') for r in records]


# ------------------------------------------------------------------- checks

def check_mx(domain):
    mx = dig(domain, "MX")
    hosts = []
    for r in mx:
        parts = r.split()
        if len(parts) == 2:
            hosts.append({"pref": int(parts[0]), "host": parts[1].rstrip(".")})
    hosts.sort(key=lambda h: h["pref"])
    return {"present": bool(hosts), "hosts": hosts}


def check_spf(domain):
    recs = [r for r in txt_join(dig(domain, "TXT")) if r.lower().startswith("v=spf1")]
    if not recs:
        return {"present": False, "multiple": False, "record": None,
                "all_qualifier": None, "lookups": 0, "includes": [], "over_limit": False}
    # More than one SPF record is itself a hard failure: RFC 7208 says PermError.
    rec = recs[0]
    m = re.search(r"([-~?+])all\b", rec)
    includes = re.findall(r"include:([^\s]+)", rec)
    # Count mechanisms that trigger a DNS lookup. Limit is 10 (RFC 7208 4.6.4).
    lookups = len(re.findall(r"\b(include|a|mx|ptr|exists|redirect)[:=\s]", rec + " "))
    return {"present": True, "multiple": len(recs) > 1, "record": rec,
            "all_qualifier": (m.group(1) if m else None),
            "lookups": lookups, "includes": includes, "over_limit": lookups > 10}


def check_dkim(domain):
    """Sweep known selectors. See HONESTY CONSTRAINTS in the module docstring."""
    found = []
    for sel, owner in SIG["selectors"].items():
        recs = txt_join(dig(f"{sel}._domainkey.{domain}", "TXT"))
        cname = dig(f"{sel}._domainkey.{domain}", "CNAME")
        if any("v=dkim1" in r.lower() or "p=" in r for r in recs) or cname:
            found.append({"selector": sel, "likely_provider": owner,
                          "via": "CNAME" if cname and not recs else "TXT"})
    return {"selectors_tried": len(SIG["selectors"]), "found": found,
            "any_found": bool(found)}


def check_dmarc(domain):
    recs = [r for r in txt_join(dig(f"_dmarc.{domain}", "TXT"))
            if r.lower().startswith("v=dmarc1")]
    if not recs:
        return {"present": False, "record": None, "policy": None, "sp": None,
                "pct": None, "rua": [], "ruf": [], "status": "missing",
                "reports_readable": None}
    rec = recs[0]
    tag = lambda t: (re.search(rf"\b{t}=([^;\s]+)", rec) or [None, None])[1]
    p, sp, pct = tag("p"), tag("sp"), tag("pct")
    rua = re.findall(r"rua=([^;]+)", rec)
    rua = [a.strip() for chunk in rua for a in chunk.split(",")]
    ruf = re.findall(r"ruf=([^;]+)", rec)
    ruf = [a.strip() for chunk in ruf for a in chunk.split(",")]
    status = {"none": "monitoring-only", "quarantine": "moderate",
              "reject": "strict"}.get((p or "").lower(), "unknown")
    # Reports going to a human mailbox arrive as raw XML and in practice go unread.
    known_readers = ("dmarc.brevo.com", "dmarcian", "postmarkapp", "valimail",
                     "easydmarc", "dmarcdigests", "agari", "fraudmarc", "mxtoolbox")
    reports_readable = None
    if rua:
        reports_readable = any(k in a.lower() for a in rua for k in known_readers)
    return {"present": True, "record": rec, "policy": p, "sp": sp, "pct": pct,
            "rua": rua, "ruf": ruf, "status": status,
            "reports_readable": reports_readable}


def check_maturity(domain):
    mta = txt_join(dig(f"_mta-sts.{domain}", "TXT"))
    tls = txt_join(dig(f"_smtp._tls.{domain}", "TXT"))
    bimi = txt_join(dig(f"default._bimi.{domain}", "TXT"))
    return {"mta_sts": bool(mta), "tls_rpt": bool(tls), "bimi": bool(bimi)}


def sender_inventory(domain, spf):
    """
    Infer which providers are attached to the domain, then cross-check each
    against SPF. This is the check that catches a provider verified years ago,
    still able to send, but never added to SPF.

    Each entry carries `mail`, which says whether the signal implies mail
    sending at all. A site-verification token or a custom web-domain CNAME
    proves a relationship with a vendor, not that the vendor sends as this
    domain. Only mail-relevant senders missing from SPF count as a gap, so the
    gap list stays worth reading.
    """
    senders = {}

    def add(name, evidence, mail, note=None):
        e = senders.setdefault(name, {"evidence": [], "in_spf": False,
                                      "mail_relevant": mail, "note": note})
        if evidence not in e["evidence"]:
            e["evidence"].append(evidence)
        e["mail_relevant"] = e["mail_relevant"] or mail
        if note and not e.get("note"):
            e["note"] = note

    for rec in txt_join(dig(domain, "TXT")):
        for token, meta in SIG["apex_tokens"].items():
            if rec.lower().startswith(token.lower()):
                add(meta["provider"], f"apex TXT token '{token}'", meta["mail"])

    for inc in spf.get("includes", []):
        owner = SIG["spf_includes"].get(inc, f"unknown ({inc})")
        add(owner, f"SPF include:{inc}", True)
        senders[owner]["in_spf"] = True

    for sub in SEND_SUBDOMAINS:
        for target in dig(f"{sub}.{domain}", "CNAME"):
            t = target.rstrip(".").lower()
            for frag, meta in SIG["cname_targets"].items():
                if frag in t:
                    add(meta["provider"], f"{sub}.{domain} CNAME -> {t}",
                        meta["mail"], meta.get("note"))

    return senders


def check_blacklists(domain, mx):
    """
    GATED behind --blacklist and deliberately labelled. For a domain on hosted
    email the MX addresses belong to the provider, so a listing describes the
    PROVIDER's shared infrastructure, never this domain's own reputation.
    """
    results = []
    ips = []
    for h in mx.get("hosts", [])[:2]:
        try:
            ips.extend({ai[4][0] for ai in socket.getaddrinfo(h["host"], None, socket.AF_INET)})
        except Exception:
            pass
    for ip in sorted(set(ips))[:3]:
        rev = ".".join(reversed(ip.split(".")))
        for bl in DNSBLS:
            listed = bool(dig(f"{rev}.{bl}", "A"))
            results.append({"ip": ip, "list": bl, "listed": listed})
    return {"checked": bool(results), "results": results,
            "caveat": "These addresses belong to the mail provider, not this domain. "
                      "A listing reflects the provider's shared infrastructure."}


# -------------------------------------------------------------------- scoring

def score(rep):
    """0-100 readiness. Weighted toward what actually blocks a DMARC rollout."""
    s, notes = 0, []
    spf, dkim, dmarc = rep["spf"], rep["dkim"], rep["dmarc"]

    if spf["present"] and not spf["multiple"]:
        s += 20
        if spf["all_qualifier"] == "-":
            s += 10
        elif spf["all_qualifier"] == "~":
            s += 6
            notes.append("SPF ends in ~all (soft fail). -all is stronger once senders are confirmed.")
        else:
            notes.append("SPF has no restrictive all qualifier, so it asserts almost nothing.")
        if spf["over_limit"]:
            s -= 10
            notes.append(f"SPF needs {spf['lookups']} DNS lookups, over the limit of 10. "
                         "Receivers return PermError and SPF effectively fails.")
    elif spf["multiple"]:
        notes.append("Multiple SPF records found. This is a PermError, SPF fails entirely.")
    else:
        notes.append("No SPF record.")

    if dkim["any_found"]:
        s += 25
    else:
        notes.append(f"No DKIM key found across {dkim['selectors_tried']} known selectors. "
                     "This is not proof of absence, selectors are arbitrary.")

    if dmarc["present"]:
        s += 15
        s += {"strict": 20, "moderate": 12, "monitoring-only": 4}.get(dmarc["status"], 0)
        if dmarc["status"] == "monitoring-only":
            notes.append("DMARC is p=none, so nothing is enforced and anyone can spoof the domain.")
        if dmarc["sp"] and dmarc["sp"].lower() == "none" and dmarc["policy"] != "none":
            notes.append("sp=none leaves subdomains unprotected even though the apex policy is stronger.")
        if dmarc["rua"] and dmarc["reports_readable"] is False:
            notes.append("DMARC reports go to a normal mailbox as raw XML. In practice these go unread. "
                         "Point rua at a report reader before changing policy.")
        if not dmarc["rua"]:
            notes.append("No rua address, so no aggregate reports are collected. "
                         "You cannot safely tighten policy without them.")
    else:
        notes.append("No DMARC record.")

    m = rep["maturity"]
    s += 5 if m["mta_sts"] else 0
    s += 3 if m["tls_rpt"] else 0
    s += 2 if m["bimi"] else 0

    gaps = [n for n, d in rep["senders"].items()
            if not d["in_spf"] and d.get("mail_relevant")]
    if gaps:
        notes.append("Providers attached to this domain but absent from SPF: "
                     + ", ".join(gaps)
                     + ". Confirm whether each still sends before tightening DMARC.")
    return max(0, min(100, s)), notes


# -------------------------------------------------------------------- reports

def audit(domain, want_blacklist=False):
    spf = check_spf(domain)
    rep = {"domain": domain, "mx": check_mx(domain), "spf": spf,
           "dkim": check_dkim(domain), "dmarc": check_dmarc(domain),
           "maturity": check_maturity(domain)}
    rep["senders"] = sender_inventory(domain, spf)
    if want_blacklist:
        rep["blacklist"] = check_blacklists(domain, rep["mx"])
    rep["score"], rep["notes"] = score(rep)
    return rep


def print_audit(rep):
    d, spf, dkim, dmarc = rep["domain"], rep["spf"], rep["dkim"], rep["dmarc"]
    print(f"\n{'='*66}\n  {d}   readiness {rep['score']}/100\n{'='*66}")

    hosts = ", ".join(h["host"] for h in rep["mx"]["hosts"]) or "none"
    print(f"\nMX      {hosts}")
    print(f"SPF     {spf['record'] or 'MISSING'}")
    if spf["present"]:
        print(f"        qualifier={spf['all_qualifier'] or 'none'}  lookups={spf['lookups']}/10")
    if dkim["found"]:
        for f in dkim["found"]:
            print(f"DKIM    {f['selector']} ({f['via']})  likely {f['likely_provider']}")
    else:
        print(f"DKIM    none found across {dkim['selectors_tried']} selectors (not proof of absence)")
    print(f"DMARC   {dmarc['record'] or 'MISSING'}")
    if dmarc["present"]:
        print(f"        policy={dmarc['policy']} sp={dmarc['sp'] or 'inherits'} "
              f"status={dmarc['status']} reports_readable={dmarc['reports_readable']}")

    m = rep["maturity"]
    print(f"EXTRAS  MTA-STS={m['mta_sts']}  TLS-RPT={m['tls_rpt']}  BIMI={m['bimi']}")

    print("\nSENDER INVENTORY  (inferred, confirm before acting)")
    if not rep["senders"]:
        print("  none detected")
    for name, info in sorted(rep["senders"].items()):
        if not info.get("mail_relevant"):
            flag = "not mail"
        elif info["in_spf"]:
            flag = "in SPF"
        else:
            flag = "GAP"
        print(f"  [{flag:10}] {name}")
        for e in info["evidence"]:
            print(f"               via {e}")
        if info.get("note"):
            print(f"               note: {info['note']}")

    if "blacklist" in rep:
        print("\nBLACKLIST  (provider infrastructure, NOT this domain's reputation)")
        for r in rep["blacklist"]["results"]:
            if r["listed"]:
                print(f"  LISTED  {r['ip']} on {r['list']}")
        if not any(r["listed"] for r in rep["blacklist"]["results"]):
            print("  no listings on the lists checked")

    if rep["notes"]:
        print("\nFINDINGS")
        for i, n in enumerate(rep["notes"], 1):
            print(f"  {i}. {n}")
    print()


def prospect_rows(domains):
    """CSV for list enrichment. Columns kept compatible with dns_dmarc_check.py."""
    w = csv.writer(sys.stdout)
    w.writerow(["domain", "spf_present", "dmarc_record", "dmarc_status",
                "dkim_found", "gap"])
    for d in domains:
        spf, dmarc, dkim = check_spf(d), check_dmarc(d), check_dkim(d)
        gap = dmarc["status"] in ("missing", "monitoring-only")
        w.writerow([d, spf["present"], dmarc["record"] or "",
                    dmarc["status"], dkim["any_found"], gap])


def main():
    ap = argparse.ArgumentParser(description="Email auth posture for a domain.")
    ap.add_argument("file", nargs="?", help="file of domains, one per line")
    ap.add_argument("--domain", help="single domain")
    ap.add_argument("--mode", choices=["audit", "prospect"], default="audit")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--blacklist", action="store_true",
                    help="also query DNSBLs. Reports the PROVIDER's shared "
                         "infrastructure, not this domain's own reputation.")
    a = ap.parse_args()

    domains = []
    if a.domain:
        domains = [a.domain.strip().lower()]
    elif a.file:
        with open(a.file, encoding="utf-8") as fh:
            domains = [l.strip().lower() for l in fh if l.strip() and not l.startswith("#")]
    else:
        ap.error("pass --domain or a file of domains")

    if a.mode == "prospect":
        prospect_rows(domains)
        return

    reports = [audit(d, a.blacklist) for d in domains]
    if a.json:
        print(json.dumps(reports, indent=2))
    else:
        for r in reports:
            print_audit(r)


if __name__ == "__main__":
    main()
