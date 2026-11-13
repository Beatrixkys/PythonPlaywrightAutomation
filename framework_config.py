
import os

# Environment
ENVIRONMENT = os.getenv("TEST_ENV", "tst")
# Browsers
BROWSERS = os.getenv("BROWSERS", "chromium").split(",")
# Retry configuration
RETRIES = int(os.getenv("RETRIES", "1"))
RETRY_DELAY = int(os.getenv("RETRY_DELAY", "1"))
