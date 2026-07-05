# Python Practice Workspace

A collection of Python practice scripts, experimental mini-projects, and algorithmic challenges, all managed as a unified [uv workspace](https://docs.astral.sh/uv/concepts/workspaces/).

## 📁 Directory Structure

```
python/
├── 0xx_...py             # Standalone TIL-style experiment scripts (see index below).
├── 0xx-.../              # Numbered mini-projects, each a uv workspace member.
├── coding-problems/      # LeetCode, HackerRank, CodeSignal & AlgoExpert solutions + tests.
├── pyproject.toml        # Workspace configuration (deps, ruff, pytest).
└── uv.lock               # Shared lockfile.
```

## 🧪 Experiment Scripts (TIL)

Small standalone scripts, each exploring one language feature or behavior:

| Script | What it explores |
|---|---|
| [000_infinite_recursion.py](000_infinite_recursion.py) | What happens when recursion never terminates |
| [001_python_asssert_statement.py](001_python_asssert_statement.py) | The `assert` statement |
| [002_pass_by_value_or_reference.py](002_pass_by_value_or_reference.py) | Whether Python passes arguments by value or reference |
| [003_for_loops_vs_list_comprehensions.py](003_for_loops_vs_list_comprehensions.py) | For loops vs. list comprehensions |
| [004_text_wrap_module.py](004_text_wrap_module.py) | The `textwrap` module |
| [005_HTH_assessment_1.py](005_HTH_assessment_1.py) | Practice assessment problem |
| [006_HTH_assessment_2.py](006_HTH_assessment_2.py) | Practice assessment problem |
| [007_collections_counter.py](007_collections_counter.py) | `collections.Counter` |
| [008_class_attribute_default_values.py](008_class_attribute_default_values.py) | Class attribute default values |
| [009_python_match_case.py](009_python_match_case.py) | Structural pattern matching (`match`/`case`) |
| [010_object_attributes_by_value_or_reference.py](010_object_attributes_by_value_or_reference.py) | Whether object attributes are copied or referenced |
| [011_python_requests_library.py](011_python_requests_library.py) | The `requests` library |
| [012_inheritance.py](012_inheritance.py) | Class inheritance |
| [013_python_asyncio.py](013_python_asyncio.py) | `asyncio` basics |
| [014_scope_test_in_python.py](014_scope_test_in_python.py) | Scoping rules |
| [015_linked_list.py](015_linked_list.py) | Implementing a singly-linked list |

## 🚀 Mini-Projects

Each numbered folder is an independent workspace member with its own dependencies and README:

| Project | Description |
|---|---|
| [016-chapter_title_extractor/](016-chapter_title_extractor/) | Extracts chapter titles from a software engineering textbook's ToC using regex |
| [017-email_finder/](017-email_finder/) | Recursively crawls directories to extract unique email addresses |
| [018-modules_and_packages/](018-modules_and_packages/) | Demonstrates Python module and package import mechanics |
| [019-pillow_image_types_support/](019-pillow_image_types_support/) | Notebook exploring image format support in Pillow |
| [020-text_counter/](020-text_counter/) | Counts words/characters in text |
| [021-token-generation-with-itsdangerous/](021-token-generation-with-itsdangerous/) | Secure token generation with the `itsdangerous` library |

New mini-project folders use kebab-case (like `021-token-generation-with-itsdangerous`).

## 📝 Coding Problems

[coding-problems/](coding-problems/) contains 149+ solutions organized by platform, with an auto-generated
index linking every solution to its original problem. See its [README](coding-problems/README.md).

## ⚙️ Setup & Usage

Run once in this directory to set up the shared environment (installs pytest too):

```bash
uv sync
```

Then:

```bash
uv run 013_python_asyncio.py                          # run a standalone script
uv run pytest                                         # run solution tests
uv run python coding-problems/generate_index.py       # regenerate the solutions index
uvx ruff check . && uvx ruff format --check .         # lint & format check (same as CI)
```

Workspace projects manage their own dependencies automatically:

```bash
cd 021-token-generation-with-itsdangerous
uv run itsdangerous_token_generation.py
```
