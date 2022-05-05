from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

TOGGL_API_URL = ""
TOGGL_API_AUTH = ""
TOGGL_USER_AGENT = ""
TOGGL_WORKSPACE_ID = ""
TOGGL_DETAILED_REPORT_URL = ""

# these are toggl variables
TOGGL_API_URL = os.getenv("TOGGL_API_URL")
TOGGL_API_AUTH = HTTPBasicAuth(os.getenv("TOGGL_TOKEN"), "api_token")
TOGGL_USER_AGENT = os.getenv("TOGGL_USER_AGENT")
TOGGL_WORKSPACE_ID = os.getenv("TOGGL_WORKSPACE_ID")
TOGGL_DETAILED_REPORT_URL = os.getenv("TOGGL_DETAILED_REPORT_URL")
TOGGL_API_ERROR = (
    "There is an error with the TOGGL API setting. Check the enviroment variables"
)

# these are slack variables
SLACK_API_POST_URL = os.getenv("SLACK_API_POST_URL")
SLACK_ENGINEERING_CHANNEL = os.getenv("SLACK_ENGINEERING_CHANNEL")
SLACK_GENERAL_CHANNEL = os.getenv("SLACK_GENERAL_CHANNEL")
SLACK_VDU_TESTING = os.getenv("SLACK_VDU_TESTING")
SLACK_USERNAME = os.getenv("SLACK_USERNAME")
