"""Setup configuration for the personal website package.

This module handles package metadata and dependencies for the FastHTML-based
personal website featuring dynamic content and OpenAI integration.
"""

from setuptools import setup, find_packages

setup(
    name="website",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "python-fasthtml",
        "markdown",
        "openai",
        "fastapi",
        "python-dotenv",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.12",
    ],
)
