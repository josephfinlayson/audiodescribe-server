def getFaceDescription(faces):
    ages = set(face['age'] for face in faces)
    no_of_men = len([face for face in faces if face['gender'] == 'Male'])
    no_of_women = len([face for face in faces if face['gender'] == 'Female'])

    return '%d men, and %d women. Ages from %d to %d'%(no_of_men, no_of_women, min(ages), max(ages))

def getDescription(responses):
    results = []
    if 'general' in responses:
        # TODO, handle missing
        results.append(responses['general']['description']['captions'][0]['text'])
        if 'faces' in responses['general'] and responses['general']['faces']:
            results.append(getFaceDescription(responses['general']['faces']))

    if not results:
        description = "Sorry, didn't see anything"
    else:
        description = ".\n".join(results)

    return {"description": description, "debug": responses}
