import random
from pymessenger.bot import Bot
from tokens import *
import json
import os
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


# def send_message(recipient_id, message):
#     """
#     Send txt message to user in FB
#     :param recipient_id:
#     :param message:
#     :return: 'success'
#     """
#     chatbot = Bot(FB_VERIFY_TOKEN)
#     chatbot.send_text_message(recipient_id, message)
#     return 'success'

def send_message(recipient_id, message_text):
    """
    direct request to messenger
    :param recipient_id:
    :param message_text:
    :return:
    """
    params = {
        "access_token": FB_VERIFY_TOKEN
    }

    data = {
        'recipient': json.dumps({
            'id': recipient_id
        }),
        'message': json.dumps({
            'body': {
                'type': 'image',
                'payload': {}
            }
        }),
        'filedata': (os.path.basename('cat.jpg'), open('cat.jpg', 'rb'), 'image/png')
    }

    multipart_data = MultipartEncoder(data)

    multipart_header = {
        'Content-Type': multipart_data.content_type
    }

    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=multipart_header,
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
    params = {
        "access_token": FB_VERIFY_TOKEN
    }

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
        'filedata': (os.path.basename('cat.jpg'), open('cat.jpg', 'rb'), 'image/png')
    }

    multipart_data = MultipartEncoder(data)

    multipart_header = {
        'Content-Type': multipart_data.content_type
    }

    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=multipart_header,
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
