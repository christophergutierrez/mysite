"""Experience page for the personal website."""

import json
from datetime import datetime
from pathlib import Path  # Add this import
# pylint: disable=no-name-in-module, import-error
from fasthtml.common import Div, Style, Script
from website.utils.helpers import create_menu
from website.config.assets import CUSTOM_CSS, CUSTOM_JS

# Load work history from JSON file
BASE_DIR = Path(__file__).parent.parent
with open(BASE_DIR / "data" / "work_history.json", "r", encoding="utf-8") as f:
    work_history = json.load(f)

def calculate_grid_position(start_date: str, end_date: str,
                          max_year_month: float) -> str:
    """
    Calculate grid row position based on month-level precision.

    Args:
        start_date: Start date in 'YYYY-MM-DD' format
        end_date: End date in 'YYYY-MM-DD' format or 'Present'
        max_year_month: Maximum year-month fraction for positioning

    Returns:
        CSS grid-row position string
    """
    if end_date == "Present":
        end_date = datetime.now().strftime("%Y-%m-%d")

    start_year, start_month = map(int, start_date.split("-")[:2])
    end_year, end_month = map(int, end_date.split("-")[:2])

    start_fractional_year = start_year + (start_month - 1) / 12
    end_fractional_year = end_year + (end_month - 1) / 12

    start_row = int((max_year_month - start_fractional_year) * 12 + 1)
    end_row = int((max_year_month - end_fractional_year) * 12 + 2)

    return f"grid-row: {start_row} / {end_row};"

def experience_page():
    """Generate the experience page content."""
    def year_month_fraction(date: str) -> float:
        """Convert date string to year.month fraction."""
        if date == "Present":
            now = datetime.now()
            return now.year + (now.month - 1) / 12
        year, month = map(int, date.split("-")[:2])
        return year + (month - 1) / 12

    min_year_month = min(year_month_fraction(job["start_date"])
                        for job in work_history)
    max_year_month = max(year_month_fraction(job["end_date"])
                        for job in work_history)
    experience_blocks = []
    for job in work_history:
        grid_position = calculate_grid_position(
            job["start_date"],
            job["end_date"],
            max_year_month  # Removed unused min_year_month argument
        )
        experience_blocks.append(
            Div(
                Div(
                    f"{job['company']} | {job['title']}",
                    Div(job["description"], Class="description"),
                    Class="experience-block",
                ),
                Class="experience-row",
                Style=grid_position,
            )
        )

    menu = create_menu("/experience")

    timeline = Div(
        *[
            Div(str(year), Class="timeline-year")
            for year in range(int(max_year_month), int(min_year_month) - 1, -1)
        ],
        Class="timeline",
    )

    return Div(
        Style(CUSTOM_CSS),
        Script(CUSTOM_JS),
        menu,
        Div(
            timeline,
            Div(*experience_blocks, Class="experience-container"),
            Class="container",
        ),
    )
