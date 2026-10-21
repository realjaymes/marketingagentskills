#!/usr/bin/env python3
"""Keep the published skill count accurate.

Counts skills/*/SKILL.md, rewrites the count in README.md, and checks that the
README skill table and category lists name every skill folder.

  python3 scripts/sync-skill-count.py          rewrite README count
  python3 scripts/sync-skill-count.py --check  exit 1 on any mismatch
  python3 scripts/sync-skill-count.py --check --repo owner/name
                                               also check the GitHub description
"""
import argparse
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
COUNT_RE = re.compile(r"\b\d+( AI agent skills for marketing)")


def skills():
    return sorted(p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md"))


def readme_lists(text):
    table = set(re.findall(r"^\| \[([\w-]+)\]\(skills/", text, re.M))
    cats = text.split("## Skill Categories", 1)[-1].split("\n---", 1)[0]
    return table, set(re.findall(r"`([\w-]+)`", cats))


def description(repo):
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}")
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req) as r:
        return json.load(r).get("description") or ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--repo", help="owner/name, check the GitHub description")
    args = ap.parse_args()

    names = skills()
    n = len(names)
    text = README.read_text()
    problems = []

    found = COUNT_RE.findall(text)
    if not found:
        problems.append("README count sentence not found")
    for m in re.finditer(r"\b(\d+) AI agent skills for marketing", text):
        if int(m.group(1)) != n:
            problems.append(f"README says {m.group(1)}, actual {n}")

    table, cats = readme_lists(text)
    for label, got in (("table", table), ("categories", cats)):
        for s in sorted(set(names) - got):
            problems.append(f"README {label} missing skill: {s}")
        for s in sorted(got - set(names)):
            problems.append(f"README {label} lists absent skill: {s}")

    if args.repo:
        d = description(args.repo)
        m = re.search(r"\b(\d+) AI agent skills", d)
        if not m or int(m.group(1)) != n:
            problems.append(f"GitHub description says '{d}', actual {n}")

    if args.check:
        for p in problems:
            print("MISMATCH:", p)
        print(f"{n} skills" + ("" if problems else ", all counts match"))
        sys.exit(1 if problems else 0)

    new = re.sub(r"\b\d+( AI agent skills for marketing)", rf"{n}\1", text)
    if new != text:
        README.write_text(new)
        print(f"README count set to {n}")
    else:
        print(f"README count already {n}")
    for p in problems:
        if "count" not in p and "says" not in p:
            print("WARN:", p)


if __name__ == "__main__":
    main()
