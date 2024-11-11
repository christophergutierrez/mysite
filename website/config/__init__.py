# config/__init__.py
"""Application configuration."""
from .assets import CUSTOM_CSS, CUSTOM_JS
from .settings import get_app_settings

__all__ = [
    'get_app_settings',
    'CUSTOM_CSS',
    'CUSTOM_JS',
]
