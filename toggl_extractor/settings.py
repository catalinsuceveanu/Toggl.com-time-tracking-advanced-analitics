from requests.auth import HTTPBasicAuth


# these are toggl variables
API_URL_TOGGL = "https://api.track.toggl.com/api/v8"
API_AUTH_TOGGL = HTTPBasicAuth("a450eba69fc631d8617db98559e47bef", "api_token")
USER_AGENT_TOGGL = "user_agent=catalin@vipra.tech"
TOGGL_WORKSPACE_ID = "4951342"

# these are slack variables
SLACK_API_POST_URL = (
    "https://hooks.slack.com/services/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"
)
SLACK_ENGINEERING_CHANNEL = "C0276BTDGTU"
SLACK_GENERAL_CHANNEL = "C01GT9CKAR1"
SLACK_VDU_TESTING = "C0391JYQUTF"
SLACK_USERNAME = "VDU"
