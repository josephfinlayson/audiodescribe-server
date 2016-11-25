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
    return 'it contains ' + str(faceObject['numberOfMen']) + ' men, and ' + str(faceObject['numberOfWomen']) + ' women. The ages range from ' + str(faceObject['ageMin']) + ' to ' + str(faceObject['ageMax'])

def getFaceDescription(faceList):
    return getFaceString(getFaceObject(faceList))

def getDescription(responses):
    results = []
    if 'general' in responses:
        results.append(getFaceDescription(responses['general']['faces']))

    if not results:
        description = "Sorry, didn't see anything"
    else:
        description = ".\n".join(results)

    return {"description": description, "debug": responses}
