"""AMA page for the personal website."""

# pylint: disable=no-name-in-module
from fasthtml.common import Div, Style, Script, Form, Input, Button
from website.utils.helpers import create_menu
from website.config.assets import CUSTOM_CSS, CUSTOM_JS

def ama_page():
    """
    Generate the AMA (Ask Me Anything) page content.
    
    Creates a page with a form for submitting questions and a response box
    for displaying answers, styled according to the site's theme.
    """
    menu = create_menu("/ama")

    form = Form(
        Input(
            id="question-input",
            Class="ama-input",
            placeholder="Type your question here...",
            type="text",
        ),
        Button(
            "Submit",
            id="submit-button",
            Class="ama-button",
            type="submit"
        ),
        id="ama-form",
        Class="ama-form",
    )

    response_box = Div(
        """
        Ask My Assistant!<br>
        Your reply will appear here. Some example questions:<br>
        - When did Chris work at Airbnb?<br>
        - Does Christopher know SQL?<br>
        - Has he managed people?
        """,
        id="response-box",
        Class="ama-response"
    )

    content = Div(form, response_box)

    return Div(
        Style(CUSTOM_CSS),
        Script(CUSTOM_JS),
        menu,
        content
    )
