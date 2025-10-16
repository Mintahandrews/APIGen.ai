"""Example OpenAPI specifications for testing."""

import os
from pathlib import Path

EXAMPLES_DIR = Path(__file__).parent

def get_example_path(name: str) -> Path:
    """Get path to an example file."""
    return EXAMPLES_DIR / name

__all__ = ['EXAMPLES_DIR', 'get_example_path']