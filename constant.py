import os
from pathlib import Path
from dotenv import load_dotenv
from framework_config import ENVIRONMENT


ENV_FILE = (
    Path(__file__).resolve().parent
    / "env"
    / f".{ENVIRONMENT}.env"
)


load_dotenv(ENV_FILE)

BASE_URL = os.getenv("BASE_URL")
if not BASE_URL:
    raise ValueError("BASE_URL is not configured.")

ANNUAL_INTEREST_RATE = 0.0788
TIMEOUT = 500