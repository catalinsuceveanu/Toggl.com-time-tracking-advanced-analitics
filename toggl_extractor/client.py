import requests
import json
from datetime import date, timedelta
from requests.auth import HTTPBasicAuth

API_URL = "https://api.track.toggl.com/api/v8"
API_REPORT = "https://api.track.toggl.com/reports/api/v2"
API_AUTH = HTTPBasicAuth("a450eba69fc631d8617db98559e47bef", "api_token")
YESTERDAY = date.today() - timedelta(1)
USER_AGENT = "user_agent=catalin@vipra.tech"

# method for for each api request ( get_time_entries )
def check_authentification():
    """this is just an authentification tester, it returns a boolean about the succesfulness of the connection"""
    request = requests.get(f"{API_URL}/me", auth=API_AUTH)
    return request.status_code == 200


def get_time_entries_in_range(start_date):
    """outputs a list of entries according to the start and end date from the args, for a specific authentification"""

    request = requests.get(
        f"{API_URL}/time_entries?start_date={start_date}T00%3A00%3A00%2B00%3A00&end_date={YESTERDAY}T23%3A59%3A00%2B00%3A00",
        auth=API_AUTH,
    )
    all_data = json.loads(request.text)
    return all_data


def get_detailed_report(start_date, page_no):
    request = requests.get(
        f"{API_REPORT}/details?workspace_id=4951342&since={start_date}&until={YESTERDAY}&{USER_AGENT}&page={page_no}",
        auth=API_AUTH,
    )
    all_data = json.loads(request.text)
    return all_data
