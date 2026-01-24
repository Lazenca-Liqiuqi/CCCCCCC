#!/usr/bin/env python3
"""
Download 16 Anthropic Engineering articles as HTML files.
"""

import requests
from pathlib import Path
import time

# 16篇文章的slug映射
ARTICLES = [
    ("01", "contextual-retrieval"),
    ("02", "building-effective-agents"),
    ("03", "swe-bench-sonnet"),
    ("04", "claude-code-best-practices"),
    ("05", "claude-think-tool"),
    ("06", "multi-agent-research-system"),
    ("07", "desktop-extensions"),
    ("08", "a-postmortem-of-three-recent-issues"),
    ("09", "effective-context-engineering-for-ai-agents"),
    ("10", "building-agents-with-the-claude-agent-sdk"),
    ("11", "equipping-agents-for-the-real-world-with-agent-skills"),
    ("12", "writing-tools-for-agents"),
    ("13", "code-execution-with-mcp"),
    ("14", "beyond-permission-prompts"),  # 需要验证
    ("15", "effective-harnesses-for-long-running-agents"),
    ("16", "advanced-tool-use"),
]

BASE_URL = "https://www.anthropic.com/engineering/"
OUTPUT_DIR = Path(__file__).parent / "html"


def download_article(number: str, slug: str) -> bool:
    """Download single article HTML."""
    url = f"{BASE_URL}{slug}"
    filename = f"{number}-{slug}.html"
    output_path = OUTPUT_DIR / filename

    try:
        print(f"Downloading: {slug}...")
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(response.text)

        file_size = len(response.text)
        print(f"  ✓ Saved to {filename} ({file_size:,} bytes)")
        return True

    except requests.RequestException as e:
        print(f"  ✗ Error downloading {slug}: {e}")
        return False


def main():
    """Download all articles."""
    # Ensure output directory exists
    OUTPUT_DIR.mkdir(exist_ok=True)

    print(f"Starting download of {len(ARTICLES)} articles...")
    print(f"Output directory: {OUTPUT_DIR}\n")

    success_count = 0
    failed = []

    for number, slug in ARTICLES:
        if download_article(number, slug):
            success_count += 1
        else:
            failed.append((number, slug))

        # Be polite to the server
        time.sleep(0.5)

    print(f"\n{'='*50}")
    print(f"Download complete: {success_count}/{len(ARTICLES)} succeeded")

    if failed:
        print(f"\nFailed downloads:")
        for number, slug in failed:
            print(f"  - {number}: {slug}")


if __name__ == "__main__":
    main()
