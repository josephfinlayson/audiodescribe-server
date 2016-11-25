# import requests
# from gtts import gTTS
# import uuid
# # system dependency on ffmpeg ->
# from pydub import AudioSegment
# from pydub.playback import play
# import json
#
# import picamera
from gpiozero import Button
from signal import pause

# camera = picamera.PiCamera()


def recognize():
    print 'pressed '

RECOGNIZE_BUTTON_PIN = 18
recognize_button = Button(RECOGNIZE_BUTTON_PIN)
recognize_button.when_pressed = recognize


def ocr():
    print 'ocr pressed '

OCR_BUTTON_PIN = 23
ocr_button = Button(OCR_BUTTON_PIN)
ocr_button.when_pressed = ocr

#
# def getDescriptorForImage(image):
#     payload = {'file': open(image, "rb")}
#     response = requests.post("http://localhost:5000", files=payload)
#     print response.content
#     print response.text
#     return json.loads(response.content)
#
#
# def sayText(text):
#     tts = gTTS(text=text, lang='en')
#     filename = (text[:15] + str(uuid.uuid4().get_hex().upper()[0:6])) + '.mp3'
#     tts.save(filename)
#     song = AudioSegment.from_mp3(filename)
#     play(song)



# TODO, will get {"description": "...", "debug": {...}} from the api. Speak the description.



# descriptionString = getDescriptorForImage('sample.jpg')
# sayText(descriptor['description']['captions'][0]['text'])
pause()