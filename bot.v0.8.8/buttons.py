from enum import Enum

class MainMenuButtons(str, Enum):
    MAIN_MENU = "Головне меню",
    SCHEDULE_TODAY = "Розклад на сьогодні 📋",
    SCHEDULE_TOMORROW = "Розклад на завтра 📋",
    CHANGES_TODAY = "Зміни на сьогодні ⚠️",
    CHANGES_TOMORROW = "Зміни на наступний день ⚠️",
    FIND_BY_TEACHER = "Пошук по викладачу 👩🏼‍🏫",
    FIND_BY_GROUP = "Пошук по групі 🔎",
    FIND_BY_DAY = "Пошук по дню тижня 📅",
    ADDITIONAL_FUNCTIONS = "Дод. функції ☕️",
    HELP = "Допомога 🏥"

class FindByDayButtons(str, Enum):
    MONDAY = "Понеділок",
    TUESDAY = "Вівторок",
    WEDNESDAY = "Середа",
    THURSDAY = "Четвер",
    FRIDAY = "П'ятниця"

class Register(str, Enum):
    STUDENT = "Я студент",
    TEACHER = "Я викладач"

class AdditionalFuncButtons(str, Enum):
    RINGS_SCHEDULE = "Розклад дзвінків⌛️",
    EDU_PROCESS = "Графік НП",
    COLLEGE_MAP = "Мапа коледжу",
    WORK_SATURDAYS = "Робочі суботи",
    CHANGE_DATA = "Змінити реєстраційні дані"

class CollegeFloors(str, Enum):
    FIRST_FLOOR = "I",
    SECOND_FLOOR = "II",
    THIRD_FLOOR = "III"