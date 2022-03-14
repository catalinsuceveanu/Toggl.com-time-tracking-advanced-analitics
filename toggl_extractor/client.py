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
        response = requests.get(
            generate_api_report_url(start_date, end_date, current_page),
            auth=API_AUTH,
        )
        report = json.loads(response.text)

        for entry in report["data"]:
            time_entries.append(entry)

        if len(time_entries) >= report["total_count"]:
            break
        current_page += 1

    return time_entries


def generate_api_report_url(start_date, end_date, page_no):
    API_REPORT_URL = "https://api.track.toggl.com/reports/api/v2"
    return (
        f"{API_REPORT_URL}/details?workspace_id={WORKSPACE_ID}&since={start_date}&until={end_date}&{USER_AGENT}&page={page_no}",
    )


# def check_authentification():
#     """
#     This checks if the authentication passes on Toggl
#     Returns `true` if connection is succesfful, `false` otherwise
#     """
#     request = requests.get(f"{API_URL}/me", auth=API_AUTH)
#     return request.status_code == 200


# def get_time_entries_in_range(start_date):
#     """
#         outputs a list of entries according to the start and end date from the args,
#         for a specific authentification
#     """

#     request = requests.get(
#         f"{API_URL}/time_entries?start_date={start_date}T00%3A00%3A00%2B00%3A00&end_date={YESTERDAY}T23%3A59%3A00%2B00%3A00",
#         auth=API_AUTH,
#     )
#     all_data = json.loads(request.text)
#     return all_data
