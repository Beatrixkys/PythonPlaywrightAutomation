import os
from pathlib import Path
from dotenv import load_dotenv
from framework_config import TEST_ENV


ENV_FILE = (
    Path(__file__).resolve().parent
    / "env"
    / f".{TEST_ENV}.env"
)


load_dotenv(ENV_FILE)

BASE_URL = os.getenv("BASE_URL")
if not BASE_URL:
    raise ValueError("BASE_URL is not configured.")

ANNUAL_INTEREST_RATE = 0.0788
TIMEOUT = 500

CIMB_BASE_URL = os.getenv("CIMB_BASE_URL")
BASE_API_PLACEHOLDER = os.getenv("BASE_API_PLACEHOLDER")

POSTS_ENDPOINT = "/posts"
COMMENTS_ENDPOINT = "/comments"

AUTH_HEADERS ={}

POST_SCHEMA = {
    "userId": int,
    "id": int,
    "title": str,
    "body": str
}