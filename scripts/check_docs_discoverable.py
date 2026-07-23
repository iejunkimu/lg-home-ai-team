"""Fail when a Markdown document is built but absent from site navigation."""

from pathlib import Path
from urllib.parse import quote


DOCS_DIR = Path("docs")
SITE_DIR = Path("site")


def output_path(source: Path) -> Path:
    relative = source.relative_to(DOCS_DIR)
    if relative.name == "index.md":
        return SITE_DIR / relative.parent / "index.html"
    return SITE_DIR / relative.with_suffix("") / "index.html"


def navigation_href(source: Path) -> str:
    relative = source.relative_to(DOCS_DIR)
    if relative.name == "index.md":
        path = relative.parent.as_posix()
    else:
        path = relative.with_suffix("").as_posix()
    return f"{quote(path)}/"


def main() -> int:
    home = SITE_DIR / "index.html"
    if not home.exists():
        print("site/index.html is missing; run `mkdocs build --strict` first.")
        return 1

    home_html = home.read_text(encoding="utf-8")
    missing_outputs: list[str] = []
    missing_navigation: list[str] = []
    sources = sorted(DOCS_DIR.rglob("*.md"))

    for source in sources:
        rendered = output_path(source)
        if not rendered.exists():
            missing_outputs.append(source.as_posix())

        relative = source.relative_to(DOCS_DIR)
        if relative == Path("index.md"):
            continue

        expected = f'href="{navigation_href(source)}"'
        if expected not in home_html:
            missing_navigation.append(source.as_posix())

    if missing_outputs:
        print("Markdown files missing rendered HTML:")
        for path in missing_outputs:
            print(f"- {path}")

    if missing_navigation:
        print("Markdown files missing from site navigation:")
        for path in missing_navigation:
            print(f"- {path}")

    if missing_outputs or missing_navigation:
        return 1

    print(f"All {len(sources)} Markdown files are rendered and discoverable.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
