from FB_func import *
from google_func import *
from flask import Flask, request
import json


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def lambda_handler(event = None, context = None):
    # If launched not in AWS Lambda

    if event is None:
        if request.method == 'GET':
            if 'hub.challenge' in request.args:
                token_sent = request.args['hub.verify_token']
                return verify_fb_token(request.args['hub.challenge'], token_sent)
        else:
            # making body same as in AWS Lambda
            event = {'body': {'entry': []}}
            events = request.get_json()['entry']
            for event_ in events:
                event['body']['entry'].append(event_)
            event['httpMethod'] = 'POST'
            event['body'] = json.dumps(event['body'])

    if 'httpMethod' in event:

        # this is GET request
        if event['httpMethod'] == 'GET':
            if ('queryStringParameters' in event) and ('hub.verify_token' in event['queryStringParameters']):
                token_sent = event['queryStringParameters']['hub.verify_token']
                return {
                    'statusCode': 200,
                    'body': verify_fb_token(event['queryStringParameters']['hub.challenge'], token_sent)
                }

        # this is POST request
        else:
            if event['body'] is not None and 'entry' in event['body']:
                entries = json.loads(event['body'])['entry']
                for entry in entries:
                    if entry is not None and 'messaging' in entry:
                        # yes, its message and we need to read it
                        proceed_message(entry['messaging'])
            return {
                'statusCode': 200,
                'body': json.dumps('OK')
            }
    return {
        'statusCode': 403
    }


def proceed_message(messaging):
    for message in messaging:
        if message is not None and 'message' in message:
            recipient_id = message['sender']['id']
            if message['message'].get('text'):
                incoming_message = message['message'].get('text')
                # here we can do what we want: read message and basic answer or execute action etc
                if not make_action(recipient_id, incoming_message):
                    send_message(recipient_id, get_random_message())


def make_action(recipient_id, incoming_message):
    response_sent_text = ''
    if '/help' in incoming_message.lower():
        response_sent_text = 'This is the FaceBook message bot,\nplease ask me "cat" if you want get pic of cuttie cat )'
    elif 'cat' in incoming_message.lower():
        download_image(get_random_cat_image(incoming_message.lower()))
        send_image(recipient_id, 'cat.jpg')
        return True
    else:
        return False

    send_message(recipient_id,response_sent_text)
    return True



if __name__ == '__main__':
    app.run()