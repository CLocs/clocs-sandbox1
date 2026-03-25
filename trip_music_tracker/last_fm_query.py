import json
import pandas as pd
import requests
import pylast

from params import *

def lastfm_get(payload):
    # define headers and URL
    headers = headers_default
    url = 'https://ws.audioscrobbler.com/2.0/'

    # Add API key and format to the payload
    payload = payload_default
    payload['api_key'] = API_KEY
    payload['format'] = 'json'

    response = requests.get(url, headers=headers, params=payload)
    return response


def lastfm_get_user_info(payload):
    # define headers and URL
    headers = headers_default
    url = 'https://ws.audioscrobbler.com/2.0/'

    # Add API key and format to the payload
    payload = payload_default
    payload['api_key'] = API_KEY
    payload['format'] = 'json'

    response = requests.get(url, headers=headers, params=payload)
    return response


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
    return text


def get_some_lastfm():
    r = requests.get('https://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
    print(r.status_code)

    r = lastfm_get({
        'method': 'chart.gettopartists'
    })
    print(r.status_code)

    jprint(r.json())

    # r0 = responses[0]
    # r0_json = r0.json()
    # r0_artists = r0_json['artists']['artist']
    # r0_df = pd.DataFrame(r0_artists)
    # r0_df.head()

    pass


if __name__ == '__main__':
    get_some_lastfm()


