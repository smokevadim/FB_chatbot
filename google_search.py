from tokens import *
import requests
import random
import json

def get_image_cat(query):
    req = requests.request(
        'GET', 'https://www.googleapis.com/customsearch/v1?cx={}&key={}&searchType=image&imgSize=medium&safe=active&q=cat+{}'.format(GOOGLE_CX, GOOGLE_API_KEY, query)
    )
    j = json.loads(req.text)

    return random.choice(j['items'])['link']
