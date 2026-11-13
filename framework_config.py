import os

# Environment
TEST_ENV = os.getenv("TEST_ENV") or "tst"

# Browsers
BROWSERS = (os.getenv("BROWSERS") or "chromium").split(",")

# Retry configuration
RETRIES = int(os.getenv("RETRIES") or "1")
RETRY_DELAY = int(os.getenv("RETRY_DELAY") or "1")