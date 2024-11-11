"""Utility functions for the website."""

# pylint: disable=no-name-in-module
from pathlib import Path  # Add this import
import markdown
from fasthtml.common import Div


def create_menu(active_page):
    """Create the menu with the specified page marked as active."""
    menu_items = [
        ("Home", "/"),
        ("Experience", "/experience"),
        ("AMA", "/ama"),
        ("My Blog", "/my_blog"),
    ]

    menu_divs = []
    for name, href in menu_items:
        is_active = href == active_page
        menu_divs.append(
            Div(
                name,
                Class=f"menu-item{' active' if is_active else ''}",
                data_href=href,
                onclick=f"window.location.href='{href}';",
            )
        )

    return Div(*menu_divs, Class="menu")


def generate_from_markdown(file_path: str) -> str:
    """Convert markdown file content to HTML."""
    base_dir = Path(__file__).parent.parent  # Get the website package directory
    full_path = base_dir / "templates" / file_path

    with open(full_path, "r", encoding="utf-8") as f:
        text = f.read()
    # Convert markdown text to HTML
    return markdown.markdown(text)
