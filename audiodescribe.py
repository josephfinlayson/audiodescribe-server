from flask import Flask, request, redirect, url_for, send_from_directory, Response
from utils.RequestHelper import processRequest
import json

app = Flask(__name__)

UPLOAD_FOLDER = './folder'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

emotion_url = 'https://api.projectoxford.ai/emotion/v1.0/recognize'
recognize_url = 'https://api.projectoxford.ai/vision/v1.0/analyze'
response_headers = dict()
response_headers['Content-Type'] = 'application/json'


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            result = json.dumps({'error': True, 'message': 'no file'})
            return Response(response=json.dumps(result), content_type='application/json')

        file = request.files['file']

        if file:
            data = file.read()

            params = {'visualFeatures': 'Description,Faces'}
            result = processRequest(data, params, recognize_url)

            response = Response(response=json.dumps(result), content_type='application/json')

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
