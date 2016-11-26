import requests
import time

_maxNumRetries = 0

def processRequest(name, _key, data, json, params, url):
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
        headers = {'Ocp-Apim-Subscription-Key': _key}
        if json:
            headers['Content-Type'] = 'application/json'
        else:
            headers['Content-Type'] = 'application/octet-stream'

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

    return (name, result)
