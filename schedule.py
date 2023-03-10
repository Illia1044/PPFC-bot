import json
from groups import Group
from teachers import Teacher

class Schedule:
    def __init__(self, jsonDict):
        self.id = jsonDict["id"]
        self.group = Group(jsonDict["group"])
        self.classroom = Classroom(jsonDict["classroom"])
        self.teacher = Teacher(jsonDict["teacher"])
        self.subject = Subject(jsonDict["subject"])
        self.isSubject = jsonDict["isSubject"]
        self.lessonNumber = jsonDict["lessonNumber"]
        self.dayNumber = jsonDict["dayNumber"]
        self.isNumerator = jsonDict["isNumerator"]

class Subject:
    def __init__(self, jsonDict):
        self.id = jsonDict["id"]
        self.name = jsonDict["name"]

class Classroom:
    def __init__(self, jsonDict):
        self.id = jsonDict["id"]
        self.name = jsonDict["name"]

def scheduleCreator(dict, state):
    scheduleDictList = json.loads(dict)
    schedules = {}

    for scheduleDict in scheduleDictList:
        schedule = Schedule(scheduleDict)
        dayNumber = schedule.dayNumber
        subject = schedule.subject.name
        lessonNumber = schedule.lessonNumber
        group = schedule.group.number
        teacher = schedule.teacher.firstName + " " + schedule.teacher.lastName 
        classroom = schedule.classroom.name
        isNumerator = schedule.isNumerator

        if dayNumber not in schedules:
            schedules[dayNumber] = {}

        schedules[dayNumber].setdefault(lessonNumber, set()).add((lessonNumber, subject, group, teacher, classroom, isNumerator))

    scheduleForm = " "
    for dayNumber, scheduleItem in schedules.items():
        if state != None:
            dayName = formatNumberToDay(dayNumber) + " " + formatIsNumerator(state)
        else:
            dayName = formatNumberToDay(dayNumber)

        scheduleForm += dayName + "\n"

        for lessons in scheduleItem.values():
            lessons = list(lessons)
            lessons.sort(reverse=True, key = lambda d: d[5])

            for lesson in lessons:
                if state != None and len(lessons)>1:
                    if lesson[5] != state:
                        continue

                ending = " ??????."
                if str(lesson[4]) == "??????":
                    ending = ""

                if len(lessons) > 1 and state == None:
                    ending += " " + formatIsNumerator(lesson[5])

                ending += "\n"

                scheduleForm += str(lesson[0]) + ". "+ str(lesson[1]) + " ?????? " + str(lesson[2]) + " ?????????? ?????? " + str(lesson[3]) +  " ?????? " + str(lesson[4]) + ending

    return scheduleForm

def formatNumberToDay(dayNumber):
    if dayNumber == 1:
        dayName = "??????????????????:"
    if dayNumber == 2:
        dayName = "\n????????????????:"
    if dayNumber == 3:
        dayName = "\n????????????:"
    if dayNumber == 4:
        dayName = "\n????????????:"
    if dayNumber == 5:
        dayName = "\n??'????????????:"
    return dayName

def formatDayToNumber(message):
    dayNumber = ""
    if message.text == "??????????????????":
        dayNumber = 1
    if message.text == "????????????????":
        dayNumber = 2
    if message.text == "????????????":
        dayNumber = 3
    if message.text == "????????????":
        dayNumber = 4
    if message.text == "??'????????????":
        dayNumber = 5
    return dayNumber

def formatIsNumerator(bool):
    state = ""
    if bool == True:
        state = "(??????????????????) ????"
    if bool == False:
        state = "(??????????????????) ????"
    return state