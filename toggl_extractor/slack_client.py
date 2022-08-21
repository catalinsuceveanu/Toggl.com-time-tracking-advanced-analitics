import requests
from toggl_extractor import settings


def post_to_slack(message):

    payload = {
        "channel": settings.SLACK_VDU_TESTING,
        "username": settings.SLACK_USERNAME,
        "text": message,
    }
    try:
        request = requests.post(settings.SLACK_API_POST_URL, json=payload)
        if request.status_code == 200:
            print("The output for the required days was posted on slack")
        else:
            print(
                f" [{request.status_code}] error while posting to slack.\n"
                + settings.SLACK_API_ERROR
            )
    except:
        print(settings.SLACK_API_ERROR)
