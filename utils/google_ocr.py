import base64

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()
service = discovery.build('vision', 'v1', credentials=credentials)

def get_google_ocr(image_data):
    image_content = base64.b64encode(image_data)
    service_request = service.images().annotate(body={
        'requests': [{
            'image': {
                'content': image_content.decode('UTF-8')
            },
            'features': [{
                'type': 'TEXT_DETECTION'
                #, 'maxResults': 1
            }]
        }]
    })

    response = service_request.execute()
    return ('ocr-google', response)
