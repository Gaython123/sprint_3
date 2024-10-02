import datetime

plans = {}
class Day:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"

    def display(self):
        print(f"Date is day: {self.day}/{self.month}/{self.year}")

#поняття оної відповідальності / single responsibility
    def days_to_end_of_month(self):
        if self.month == 2 and self.year % 4 == 0 or self.year % 100 == 0 and self.year % 400 == 0:
            if self.day != 29:
                return 29 - self.day
            else:
                return 0

        elif self.month == 2:
            if self.day != 28:
                return 28 - self.day
            else:
                return 0

        elif self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7 or self.month == 8 or self.month == 10 or self.month == 12:
            if self.day != 31:
                return 31 - self.day
            else:
                return 0
                
        else:
            if self.day != 30:
                return 30 - self.day
            else:
                return 0
    def print_days_to_the_end_of_month(self):
        print(f"Days to the end of month : {self.days_to_end_of_month()}")

class Task:
    def __init__(self, task: str, action):
        self.task = task
        self.action = action

    def __str__(self):
        return f"{self.task}"

    def do_action(self, action):
        return self.action()

class Planner:
    def __init__(self):
        self.plans = {}
#Тут я працюю з класами тому прописую все в класы)

    def __str__(self):
        return f"{self.plans}"

    def display(self):
        print(f"The plan is '{self.plans}'")

    def add_task(self, task: Task, day: Day):
        self.plans[task] = day
    #def calculate_/ add_/ - return
    #view_/ show_/ = print

    def view_plan(self):
        for task in self.plans:
            print(f"{task} : {self.plans[task]} description: {task.action()}")

    #def view_planner

planner = Planner()
#lambda - скорочена верся функції якв прописуэться у один рядок
#у лямбді ретурн не пишем. Ретурн є неявний


task = Task("Play Games", lambda: "We are playing games!")
day = Day(1, 12, 2024)
planner.add_task(task, day)
#planner.view_plan()

new_task = Task("Have breakfast", lambda: "Bon apettito")
new_day = Day(12,12,12)
planner.add_task(new_task, new_day)
planner.view_plan()
#Коли мми пишемо () ми хочемо викликати функцію а коли хочемо передати -
# РЕТУРН то без дужок






def new_plan_creating():
    new_plan = Planner
    new_plan = input("Create a new plan")

    day = int(input("Choose 'day'"))
    month = int(input("Choose 'month'"))
    year = int(input("Choose 'Year'"))

    date = Day
    date = datetime.date(year, month, day)
    today = Day
    today = datetime.date.today()

    if date < today:
        print(f"You cannot add a '{new_plan}' to past time")

    else:
        print(f"You have successfully added '{new_plan}' on date '{date}' to your planner")
        plans[new_plan] = date
        print(plans)

#new_plan_creating()











