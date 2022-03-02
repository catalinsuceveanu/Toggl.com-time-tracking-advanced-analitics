import requests
import json
from datetime import date, timedelta
from requests.auth import HTTPBasicAuth

API_URL = "https://api.track.toggl.com/api/v8/"
API_REPORT = "https://api.track.toggl.com/reports/api/v2/"
API_AUTH = HTTPBasicAuth("a450eba69fc631d8617db98559e47bef", "api_token")
yesterday = date.today() - timedelta(1)

# method for for each api request ( get_time_entries )
def check_authentification():
    """this is just an authentification tester, it returns a boolean about the succesfulness of the connection"""
    try:
        request = requests.get(f"{API_URL}me", auth=API_AUTH)
        return request.status_code == 200
    except:
        return False


def get_time_entry(entry_id):
    """retruns a time entry based on a entry id provided as arg"""
    try:
        output = []
        request = requests.get(f"{API_URL}time_entries/{entry_id}", auth=API_AUTH)
        if request.status_code == 200:
            output.insert(0, id)
            datas = json.loads(request.text)
            for key in datas["data"]:
                value = datas["data"][key]
                print(f"{key} = {value}")
                if key == "start":
                    output.insert(1, value)
                if key == "duration":
                    output.insert(2, value)
            return output

        else:
            return request.status_code

    except:
        return False


def get_time_entries_in_range(start_date):
    """outputs a list of entries according to the start and end date from the args, for a specific authentification"""
    try:
        request = requests.get(
            f"{API_URL}time_entries?start_date={start_date}T00%3A00%3A00%2B00%3A00&end_date={yesterday}T23%3A59%3A00%2B00%3A00",
            auth=API_AUTH,
        )
        datas = json.loads(request.text)
        return datas
    except:
        return False


def get_detailed_report(start_date):
    request = requests.get(
        f"{API_REPORT}details?workspace_id=4951342&since={start_date}&until={yesterday}&user_agent=api_test"
    )
    print(request.status_code)
    # datas = json.loads(request.text)
    # return datas
