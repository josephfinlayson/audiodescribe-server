import traceback

def getCaption(responses):
    if 'general' in responses:
        return responses['general']['description']['captions'][0]['text']

def getFaceDescription(responses):
    if 'general' in responses:
        if 'faces' in responses['general'] and responses['general']['faces']:
            faces = responses['general']['faces']
            ages = set(face['age'] for face in faces)
            no_of_men = len([face for face in faces if face['gender'] == 'Male'])
            no_of_women = len([face for face in faces if face['gender'] == 'Female'])

            return '%d men, and %d women. Ages from %d to %d'%(no_of_men, no_of_women, min(ages), max(ages))

describers = [getCaption, getFaceDescription]

def getDescription(responses):
    results = []
    failed = []
    for describer in describers:
        try:
            description = describer(responses)
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
