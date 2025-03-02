
"""Run script for the website in both development and production environments."""

import os
import sys
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

try:
    from website.app import create_app
    from website.config.settings import get_app_settings

    settings = get_app_settings()
    app = create_app()

    if __name__ == "__main__":
        import uvicorn
        
        # Use settings port for consistency
        port = settings["port"]
        logger.info(f"Starting server on port {port}")
        
        uvicorn.run(
            app,  # Use the app directly instead of "run:app" string
            host="0.0.0.0",  # Ensure it's accessible publicly
            port=port,
            log_level="info"
        )
except Exception as e:
    logger.error(f"Failed to start application: {e}")
    sys.exit(1)
