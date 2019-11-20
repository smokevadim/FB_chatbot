from flask import Flask, request
import random
from pymessenger import bot

ACCESS_TOKEN = 'EAANf5If7nRwBAA2EY7TZBZAtfjMQoNphZA6EHIbXjAvCSGDwpndjP8kYlCZAApOmh34qa3RZCuZCzc8Y7aaMOnjv2XRZBmAAZCwssmV7h2iprhkoCJjE78O318PWxFGWb7zcFFZAkHvTIboAN64HheKnQAfqZB3a4PVy6Vo7GILo8hcwZDZD'
app = Flask(__name__)

def verify_fb_token(token_sent):
    '''Check token from FB'''
    if token_sent == VERIFY_TOKEN:
        return request.args.get('hub.challenge')
    return 'Invalid verification token!'


def send_message(recipient_id, message):
    '''Send txt message to user in FB'''
    bot.send_text_message(recipient_id, message)
    return 'success'


def get_message():
    '''Random messages'''
    sample_messages = ['Great!', 'Its awesome!', 'Just do it again!', 'Cool!!!']
    return random.choice(sample_messages)


@app.route('/', methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        token_sent = request.args['hub.verify_token']
        return verify_fb_token(token_sent)
    else:
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    # ID
                    recipient_id = message['sender']['id']
                    if message['message'].get['text']:
                        response_sent_text = get_message()
                        send_message(recipient_id, response_sent_text)
                    # attachments
                    if message['message'].get['attachments']:
                        response_sent_nontext = get_message()
                        send_message(recipient_id, response_sent_nontext)
        return 'Message processed'


if __name__ == '__main__':
    app.run()
