# in modules/github_client.py
import requests
import json
from config import GITHUB_TOKEN, GITHUB_OWNER, GITHUB_REPO

BASE_URL = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def post_review_comment(pull_number, commit_id, body, path, line):
    """Posts a single review comment to a pull request."""
    url = f"{BASE_URL}/pulls/{pull_number}/comments"
    data = {
        "body": body,
        "commit_id": commit_id,
        "path": path,
        "line": line
    }
    response = requests.post(url, data=json.dumps(data), headers=HEADERS)
    if response.status_code == 201:
        print(f"Successfully posted comment to PR #{pull_number}")
    else:
        print(f"Failed to post comment: {response.json()}")

def set_commit_status(sha, state, description):
    """Sets a pass/fail/pending status on a specific commit."""
    url = f"{BASE_URL}/statuses/{sha}"
    data = {
        "state": state, # "success", "failure", "error", or "pending"
        "description": description,
        "context": "CI / Automated Code Review"
    }
    response = requests.post(url, data=json.dumps(data), headers=HEADERS)
    if response.status_code == 201:
        print(f"Successfully set status '{state}' for commit {sha[:7]}")
    else:
        print(f"Failed to set status: {response.json()}")