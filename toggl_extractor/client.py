import requests
import json
from toggl_extractor import settings


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
        f"{API_REPORT_URL}/details?workspace_id={settings.TOGGL_WORKSPACE_ID}&since={start_date}&until={end_date}&{settings.USER_AGENT_TOGGL}&page={page_no}",
        auth=settings.API_AUTH_TOGGL,
    )
    return response
