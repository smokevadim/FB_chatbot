from googleapiclient.discovery import build
from random import randint
from tokens import *
import requests


def get_random_image(q=''):
    """
    Getting random image
    :param q:
    :return:
    """
    results = google_search(q, GOOGLE_API_KEY, GOOGLE_CSE_ID, num=1, imgSize='small', imgType='photo', start=randint(1,30))
    for result in results:
        try:
            for cse_image in result['pagemap']['cse_image']:
                return cse_image['src']
        except:
            return "/ᐠ｡ꞈ｡ᐟ\\"


def get_random_cat_image(q=''):
    return get_random_image('cute+' + q)


def google_search(search_term, api_key, cse_id, **kwargs):
    """
    just searching function using Google Custom Search API
    :param search_term:
    :param api_key:
    :param cse_id:
    :param kwargs:
    :return:
    """
    service = build("customsearch", "v1", developerKey=api_key, cache_discovery=False)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    if int(res['searchInformation']['totalResults'])>0:
        return res['items']
    return []


def download_image(url):
    """
    download image to local directory function
    :param url:
    :return:
    """
    if 'http' in url:
        req = requests.get(url)
        with open('/tmp/cat.jpg', 'wb') as f:
            f.write(req.content)
    return url

