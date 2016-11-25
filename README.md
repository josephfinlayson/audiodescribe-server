# audiodescribe-server

# Install dependencies:
    pip install requests
    pip install flask
    pip install gevent
    
# Run server:

Doesn't reload on changes:

    FLASK_APP=audiodescribe.py flask run
    
Debug, reloads, causes issues for gevent, there's a different way:

    FLASK_APP=audiodescribe.py FLASK_DEBUG=1 flask run

# TODO:
* [DONE] Return {"desription": ...} with description ready to be read.
* [DONE] Confirm that requests are done in parallel
* Run on public server, with linkable uploaded images
* Use uploaded image url to send to Microsof APIs
* Use APIs appropriately, with appropriate parameters
* Support request parameters to turn features on/off
  

curl -X POST -F file=@folder/14958047_1228744947196397_1386475895_o.jpg http://127.0.0.1:5000/ | jq .



