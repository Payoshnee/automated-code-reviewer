# in config.py
import os
from dotenv import load_dotenv

# Load .env for local testing, but GitHub Actions will provide the variables in production
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_OWNER = os.getenv("GITHUB_OWNER")
GITHUB_REPO = os.getenv("GITHUB_REPO")