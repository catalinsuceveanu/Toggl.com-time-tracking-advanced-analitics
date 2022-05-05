from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

# these are toggl variables
TOGGL_API_URL = "https://api.track.toggl.com/api/v8/me"
TOGGL_DETAILED_REPORT_URL = "https://api.track.toggl.com/reports/api/v2"
TOGGL_API_AUTH = HTTPBasicAuth(os.getenv("TOGGL_TOKEN"), "api_token")
TOGGL_USER_AGENT = "user_agent=" + os.getenv("TOGGL_USER_AGENT")
# this ine looks like: user_agent=your_email@domain.com
TOGGL_WORKSPACE_ID = os.getenv("TOGGL_WORKSPACE_ID")

TOGGL_API_ERROR = (
    "There is an error with the TOGGL API settings. Check the enviroment variables."
)

# these are slack variables
SLACK_API_POST_URL = os.getenv("SLACK_API_POST_URL")
SLACK_ENGINEERING_CHANNEL = os.getenv("SLACK_ENGINEERING_CHANNEL")
SLACK_GENERAL_CHANNEL = os.getenv("SLACK_GENERAL_CHANNEL")
SLACK_VDU_TESTING = os.getenv("SLACK_VDU_TESTING")
SLACK_USERNAME = os.getenv("SLACK_USERNAME")

SLACK_API_ERROR = (
    "There is an error with the SLACK API settings. Check the enviroment variables."
)
