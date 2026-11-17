import os
from pathlib import Path
from framework_config import BROWSERS, RETRIES, RETRY_DELAY
from utils.api import api_helper
from utils.api.api_client import APIClient
import pytest

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

@pytest.fixture
def api_client():
    def _client(base_url, extra_headers=None, override_all=False):
        headers = api_helper.get_headers(extra_headers, override_all)
        proxies = None
        if str(os.getenv("USE_ZAP")).lower() == "true":
            proxies = {
                "http": "http://localhost:8080",
                "https": "http://localhost:8080"
            }

        return APIClient(base_url=base_url, headers=headers, proxies=proxies)
    return _client