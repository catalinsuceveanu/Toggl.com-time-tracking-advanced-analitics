import re
import requests
import json
from requests.auth import HTTPBasicAuth

API_URL = "https://api.track.toggl.com/api/v8/"
API_AUTH = HTTPBasicAuth("26cef151fee3519a5fef575ffa498cad", "api_token")

# method for for each api request ( get_time_entries )
def authentification():
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


def get_time_entry(id):
    output = []
    time_entry = requests.get(f"{API_URL}time_entries/{id}", auth=API_AUTH)
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
            # print(f"{key} = {value}")
            if key == "start":
                output.insert(1, value)
            if key == "duration":
                output.insert(2, value)
        return output


def get_all_time_entries(user_id):
    output = []
    received_data = requests.get(f"{API_URL}me?with_related_data=true", auth=API_AUTH)
    if received_data.status_code != 200:
        print(
            "Connection failed, API code: "
            + str(received_data.status_code)
            + received_data.text
        )
    else:
        print("Connection succeded, API code: " + str(received_data.status_code))
        datas = json.loads(received_data.text)
        for key in datas["data"]:
            value = datas["data"][key]
            if key == "time_entries":
                output = value
                return output
