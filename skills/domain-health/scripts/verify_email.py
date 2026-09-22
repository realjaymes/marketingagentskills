#!/usr/bin/env python3
"""
Self-built email verifier (MX + SMTP), standard library + the `dig` command.
No third-party account, no per-email cost. This is the reusable version of the
verifier the Revenue.Inc take-home needed.

verify(email) returns:
  {"status": "valid" | "invalid" | "risky" | "unknown", "mx": <host>, "reason": ...}

Honesty about limits: many mail servers accept-all (catch-all) or block the
SMTP probe, and many networks block outbound port 25. So "valid" means "the
server accepted the recipient", and "risky" means "catch-all / can't be sure".
Treat results as a strong signal, not a guarantee. For higher accuracy at scale,
run reacherhq/check-if-email-exists as a local service and call it instead.
"""
import re, subprocess, smtplib, socket

EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$")
FROM_ADDR = "verify@example.com"   # HELO/MAIL FROM identity; use your own domain in prod

_SMTP_OK = None
def _smtp_available(timeout=4):
    """Probe once whether outbound port 25 works here (cached). Most clouds/ISPs
    block it; when blocked, verify() returns 'unknown' instantly instead of
    hanging on every address."""
    global _SMTP_OK
    if _SMTP_OK is None:
        try:
            s = socket.create_connection(("gmail-smtp-in.l.google.com", 25), timeout=timeout)
            s.close(); _SMTP_OK = True
        except Exception:
            _SMTP_OK = False
    return _SMTP_OK


def mx_hosts(domain):
    """Return MX hostnames for a domain, best first, via `dig`."""
    try:
        out = subprocess.run(["dig", "+short", "MX", domain], capture_output=True,
                             text=True, timeout=10).stdout.strip()
    except Exception:
        return []
    hosts = []
    for line in out.splitlines():
        parts = line.split()
        if len(parts) == 2:  # "10 mail.example.com."
            hosts.append((int(parts[0]), parts[1].rstrip(".")))
    hosts.sort()
    return [h for _, h in hosts]


def verify(email, timeout=10):
    email = (email or "").strip().lower()
    if not EMAIL_RE.match(email):
        return {"status": "invalid", "mx": "", "reason": "bad format"}
    domain = email.split("@")[1]
    hosts = mx_hosts(domain)
    if not hosts:
        return {"status": "invalid", "mx": "", "reason": "no MX record"}
    mx = hosts[0]

    if not _smtp_available():
        return {"status": "unknown", "mx": mx, "reason": "port 25 unavailable"}

    try:
        server = smtplib.SMTP(timeout=timeout)
        server.connect(mx, 25)
        server.helo(socket.getfqdn() or "localhost")
        server.mail(FROM_ADDR)
        code, _ = server.rcpt(email)
        # catch-all probe: a random address that shouldn't exist
        probe_code, _ = server.rcpt("no-such-user-zzq19x@" + domain)
        server.quit()
    except (smtplib.SMTPServerDisconnected, smtplib.SMTPConnectError, socket.error, OSError) as e:
        return {"status": "unknown", "mx": mx, "reason": f"smtp probe blocked ({e.__class__.__name__})"}

    if probe_code in (250, 251):
        return {"status": "risky", "mx": mx, "reason": "catch-all domain"}
    if code in (250, 251):
        return {"status": "valid", "mx": mx, "reason": "accepted"}
    if code in (550, 551, 553):
        return {"status": "invalid", "mx": mx, "reason": "rejected"}
    return {"status": "unknown", "mx": mx, "reason": f"smtp code {code}"}


if __name__ == "__main__":
    import sys
    addr = sys.argv[1] if len(sys.argv) > 1 else "info@example.com"
    print(addr, "->", verify(addr))
