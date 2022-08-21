import requests
import json
from toggl_extractor import settings
from datetime import date, timedelta


def get_time_entries(start_date, end_date):
    time_entries = []
    current_page = 1

    while True:
        response = requests.get(
            generate_api_report_url(start_date, end_date, current_page),
            auth=settings.TOGGL_API_AUTH,
        )
        report = json.loads(response.text)

        for entry in report["data"]:
            time_entries.append(entry)

        if len(time_entries) >= int(report["total_count"]):
            break
        else:
            current_page += 1

    return time_entries


def generate_api_report_url(start_date, end_date, page_no):
    url = f"{settings.TOGGL_DETAILED_REPORT_URL}/details?workspace_id={settings.TOGGL_WORKSPACE_ID}&since={start_date}&until={end_date}&{settings.TOGGL_USER_AGENT}&page={page_no}"
    return url


def check_toggl_api_settings():
    TODAY = date.today()
    YESTERDAY = date.today() - timedelta(1)
    try:
        check_auth_url_and_auth = requests.get(
            settings.TOGGL_API_URL, auth=settings.TOGGL_API_AUTH
        )
        check_user_agent_wrkspc_id_and_detailed_rep_url = requests.get(
            generate_api_report_url(YESTERDAY, TODAY, 1),
            auth=settings.TOGGL_API_AUTH,
        )
        if (
            check_auth_url_and_auth.status_code == 200
            and check_user_agent_wrkspc_id_and_detailed_rep_url.status_code == 200
        ):
            return True
        else:
            print(settings.TOGGL_API_ERROR)
            return False

    except:
        print(settings.TOGGL_API_ERROR)
        return False


print(check_toggl_api_settings())
