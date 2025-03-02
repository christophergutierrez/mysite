"""Application settings and configuration."""

import os
from pathlib import Path
from dataclasses import dataclass
from dotenv import load_dotenv


def load_env_vars():
    """Load environment variables from .env file, prioritizing local settings."""
    env_path = Path(__file__).parent.parent.parent / ".env"
    if env_path.exists():
        # Override existing environment variables with .env contents
        load_dotenv(env_path, override=True)

        # Double-check we're using the local version
        with open(env_path, "r", encoding="utf-8") as f:
            env_contents = dict(
                line.strip().split("=")
                for line in f
                if line.strip() and not line.startswith("#")
            )
            os.environ.update(env_contents)
    else:
        raise FileNotFoundError(f"Environment file not found at {env_path}")


@dataclass
class AppSettings:
    """Application settings container."""

    static_dir: Path
    template_dir: Path
    anthropic_api_key: str
    debug: bool = True


def get_app_settings() -> AppSettings:
    """Get application settings."""
    # Load environment variables with override
    load_env_vars()

    # Get base paths
    base_dir = Path(__file__).parent.parent

    return AppSettings(
        static_dir=base_dir / "static",
        template_dir=base_dir / "templates",
        anthropic_api_key=os.environ["ANTHROPIC_API_KEY"],  # Use os.environ directly
        debug=os.getenv("APP_ENV", "development") == "development",
    )
