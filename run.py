"""Runner script for the website application."""
import os
from uvicorn import run
from website.app import create_app

app = create_app()

if __name__ == "__main__":
    env = os.environ.get('ENV', 'DEV').upper()
    port = int(os.environ.get('PORT', 8080 if env == 'PROD' else 5000))

    # Run with uvicorn directly
    run(
        "run:app",
        host="0.0.0.0",
        port=port,
        reload=True
    )
