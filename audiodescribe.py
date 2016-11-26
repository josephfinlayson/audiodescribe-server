import gevent.monkey
gevent.monkey.patch_all()

from flask import Flask, request, redirect, url_for, send_from_directory, Response
from utils.RequestHelper import processRequest
from utils.interpret import getDescription
import json
import os.path
import uuid

app = Flask(__name__)




UPLOAD_FOLDER = './folder'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SEND_IMAGE_URL'] = False#True

emotion_url = 'https://api.projectoxford.ai/emotion/v1.0/recognize'
emotion_params = {}

face_urls = 'https://api.projectoxford.ai/face/v1.0/detect[?returnFaceId][&returnFaceLandmarks][&returnFaceAttributes]'
face_params = {'returnFaceAttributes': 'age, gender'}

general_purpose_recognition_url = 'https://api.projectoxford.ai/vision/v1.0/analyze'
general_purpose_params = {'visualFeatures': 'Description,Faces'}

description_url = 'https://api.projectoxford.ai/vision/v1.0/describe'
description_params = {'maxCandidates': 3}

ocr_url = 'https://api.projectoxford.ai/vision/v1.0/ocr'
ocr_params = {'detectOrientation': True}

response_headers = dict()
response_headers['Content-Type'] = 'application/json'

@app.route('/uploads/<filename>')
def uploaded_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/', methods=['GET', 'POST'])
def recognize_image():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            result = json.dumps({'error': True, 'message': 'no file'})
            return Response(response=json.dumps(result), content_type='application/json')

        file = request.files['file']

        if file:
            data = None
            if app.config['SEND_IMAGE_URL']:
                data = None
                filename = str(uuid.uuid1()) + '.jpg'
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                img_json = {'url': url_for('uploaded_image', filename=filename, _external=True)}
                print 'img_json: ', img_json
            else:
                data = file.read()
                img_json = None

            # we hit all APIs simultaneously, getting a plain english description of an image,

            jobs = []

            if request.args.get('general', 'true') == 'true':
                jobs.append( (processRequest, 'general', data, img_json, general_purpose_params, general_purpose_recognition_url) )

            if request.args.get('emotions', 'true') == 'true':
                jobs.append( (processRequest, 'emotions', data, img_json, general_purpose_params, emotion_url) )

            if request.args.get('ocr', 'true') == 'true':
                jobs.append( (processRequest, 'ocr', data, img_json, general_purpose_params, ocr_url) )


            asyncJobs = [ gevent.spawn(*jobArgs) for jobArgs in jobs ]

            # Always save the image, but if we don't need the links, wait until we've fired off the requests.
            if data:
                filename = str(uuid.uuid1()) + '.jpg'
                fd = open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'wb')
                fd.write(data)
                fd.close()

            gevent.joinall(asyncJobs, timeout=10)

            api_responses = dict(job.value for job in asyncJobs)

            response = Response(response=json.dumps(getDescription(api_responses)), content_type='application/json')

            return response

            # return redirect(url_for('uploaded_file', filename=filename))

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


if __name__ == '__main__':
    app.run()
