"""Website configuration settings."""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
env_path = Path(__file__).parents[2] / '.env'
if env_path.exists():
    load_dotenv(dotenv_path=env_path)

def get_app_settings():
    """Get application settings based on environment."""
    env = os.environ.get("ENV", "DEV")

    if env == "DEV":
        port = int(os.environ.get("DEV_PORT", 5000))
    else:
        port = int(os.environ.get("PROD_PORT", 8080))

    settings = {
        "env": env,
        "port": port,
        "anthropic_api_key": os.environ.get("ANTHROPIC_API_KEY", ""),
        "openai_api_key": os.environ.get("OPENAI_API_KEY", ""),
        "openai_assistant_id": os.environ.get("OPENAI_ASSISTANT_ID", "")
    }

    return settings