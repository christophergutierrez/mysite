"""Asset configuration and loading."""
from pathlib import Path

def load_static_file(filepath: str) -> str:
    """Load static file content."""
    base_dir = Path(__file__).parent.parent
    with open(base_dir / filepath, "r", encoding="utf-8") as f:
        return f.read()

CUSTOM_CSS = load_static_file("static/css/styles.css")
CUSTOM_JS = load_static_file("static/js/custom.js")
