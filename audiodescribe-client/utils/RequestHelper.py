import requests
import os
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

recognize_url = 'https://api.projectoxford.ai/vision/v1.0/analyze'
_key = '7642486818ac4d34a8e0f0e055d9bcef'  # Here you have to paste your primary key
json = None
defaultHeaders = {
'Ocp-Apim-Subscription-Key': _key
}



#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#


def processRequest(data, params, url, headers):
    """
    Helper function to process the request to Project Oxford

    Parameters:
    json: Used when processing images from its URL. See API Documentation
    data: Used when processing image read from disk. See API Documentation
    headers: Used to pass the key information and the data type request
    :param url:
    """
    headers.update(defaultHeaders)

    retries = 0
    result = None

    while True:
        response = requests.request('post', url, json=json, data=data, headers=headers, params=params)
        print response.status_code
        if response.status_code == 429:

            print("Message: %s" % (response.json()['error']['message']))

            if retries <= _maxNumRetries:
                time.sleep(1)
                retries += 1
                continue
            else:
                print('Error: failed after retrying!')
                break

        elif response.status_code == 200 or response.status_code == 201:
            print (response.content)
            if 'content-length' in response.headers and int(response.headers['content-length']) == 0:
                result = None
            elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str):
                if 'application/json' in response.headers['content-type'].lower():
                    result = response.json() if response.content else None
                elif 'image' in response.headers['content-type'].lower():
                    result = response.content
        else:
            print("Error code: %d" % (response.status_code))
            print("Message: %s" % (response.json()))

        break

    return result
