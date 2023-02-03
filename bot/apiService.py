import requests
import json
import datetime
baseLink = 'http://ppfc.eu-central-1.elasticbeanstalk.com/api'
def authenticate():
    url = baseLink + '/authenticate'
    myobj = {
	"username": "bot",
	"password":"Qwerty1234"
    }
    x = requests.post(url, json = myobj)
    auth = json.loads(x.text)
    accToken = auth["accessToken"]
    print(accToken)
    headers = {'Authorization': "Bearer {}".format(accToken)}

    return headers

def checkUser(userID, headers):
    url = baseLink + "/user/{}".format(userID)
    x = requests.get(url, headers = headers)
    if x.status_code == 200:
        return True
    return False


def register(ParamString, headers, userID):

    url = baseLink + "/user"
    userData = ParamString

    if checkUser(userID, headers):
        x = requests.put(url, headers = headers, json = userData)
    else: 
        x = requests.post(url, headers = headers, json = userData)

def disciplinesApi(headers):
    url = baseLink + '/discipline'
    x = requests.get(url, headers = headers)
    disciplinesDict = x.text
    
    return disciplinesDict

def coursesApi(headers):
    url = baseLink + '/course'
    x = requests.get(url, headers = headers)
    coursesDict = x.text
    
    return coursesDict

def groupByCourse(headers, par):
    url = baseLink + '/group?courseId='+ str(par)
    x = requests.get(url, headers = headers)
    groupsFromCourseDict = x.text
    return groupsFromCourseDict
    
def teacherByDiscipline(headers, par):
    url = baseLink + '/teacher?disciplineName='+ par
    x = requests.get(url, headers = headers)
    teachersFromDisciplineDict = x.text
    return teachersFromDisciplineDict
    
def getUserById(userId, headers):
    if checkUser(userId, headers):
        url = baseLink + "/user/{}".format(userId)
        x = requests.get(url, headers = headers)
        userData = x.text
    return userData

def getTeacherIdForUse(headers, par):
    url = baseLink + '/teacher?teacherFullName='+ par
    x = requests.get(url, headers = headers)
    teacher = x.text
    
    return teacher

def getGroupIdForUse(headers, par):
    url = baseLink + '/group?groupNumber='+ par
    x = requests.get(url, headers = headers)
    group = x.text

    return group

def getScheduleByGroup(headers, par):
    url = baseLink + '/schedule?groupId='+ str(par)
    x = requests.get(url, headers = headers)
    scheduleGroup = json.loads(x.text)
    sorted_data = sorted(scheduleGroup, key=lambda x: (x['dayNumber'], x['lessonNumber']))

    schedule = json.dumps(sorted_data)
    return schedule

def getScheduleByTeacher(headers, par):
    url = baseLink + '/schedule?teacherId='+ str(par)
    x = requests.get(url, headers = headers)
    scheduleTeacher = json.loads(x.text)
    sorted_data = sorted(scheduleTeacher, key=lambda x: (x['dayNumber'], x['lessonNumber']))

    schedule = json.dumps(sorted_data)
    return schedule

def getChangesForRegUser(headers, date, userData):
    url = baseLink + '/change?date='+ str(date) +str(userData)
    x = requests.get(url, headers = headers)
    changeForGroup = json.loads(x.text)
    sorted_data = sorted(changeForGroup, key=lambda x: x['lessonNumber'])

    change = json.dumps(sorted_data)
    return change

def getScheduleForRegUser(headers, date, userData):
    url = baseLink + '/schedule?dayNumber='+ str(date) + str(userData)
    x = requests.get(url, headers = headers)
    changeForGroup = json.loads(x.text)
    sorted_data = sorted(changeForGroup, key=lambda x: x['lessonNumber'])

    change = json.dumps(sorted_data)
    return change