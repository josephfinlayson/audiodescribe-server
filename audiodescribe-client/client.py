import requests
from gtts import gTTS
import uuid
# system dependency on ffmpeg ->
from pydub import AudioSegment
from pydub.playback import play
import json

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


def reduceFacesIntoGenderAndAge(pv, cv):
    cv['numberOfMen'] = pv['numberOfMen'] + 1 if cv['gender'] == "Male" else pv['numberOfMen']
    cv['numberOfWomen'] = pv['numberOfWomen'] + 1 if cv['gender'] == "Female" else pv['numberOfWomen']
    # map ages into list, get highest and lower of list
    return cv



def getFaceObject(faceList):
    ages = map(lambda faceObject: faceObject['age'], faceList)
    faceObject = reduce(reduceFacesIntoGenderAndAge, faceList, {'numberOfMen': 0, 'numberOfWomen': 0})

    faceObject['ageMax'] = reduce(lambda pv, cv: pv if (pv > cv) else cv, ages)
    faceObject['ageMin'] = reduce(lambda pv, cv: pv if (pv < cv) else cv, ages)
    del faceObject['faceRectangle']
    del faceObject['gender']
    del faceObject['age']

    return faceObject

def getFaceString(faceObject):
    return 'it contains ' + str(faceObject['numberOfMen']) + ' men, and ' + str(faceObject['numberOfWomen']) + ' women. The ages ' \
           'range from ' + str(faceObject['ageMin']) + ' to ' + str(faceObject['ageMax'])

sampleDescriptor = {
    "faces": [{"gender": "Male", "age": 34, "faceRectangle": {"width": 215, "top": 463, "height": 215, "left": 157}},
              {"gender": "Male", "age": 35, "faceRectangle": {"width": 92, "top": 676, "height": 92, "left": 478}},
              {"gender": "Male", "age": 30, "faceRectangle": {"width": 87, "top": 569, "height": 87, "left": 992}},
              {"gender": "Male", "age": 27, "faceRectangle": {"width": 69, "top": 555, "height": 69, "left": 512}},
              {"gender": "Female", "age": 25, "faceRectangle": {"width": 60, "top": 513, "height": 60, "left": 924}},
              {"gender": "Male", "age": 30, "faceRectangle": {"width": 51, "top": 460, "height": 51, "left": 644}},
              {"gender": "Female", "age": 33, "faceRectangle": {"width": 49, "top": 470, "height": 49, "left": 880}},
              {"gender": "Male", "age": 34, "faceRectangle": {"width": 42, "top": 433, "height": 42, "left": 740}}],
    "metadata": {"width": 1334, "format": "Jpeg", "height": 1001},
    "description": {
        "captions": [{"text": "Evanna Lynch et al. sitting at a table eating food", "confidence": 0.9383536254186131}],
        "tags": ["person", "table", "group", "sitting", "building", "people", "indoor", "food", "eating", "meal",
                 "posing", "restaurant", "large", "dinner", "man", "long", "glasses", "plate", "wine", "pizza",
                 "room"]}, "requestId": "9a667aaa-7234-44cd-89c4-e0657668334c"}



processedFaceObject = getFaceObject(sampleDescriptor['faces'])
faceAndGenderString = getFaceString(processedFaceObject)

# descriptionString = getDescriptorForImage('sample.jpg')

print faceAndGenderString
# sayText(descriptor['description']['captions'][0]['text'])
