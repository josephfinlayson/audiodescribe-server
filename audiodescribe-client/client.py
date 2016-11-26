import requests
from gtts import gTTS
import uuid
import time
import os
# system dependency on ffmpeg ->
from pydub import AudioSegment
from pydub.playback import play
import json
from pydub import AudioSegment


import picamera
from gpiozero import Button
from signal import pause

API_URL = 'http://51.15.49.230:5000'
camera = picamera.PiCamera()

def getFileName():
    return uuid.uuid4().get_hex() + '.jpg'

def recognize():
    filename = getFileName()
    camera.capture(filename)
    sendRequest(filename, 'recog')

RECOGNIZE_BUTTON_PIN = 18
recognize_button = Button(RECOGNIZE_BUTTON_PIN)
recognize_button.when_pressed = recognize


def ocr():
    filename = getFileName()
    camera.capture(filename)
    sendRequest(filename, 'ocr')

OCR_BUTTON_PIN = 23
ocr_button = Button(OCR_BUTTON_PIN)
ocr_button.when_pressed = ocr

def sendRequest(filename, type):
    params = {}
    if type == 'ocr':
        params['ocr'] = "true"
    payload = {'file': open(filename, "rb")}
    response = requests.post(API_URL, files=payload, params=params)
    content = json.loads(response.content)
    desc = content['description']
    print desc
    sayText(desc)

#
# def getDescriptorForImage(image):

def sayText(text):
    tts = gTTS(text=text, lang='en')
    filename = (text[:15] + str(uuid.uuid4().get_hex().upper()[0:6])) + '.mp3'
    tts.save(filename)
    one_second_silence = AudioSegment.silent(duration=1000)
    song = one_second_silence + AudioSegment.from_mp3(filename)
    play(song)



# TODO, will get {"description": "...", "debug": {...}} from the api. Speak the description.



# descriptionString = getDescriptorForImage('sample.jpg')
# sayText(descriptor['description']['captions'][0]['text'])
pause()
