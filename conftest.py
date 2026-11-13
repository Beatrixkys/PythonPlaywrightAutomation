from pathlib import Path
from framework_config import BROWSERS, RETRIES, RETRY_DELAY

PROJECT_ROOT = Path(__file__).resolve().parent

REPORT_DIR = PROJECT_ROOT / "reports"
SCREENSHOT_DIR = REPORT_DIR / "screenshots"
TRACE_DIR = REPORT_DIR / "traces"

def pytest_configure(config):
    config.option.browser = [
        browser.strip() for browser in BROWSERS
    ]
    config.option.reruns = RETRIES
    config.option.reruns_delay = RETRY_DELAY