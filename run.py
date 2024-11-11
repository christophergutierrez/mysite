"""Runner script for the website application."""
from website.app import create_app
import os
from uvicorn import run

app = create_app()

if __name__ == "__main__":
    # Select port based on the ENV environment variable
    env = os.environ.get('ENV', 'DEV').upper()
    port = int(os.environ.get('PROD_PORT', 8080)) if env == 'PROD' else int(os.environ.get('DEV_PORT', 5000))
    host = "0.0.0.0"
    
    # Run with uvicorn directly
    run(
        "run:app",
        host=host,
        port=port,
        reload=True
    )
