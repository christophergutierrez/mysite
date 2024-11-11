"""Runner script for the website application."""

from website.app import create_app

app = create_app()  # Create the app instance

if __name__ == "__main__":
    from website.app import serve
    serve()
