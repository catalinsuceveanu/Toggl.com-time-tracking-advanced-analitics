import requests
from toggl_extractor import settings


def post_to_slack(message):

    payload = {
        "channel": settings.SLACK_GENERAL_CHANNEL,
        "username": settings.SLACK_USERNAME,
        "text": message,
    }

    request = requests.post(settings.SLACK_API_POST_URL, json=payload)
    return request.status_code
