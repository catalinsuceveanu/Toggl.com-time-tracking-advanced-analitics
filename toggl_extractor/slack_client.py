from email import message
import requests
from toggl_extractor import settings


def post_to_slack(message):

    payload = {
        "channel": settings.ENGINEERING_CHANNEL,
        "username": settings.USERNAME,
        "text": message,
    }

    request = requests.post(settings.API_POST_URL, json=payload)
    return request.status_code
