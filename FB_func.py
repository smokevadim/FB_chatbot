import json
import random
from pymessenger.bot import Bot
from tokens import *


def verify_fb_token(hub_challenge, token_sent):
    '''Check token from FB'''
    if token_sent == FB_VERIFY_TOKEN:
        return hub_challenge
    return 'Invalid verification token!'


def send_message(recipient_id, message):
    '''Send txt message to user in FB'''
    chatbot = Bot(FB_VERIFY_TOKEN)
    chatbot.send_text_message(recipient_id, message)
    return 'success'


def get_message():
    '''Random messages'''
    sample_messages = ['Great!', 'Its awesome!', 'Just do it again!', 'Cool!!!']
    return random.choice(sample_messages)


def p(message):
    print('>>>{}>>>{}'.format(type(message), message))


