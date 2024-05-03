#!/usr/bin/env python3
import json
import os
import urllib.request

ORG = "SMI"
_IGNORE = (
    ".github",
    "docs",
)


def main() -> int:

    gh_pat = os.environ["GITHUB_PAT"]

    req = urllib.request.Request(
        f"https://api.github.com/orgs/{ORG}/repos",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {gh_pat}",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urllib.request.urlopen(req) as resp:
        repo_data = json.loads(resp.read().decode())

    print("| Name | Description |")
    print("| ---- | ----------- |")
    for repo in sorted(repo_data, key=lambda x: (-x["stargazers_count"], x["name"])):

        if repo["name"] in _IGNORE or repo["visibility"] != "public":
            continue

        desc = repo["description"] or ""
        print(f"| [{repo['name']}]({repo['html_url']}) | {desc} |")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
