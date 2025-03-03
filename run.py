
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

    # Get settings
    settings = get_app_settings()
    
    # Create the app
    logger.info("Creating application")
    app = create_app()

    if __name__ == "__main__":
        import uvicorn
        
        # Use PORT environment variable if available (for Cloud deployments)
        port = int(os.environ.get("PORT", settings["port"]))
        logger.info(f"Starting server on port {port}")
        
        uvicorn.run(
            "website.app:create_app",  # Use string reference for better reload support
            host="0.0.0.0",  # Ensure it's accessible publicly
            port=port,
            log_level="info",
            factory=True
        )
except Exception as e:
    logger.error(f"Failed to start application: {e}")
    import traceback
    logger.error(traceback.format_exc())
    sys.exit(1)
