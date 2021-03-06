import traceback
import collections

def highest_emotion(emotion_obj):
    scores = emotion_obj['scores'].items()

    def second(t): return t[1]

    return reversed(sorted(scores, key=second)).next()[0]

def primary_emotion(emotions):
    emotion_counts = collections.Counter()
    for e in emotions:
        emotion_counts[highest_emotion(e)] += 1

    return emotion_counts.most_common(1)[0][0]

def getEmotionDescription(responses, _):
    if 'emotions' in responses:
        emotions = responses['emotions']
        if emotions:
            emotion = primary_emotion(emotions)
            mapping = {
                "sadness": 'sad',
                "neutral": 'neutral',
                "contempt": 'contemptuous',
                "disgust": 'disgusted',
                "anger": 'angry',
                "surprise": 'surprised',
                "fear": 'fearful',
                "happiness": 'happy'
            }
            mapped_emotion = mapping[emotion]
            return "People seem mostly %s"%(mapped_emotion)

def getCaption(responses, _):
    if 'general' in responses:
        return responses['general']['description']['captions'][0]['text']

def getFaceDescription(responses, _):
    if 'general' in responses:
        if 'faces' in responses['general'] and responses['general']['faces']:
            faces = responses['general']['faces']
            ages = set(face['age'] for face in faces)
            no_of_men = len([face for face in faces if face['gender'] == 'Male'])
            no_of_women = len([face for face in faces if face['gender'] == 'Female'])

            return '%d men, and %d women. Ages from %d to %d'%(no_of_men, no_of_women, min(ages), max(ages))

def getOCR(responses, _):
    if 'ocr' in responses:
        lines = []
        ocr = responses['ocr']
        for region_obj in ocr['regions']:
            for line_obj in region_obj['lines']:
                line_words = []
                for word_obj in line_obj['words']:
                    line_words.append(word_obj['text'])
                lines.append(' '.join(line_words))
        if lines and len(lines[0]) > 0:
            return "\n".join(lines)

def getGoogleOCR(responses, _):
    descriptions = []
    if 'ocr-google' in responses:
        descriptions.append(responses['ocr-google']['responses'][0]['textAnnotations'][0]['description'])
        #for textAnnotation in responses['ocr-google']['responses'][0]['textAnnotations']:
        #    descriptions.append(textAnnotation['description'])
    if descriptions:
        return " ".join(descriptions)


describers = [getCaption, getFaceDescription, getEmotionDescription, getOCR, getGoogleOCR]

def getDescription(responses, request_args):
    results = []
    failed = []
    for describer in describers:
        try:
            description = describer(responses, request_args)
            if description:
                results.append(description)
        except Exception as err:
            print "Exception while getting description %s: %s"%(describer.__name__, err,)
            traceback.print_exc()
            print "Ignoring %s"%(describer.__name__,)
            failed.append(describer.__name__)

    if not results:
        description = "Sorry, didn't see anything"
    else:
        description = ".\n".join(results)

    return {"description": description, "debug": responses, "errors": failed}
