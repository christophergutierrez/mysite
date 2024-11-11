"""Blog redirect page."""
from starlette.responses import RedirectResponse

def my_blog_page():
    """Redirect to external blog."""
    return RedirectResponse(url="https://christophergutierrez.github.io", status_code=302)
