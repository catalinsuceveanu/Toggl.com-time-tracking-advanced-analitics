from tokenize import String
import requests
import json
from datetime import date, timedelta
from requests.auth import HTTPBasicAuth

API_URL = "https://api.track.toggl.com/api/v8"

API_AUTH = HTTPBasicAuth("a450eba69fc631d8617db98559e47bef", "api_token")

USER_AGENT = "user_agent=catalin@vipra.tech"
WORKSPACE_ID = "4951342"


def get_time_entries(start_date, end_date):
    time_entries = []
    current_page = 1

    while True:
        response = generate_api_report_url(start_date, end_date, current_page)
        report = json.loads(response.text)

        for entry in report["data"]:
            time_entries.append(entry)

        if len(time_entries) >= int(report["total_count"]):
            break
        else:
            current_page += 1

    return time_entries


def generate_api_report_url(start_date, end_date, page_no):
    API_REPORT_URL = "https://api.track.toggl.com/reports/api/v2"
    response = requests.get(
        f"{API_REPORT_URL}/details?workspace_id={WORKSPACE_ID}&since={start_date}&until={end_date}&{USER_AGENT}&page={page_no}",
        auth=API_AUTH,
    )
    return response
