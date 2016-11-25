import requests
import time
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

recognize_url = 'https://api.projectoxford.ai/vision/v1.0/analyze'
_key = '7642486818ac4d34a8e0f0e055d9bcef'  # Here you have to paste your primary key
json = None
headers = dict()
headers['Ocp-Apim-Subscription-Key'] = _key
headers['Content-Type'] = 'application/octet-stream'
_maxNumRetries = 1

#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#

def processRequest(data, json, params, url):
    """
    Helper function to process the request to Project Oxford

    Parameters:
    json: Used when processing images from its URL. See API Documentation
    data: Used when processing image read from disk. See API Documentation
    headers: Used to pass the key information and the data type request
    :param url:
    """

    retries = 0
    result = None

    while True:
        response = requests.request('post', url, json=json, data=data, headers=headers, params=params)
        print '%s - %d'%(url, response.status_code)
        if response.status_code == 429:

            print("%s - Message: %s" % (url, response.json()['error']['message']))

            if retries <= _maxNumRetries:
                time.sleep(1)
                retries += 1
                continue
            else:
                print('%s - Error: failed after retrying!'%(url,))
                break

        elif response.status_code == 200 or response.status_code == 201:
            if 'content-type' in response.headers and isinstance(response.headers['content-type'], str):
                if 'application/json' in response.headers['content-type'].lower():
                    result = response.json() if response.content else None
                elif 'image' in response.headers['content-type'].lower():
                    result = response.content
        else:
            print("%s - Error code: %d" % (url, response.status_code))
            print("%s - Message: %s" % (url, response.json()))

        break

    return result
