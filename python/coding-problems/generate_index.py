"""Regenerate the solution tables in coding-problems/README.md.

Scans each platform folder, pulls the problem URL from the comment at the top
of each solution file, and rewrites everything between the BEGIN/END markers
in README.md. Content outside the markers is left untouched.

Usage:
    uv run python coding-problems/generate_index.py
"""

import re
from pathlib import Path

PROBLEMS_DIR = Path(__file__).parent
README = PROBLEMS_DIR / "README.md"
BEGIN_MARKER = "<!-- BEGIN GENERATED INDEX (run generate_index.py) -->"
END_MARKER = "<!-- END GENERATED INDEX -->"

PLATFORMS = [
    ("leetcode", "LeetCode"),
    ("hackerrank", "HackerRank"),
    ("codesignal", "CodeSignal"),
    ("misc", "Miscellaneous (AlgoExpert & others)"),
]

URL_PATTERN = re.compile(r"https?://\S+")


def extract_url(path: Path) -> str | None:
    """Return the first URL in the file's header comment, if any."""
    with open(path, encoding="utf-8") as file:
        for line in file.readlines()[:10]:
            match = URL_PATTERN.search(line)
            if match:
                return match.group().rstrip("\"')")
    return None


def format_title(path: Path) -> tuple[str, str]:
    """Split a filename like 128_longest_consecutive_sequence into ('128', 'Longest Consecutive Sequence')."""
    number, _, rest = path.stem.partition("_")
    title = rest.replace("_", " ").title() if rest else path.stem
    return number, title


def build_table(folder: Path) -> str:
    rows = ["| # | Problem | Solution |", "|---|---------|----------|"]
    for path in sorted(
        folder.glob("*.py"), key=lambda p: (len(p.stem.split("_")[0]), p.stem)
    ):
        number, title = format_title(path)
        url = extract_url(path)
        problem = f"[{title}]({url})" if url else title
        rows.append(
            f"| {number} | {problem} | [{path.name}]({folder.name}/{path.name}) |"
        )
    return "\n".join(rows)


def build_index() -> str:
    sections = []
    total = 0
    for folder_name, display_name in PLATFORMS:
        folder = PROBLEMS_DIR / folder_name
        count = len(list(folder.glob("*.py")))
        total += count
        sections.append(f"### {display_name} ({count} solved)\n\n{build_table(folder)}")
    return f"**{total} problems solved so far.**\n\n" + "\n\n".join(sections)


def main() -> None:
    readme = README.read_text(encoding="utf-8")
    if BEGIN_MARKER not in readme or END_MARKER not in readme:
        raise SystemExit(f"Markers not found in {README}; refusing to overwrite.")
    head, _, tail = readme.partition(BEGIN_MARKER)
    _, _, tail = tail.partition(END_MARKER)
    README.write_text(
        f"{head}{BEGIN_MARKER}\n\n{build_index()}\n\n{END_MARKER}{tail}",
        encoding="utf-8",
    )
    print(f"Regenerated index in {README}")


if __name__ == "__main__":
    main()
