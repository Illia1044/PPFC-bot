#-----------------------------------------
#-  Copyright (c) 2023. Lazovikov Illia  -
#-----------------------------------------

import json
from courses import Course

class Group:
    def __init__(self, jsonDict):
        self.id = jsonDict["id"]
        self.number = jsonDict["number"]
        self.course = Course(jsonDict["course"])

# deserialization from json
def groupsList(jsonStr):
    groupsDictList = json.loads(jsonStr)
    buttonsList = []
    for groupDict in groupsDictList:
        group = Group(groupDict)
        buttonsList.append(str(group.number))
    return buttonsList

def groupsIds(jsonStr):
    groupsDictList = json.loads(jsonStr)
    groupsId = []
    for groupDict in groupsDictList:
        group = Group(groupDict)
        groupsId.append(str(group.id))
    return groupsId

def extractGroupId(jsonStr):
    groupDict = json.loads(jsonStr)
    groupId = ""
    group = Group(groupDict)
    groupId = group.id
    return groupId

def extractGroupNumber(jsonStr):
    groupDict = json.loads(jsonStr)
    groupNumber = groupDict["number"]
    return groupNumber