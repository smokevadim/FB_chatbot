import random
from tokens import *
import json
from requests_toolbelt import MultipartEncoder
import requests


def verify_fb_token(hub_challenge, token_sent):
    """
    Check token from FB
    :param hub_challenge:
    :param token_sent:
    :return:
    """
    if token_sent == FB_VERIFY_TOKEN:
        return hub_challenge
    return 'Invalid verification token!'


def send_message(recipient_id, message_text):
    """
    direct request to messenger
    :param recipient_id:
    :param message_text:
    :return:
    """
    params = {"access_token": FB_VERIFY_TOKEN}

    data = {
        'recipient': json.dumps({
            'id': recipient_id
        }),
        'message': json.dumps({
            'text': message_text
        })
    }

    multipart_data = MultipartEncoder(data)

    multipart_header = {'Content-Type': multipart_data.content_type}

    r = requests.post("https://graph.facebook.com/v5.0/me/messages", params=params, headers=multipart_header,
                      data=multipart_data)
    if r.status_code != 200:
        send_message(recipient_id, 'Repeat please?')
    return 'success'


def send_image(recipient_id, message_text):
    """
    direct request to messenger
    :param recipient_id:
    :param message_text:
    :return:
    """
    params = {"access_token": FB_VERIFY_TOKEN}

    data = {
        'recipient': json.dumps({
            'id': recipient_id
        }),
        'message': json.dumps({
            'attachment': {
                'type': 'image',
                'payload': {}
            }
        }),
        'filedata': ('cat.jpg', open('/tmp/cat.jpg', 'rb'), 'image/png')
    }

    multipart_data = MultipartEncoder(data)
    multipart_header = {'Content-Type': multipart_data.content_type}

    r = requests.post("https://graph.facebook.com/v5.0/me/messages", params=params, headers=multipart_header,
                      data=multipart_data)
    if r.status_code != 200:
        send_message(recipient_id, 'Repeat please?')
    return 'success'


def get_random_message():
    """
    Random messages
    :return: random sample message
    """
    sample_messages = ['Great!', 'Its awesome!', 'Just do it again!', 'Cool!!!']
    return random.choice(sample_messages)


def p(message):
    print('>>>{}>>>{}'.format(type(message), message))
