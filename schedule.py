#-----------------------------------------
#-  Copyright (c) 2023. Lazovikov Illia  -
#-----------------------------------------

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
        self.weekAlternation = jsonDict["weekAlternation"]

class Subject:
    def __init__(self, jsonDict):
        self.id = jsonDict["id"]
        self.name = jsonDict["name"]

class Classroom:
    def __init__(self, jsonDict):
        self.id = jsonDict["id"]
        self.name = jsonDict["name"]

def scheduleCreator(dict, state, userState):
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
        weekAlternation = schedule.weekAlternation

        if dayNumber not in schedules:
            schedules[dayNumber] = {}

        schedules[dayNumber].setdefault(lessonNumber, set()).add((lessonNumber, subject, group, teacher, classroom, weekAlternation))

    scheduleForm = " "
    for dayNumber, scheduleItem in schedules.items():
        if state != 'BOTH':
            dayName = formatNumberToDay(dayNumber) + " " + formatWeekAlternation(state)
        else:
            dayName = formatNumberToDay(dayNumber)

        scheduleForm += dayName + "\n"

        for lessons in scheduleItem.values():
            lessons = list(lessons)
            lessons.sort(reverse=True, key = lambda d: d[5])
            for lesson in lessons:

                ending = " ауд. "
                if str(lesson[4]) == "Зал " or str(lesson[4]) == "зал " :
                    ending = ""
                
                if str(state) == 'BOTH':
                    ending += formatWeekAlternation(str(lesson[5]))

                if str(state) == 'NUMERATOR':
                    if lesson[5] == state:
                        ending += formatWeekAlternation(str(lesson[5]))
                    if lesson[5] == 'DENOMINATOR':
                        continue

                if str(state) == 'DENOMINATOR':
                    if lesson[5] == state:
                        ending += formatWeekAlternation(str(lesson[5]))
                    if lesson[5] == 'NUMERATOR':
                        continue

                ending += "\n"
                if userState == True:
                    scheduleForm += "*" + str(lesson[0]) + "*. "+ str(lesson[1]) + " ➡️ " + str(lesson[3]) +  " ➡️ " + str(lesson[4]) + ending
                else:
                    scheduleForm += "*" + str(lesson[0]) + "*. "+ str(lesson[1]) + " ➡️ " + str(lesson[2]) +  " група ➡️ "  + str(lesson[4]) + ending

    return scheduleForm


def formatNumberToDay(dayNumber):
    if dayNumber == 1:
        dayName = "*Понеділок:*"
    if dayNumber == 2:
        dayName = "\n*Вівторок:*"
    if dayNumber == 3:
        dayName = "\n*Середа:*"
    if dayNumber == 4:
        dayName = "\n*Четвер:*"
    if dayNumber == 5:
        dayName = "\n*П'ятниця:*"
    return dayName

def formatDayToNumber(message):
    dayNumber = ""
    if message.text == "Понеділок":
        dayNumber = 1
    if message.text == "Вівторок":
        dayNumber = 2
    if message.text == "Середа":
        dayNumber = 3
    if message.text == "Четвер":
        dayNumber = 4
    if message.text == "П'ятниця":
        dayNumber = 5
    return dayNumber

def formatWeekAlternation(alterStatus):
    state = ""
    if alterStatus == "NUMERATOR":
        state = "*(Чисельник)* 🔵"
    if alterStatus == 'DENOMINATOR':
        state = "*(Знаменник)* 🟡"
    return state