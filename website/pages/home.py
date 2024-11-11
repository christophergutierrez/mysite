"""Call home page markdown."""
# pylint: disable=no-name-in-module
from fasthtml.common import Div, Style, Script, NotStr
from website.utils.helpers import create_menu, generate_from_markdown  # verify this import
from website.config.assets import CUSTOM_CSS, CUSTOM_JS

def home_page():
    """Generate the home page content."""
    menu = create_menu("/")
    content = NotStr(generate_from_markdown("home.md"))  # Just the filename


    return Div(
        Style(CUSTOM_CSS),
        Script(CUSTOM_JS),
        menu,
        content
    )
