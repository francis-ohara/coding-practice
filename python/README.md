# Python Practice Workspace

This repository is a collection of Python practice scripts, experimental projects, and algorithmic challenges, all managed as a unified [uv workspace](https://docs.astral.sh/uv/concepts/workspaces/).

## 📁 Directory Structure

```
python/
├── 0xx_...py                # Standalone experimental scripts.
├── 016-chapter_title_extractor/ # Software engineering textbook ToC parser.
├── 017-email_finder/         # Recursive email search tool.
├── 021-token-generation-with-itsdangerous/ # Secure token generation examples.
├── coding-problems/          # LeetCode, HackerRank, and CodeSignal solutions.
├── pyproject.toml            # Workspace configuration.
└── uv.lock                   # Project lockfile.
```

## 🚀 Projects

Every folder is an independent project with its own dependencies, but they all share a centralized management system.

### 📖 Chapter Title Extractor
Extracts chapter titles from Ian Sommerville's software engineering textbook using regex.

### 📧 Email Finder
A utility that recursively crawls directories to extract unique email addresses.

### 🔑 Token Generation (ItsDangerous)
Example of secure token generation for web apps using the `itsdangerous` library.

## ⚙️ Setup & Usage

Since this is a **uv workspace**, setting up is nearly instantaneous.

### 1. Initial Setup
Run this once in the **root** directory to set up the shared environment:
```bash
uv sync
source .venv/bin/activate
```

### 2. Running Projects
You can run any script directly from the root using `uv run`. 

**Standalone Scripts:**
```bash
uv run 001_python_asssert_statement.py
```

**Workspace Projects:**
`uv` automatically handles the environment for each project:
```bash
cd 021-token-generation-with-itsdangerous
uv run my_script.py
```

## 📝 Coding Problems
The `coding-problems` folder contains solutions to various algorithmic challenges. Use the root environment to run these.