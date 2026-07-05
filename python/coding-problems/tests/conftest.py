"""Shared helper for testing solution files.

Solution filenames start with digits (e.g. ``128_longest_consecutive_sequence.py``),
which are not valid Python module names, so tests load them by file path instead
of a regular import.
"""

import importlib.util
from pathlib import Path

PROBLEMS_DIR = Path(__file__).parent.parent


def load_solution(relative_path: str):
    """Import a solution module given its path relative to coding-problems/.

    Example:
        module = load_solution("leetcode/128_longest_consecutive_sequence.py")
        assert module.Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    """
    path = PROBLEMS_DIR / relative_path
    module_name = "solution_" + path.stem
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
