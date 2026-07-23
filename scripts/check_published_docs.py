"""Verify that every Markdown document is reachable after a Pages deployment."""

import os
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urljoin
from urllib.request import urlopen


DOCS_DIR = Path("docs")
ATTEMPTS = 6
RETRY_SECONDS = 10


def published_path(source: Path) -> str:
    relative = source.relative_to(DOCS_DIR)
    if relative.name == "index.md":
        path = relative.parent.as_posix()
    else:
        path = relative.with_suffix("").as_posix()
    return f"{quote(path)}/"


def fetch(url: str) -> str:
    with urlopen(url, timeout=20) as response:
        if response.status != 200:
            raise RuntimeError(f"{url} returned HTTP {response.status}")
        return response.read().decode("utf-8")


def verify(base_url: str) -> list[str]:
    home_html = fetch(base_url)
    failures: list[str] = []

    for source in sorted(DOCS_DIR.rglob("*.md")):
        relative = source.relative_to(DOCS_DIR)
        if relative == Path("index.md"):
            continue

        path = published_path(source)
        if f'href="{path}"' not in home_html:
            failures.append(f"{source}: missing from published navigation")
            continue

        try:
            fetch(urljoin(base_url, path))
        except (HTTPError, URLError, RuntimeError) as error:
            failures.append(f"{source}: {error}")

    return failures


def main() -> int:
    base_url = os.environ.get("SITE_URL", "").strip()
    if not base_url:
        print("SITE_URL is required.")
        return 1
    if not base_url.endswith("/"):
        base_url += "/"

    for attempt in range(1, ATTEMPTS + 1):
        try:
            failures = verify(base_url)
        except (HTTPError, URLError, RuntimeError) as error:
            failures = [str(error)]

        if not failures:
            count = sum(1 for _ in DOCS_DIR.rglob("*.md"))
            print(f"All {count} Markdown files are published and discoverable.")
            return 0

        print(f"Published-site check {attempt}/{ATTEMPTS} failed:")
        for failure in failures:
            print(f"- {failure}")

        if attempt < ATTEMPTS:
            time.sleep(RETRY_SECONDS)

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
