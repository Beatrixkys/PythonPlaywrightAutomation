import pytest
from pathlib import Path


REPORT_DIR = Path("reports")
SCREENSHOT_DIR = REPORT_DIR / "screenshots"
TRACE_DIR = REPORT_DIR / "traces"


@pytest.fixture
def page(page):
    yield page