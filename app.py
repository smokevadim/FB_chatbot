import json
import random
from pymessenger.bot import Bot
from vars import *


def verify_fb_token(event, token_sent):
    '''Check token from FB'''
    if token_sent == VERIFY_TOKEN:
        return event.get('queryStringParameters').get('hub.challenge')
    return 'Invalid verification token!'


def send_message(recipient_id, message):
    '''Send txt message to user in FB'''
    chatbot = Bot(VERIFY_TOKEN)
    chatbot.send_text_message(recipient_id, message)
    return 'success'


def get_message():
    '''Random messages'''
    sample_messages = ['Great!', 'Its awesome!', 'Just do it again!', 'Cool!!!']
    return random.choice(sample_messages)


def p(message):
    print('>>>{}>>>{}'.format(type(message), message))


def lambda_handler(event, context):
    if 'httpMethod' in event:

        # this is GET request
        if event['httpMethod'] == 'GET':
            if ('queryStringParameters' in event) and ('hub.verify_token' in event['queryStringParameters']):
                token_sent = event['queryStringParameters']['hub.verify_token']
                return {
                    'statusCode': 200,
                    'body': verify_fb_token(event, token_sent)
                }

        # this is POST request
        else:
            print('---------\nEvent:{}\n-------------{}\n-------------'.format(event, context))
            if event['body'] is not None and 'entry' in event['body']:
                p(event['body'])
                entries = json.loads(event['body'])['entry']
                p(entries)
                for entry in entries:
                    if entry is not None and 'messaging' in entry:
                        messaging = entry['messaging']
                        p(messaging)
                        for message in messaging:
                            if message is not None and 'message' in message:
                                # ID
                                p(message)
                                recipient_id = message['sender']['id']
                                if message['message'].get('text'):
                                    response_sent_text = get_message()
                                    send_message(recipient_id, response_sent_text)
                                # attachments
                                if message['message'].get('attachments'):
                                    response_sent_nontext = get_message()
                                    send_message(recipient_id, response_sent_nontext)
            return {
                'statusCode': 200,
                'body': json.dumps('OK')
            }
    return {
        'statusCode': 403
    }