# audiodescribe-server

# Install dependencies:
    pip install requests
    pip install flask
    pip install gevent
    pip install google-api-python-client
    pip install Pillow
    
# Run server:

Get google application credentials file from Filip. DO NOT CHECK IT IN TO A PUBLIC REPO

Doesn't reload on changes:

    GOOGLE_APPLICATION_CREDENTIALS=... FLASK_APP=audiodescribe.py flask run
    
And publicly accessible:

    GOOGLE_APPLICATION_CREDENTIALS=... FLASK_APP=audiodescribe.py flask run --host=0.0.0.0
    
Debug, reloads, causes issues for gevent, there's a different way:

    GOOGLE_APPLICATION_CREDENTIALS=... FLASK_APP=audiodescribe.py FLASK_DEBUG=1 flask run

# TODO:
* [DONE] Return {"desription": ...} with description ready to be read.
* [DONE] Confirm that requests are done in parallel
* [DONE] Run on public server, with linkable uploaded images
* [DONE, but disabled] Use uploaded image url to send to Microsof APIs
* [DONE] Use APIs appropriately, with appropriate parameters
* [DONE] Support request parameters to turn features on/off
* [DONE] Switch to google for ocr
  

curl -X POST -F file=@folder/14958047_1228744947196397_1386475895_o.jpg http://127.0.0.1:5000/ | jq .



