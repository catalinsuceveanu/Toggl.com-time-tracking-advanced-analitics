import requests
import json
from requests.auth import HTTPBasicAuth

API_URL = "https://api.track.toggl.com/api/v8/"
API_AUTH = HTTPBasicAuth("a450eba69fc631d8617db98559e47bef", "api_token")

# method for for each api request ( get_time_entries )
def authentification():
    """this is just an authentification tester, it returns a boolean about the succesfulness of the connection"""
    auth_state = False
    received_data = requests.get(f"{API_URL}me", auth=API_AUTH)
    if received_data.status_code != 200:
        print(
            "API is not working, staus code: "
            + str(received_data.status_code)
            + received_data.text
        )
        return auth_state
    else:
        print("API is working, staus code: " + str(received_data.status_code))
        datas = json.loads(received_data.text)
        auth_state = True
        return auth_state


def get_time_entry(entry_id):
    """retruns a time entry based on a entry id provided as arg"""
    output = []
    time_entry = requests.get(f"{API_URL}time_entries/{entry_id}", auth=API_AUTH)
    if time_entry.status_code != 200:
        print(
            "API is not working, staus code: "
            + str(time_entry.status_code)
            + time_entry.text
        )
    else:
        print("API is working, staus code: " + str(time_entry.status_code))
        output.insert(0, id)
        datas = json.loads(time_entry.text)
        for key in datas["data"]:
            value = datas["data"][key]
            print(f"{key} = {value}")
            if key == "start":
                output.insert(1, value)
            if key == "duration":
                output.insert(2, value)
        return output


def get_time_entries_in_range(start_date, end_date):
    """outputs a list of entries according to the start and end date from the args, for a specific authentification"""
    request = requests.get(
        f"{API_URL}time_entries?start_date={start_date}T00%3A00%3A00%2B00%3A00&end_date={end_date}T23%3A59%3A00%2B00%3A00",
        auth=API_AUTH,
    )
    datas = json.loads(request.text)
    return datas
