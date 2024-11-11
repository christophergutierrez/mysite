"""Main application file for the personal website."""

from fasthtml.common import fast_app
from starlette.staticfiles import StaticFiles
from website.handlers.ama_handler import handle_question
from website.pages.experience import experience_page
from website.pages.home import home_page
from website.pages.ama import ama_page
from website.pages.my_blog import my_blog_page


def create_app():
    """Create and configure the application."""
    app, router = fast_app()

    # Mount static directory - updated path
    app.mount("/website/static", StaticFiles(directory="website/static"), name="static")

    # Register page routes
    router("/")(home_page)
    router("/experience")(experience_page)
    router("/ama")(ama_page)
    router("/my_blog")(my_blog_page)

    # Register API endpoints
    router("/ask", methods=["POST"])(handle_question)

    return app
