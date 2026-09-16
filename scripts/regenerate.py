#!/usr/bin/env python3
"""
Regenerate the skill's reference files from the PUBLISHED documentation.

Two sources, both public:
  - https://docs.smartlyq.com/openapi.json  -> references/endpoints.md
  - https://docs.smartlyq.com/<page>.md     -> the mirrored reference pages

Generating from the published spec is not a convenience, it is the safety
property. Endpoints SmartlyQ deliberately does not publish are absent from
that spec, so they cannot end up in this public repo. Never point this script
at the backend source.
"""

import collections
import json
import os
import re
import sys
import urllib.request

DOCS = "https://docs.smartlyq.com"
SPEC_URL = f"{DOCS}/openapi.json"

PAGES = [
    ("authentication", "references/authentication.md"),
    ("guides/errors", "references/errors.md"),
    ("guides/rate-limiting", "references/rate-limiting.md"),
    ("guides/async-jobs", "references/async-jobs.md"),
    ("guides/idempotency", "references/idempotency.md"),
    ("guides/webhooks", "references/webhooks.md"),
]

MIRROR_NOTE = (
    "<!-- Mirrored from https://docs.smartlyq.com. The docs are the source of truth;\n"
    "     if this file and the docs disagree, the docs win. -->\n\n"
)

# Anything matching these must never appear in this public repo. The published
# spec has never contained them; this is the tripwire if that ever changes.
FORBIDDEN = ("avatar", "heygen", "/dub")


# The docs CDN 403s requests carrying a default library user-agent.
UA = "SmartlyQ-api-skill regenerate (+https://github.com/SmartlyQ/SmartlyQ-api-skill)"


def fetch(url: str, attempts: int = 5) -> str:
    """GET with retries - the docs site may still be deploying after a push."""
    last = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8")
        except Exception as exc:  # noqa: BLE001
            last = exc
            if i < attempts - 1:
                import time

                time.sleep(10 * (i + 1))
    raise SystemExit(f"could not fetch {url}: {last}")


def clean_doc(text: str) -> str:
    """Strip the docs platform's index preamble and theme markers."""
    text = re.sub(r"^>\s*##\s*Documentation Index[\s\S]*?\n(?=#\s)", "", text)
    text = text.replace(" theme={null}", "")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def build_endpoints(spec: dict) -> str:
    paths = spec["paths"]
    groups: dict[str, list] = collections.defaultdict(list)
    for path, item in sorted(paths.items()):
        group = path.strip("/").split("/")[0]
        for method, op in item.items():
            if method not in ("get", "post", "put", "patch", "delete"):
                continue
            groups[group].append((method.upper(), path, (op.get("summary") or "").strip()))

    total = sum(len(v) for v in groups.values())
    base = spec["servers"][0]["url"]
    out = [
        "# SmartlyQ API endpoint map",
        "",
        f"Generated from the published OpenAPI spec at {SPEC_URL}",
        "",
        f"Base URL: `{base}`",
        "",
        f"{len(paths)} paths, {total} operations, {len(groups)} resource groups.",
        "",
        "Use this to find the right endpoint quickly. For request and response",
        "shapes, fetch the spec or the reference page for that operation - do not",
        "guess a body from the summary.",
        "",
    ]
    for group in sorted(groups, key=lambda k: -len(groups[k])):
        ops = groups[group]
        out += [f"## {group} ({len(ops)})", "", "| Method | Path | Operation |", "| --- | --- | --- |"]
        out += [f"| `{m}` | `{p}` | {s} |" for m, p, s in ops]
        out.append("")
    return "\n".join(out)


def main() -> int:
    spec = json.loads(fetch(SPEC_URL))

    for term in FORBIDDEN:
        hits = [p for p in spec["paths"] if term in p.lower()]
        if hits:
            print(f"ABORT: published spec now contains '{term}': {hits[:5]}", file=sys.stderr)
            print("Confirm these are meant to be public before regenerating.", file=sys.stderr)
            return 1

    with open("references/endpoints.md", "w") as f:
        f.write(build_endpoints(spec))
    ops = sum(1 for p in spec["paths"].values() for m in p if m in ("get", "post", "put", "patch", "delete"))
    summary = f"{len(spec['paths'])} paths, {ops} operations"
    print(f"endpoints.md: {summary}")

    # The workflow reads this for its commit message, so it does not need a
    # second fetch or a heredoc inside YAML.
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"summary={summary}\n")

    for slug, dest in PAGES:
        body = clean_doc(fetch(f"{DOCS}/{slug}.md"))
        if "# Page Not Found" in body:
            print(f"WARN: {slug} returned a not-found page, keeping the existing file")
            continue
        with open(dest, "w") as f:
            f.write(MIRROR_NOTE + body)
        print(f"{dest}: {len(body.splitlines())} lines")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
