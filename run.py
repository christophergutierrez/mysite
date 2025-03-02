
"""Run script for the website in both development and production environments."""

import os
from website.app import create_app
from website.config.settings import get_app_settings

settings = get_app_settings()
app = create_app()

if __name__ == "__main__":
    import uvicorn
    
    port = int(os.environ.get("PROD_PORT", 8080))
    
    uvicorn.run(
        "run:app",
        host="0.0.0.0",  # Ensure it's accessible publicly
        port=port,
        log_level="info"
    )
