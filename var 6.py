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

    # >= greater equal
    def __ge__(self, other) -> bool:
        if self.year > other.year:
            return True
        elif self.year < other.year:
            return False
        else:
            if self.month > other.month:
                return True
            elif self.month < other.month:
                return False
            else:
                if self.day >= other.day:
                    return True
                else:
                    return False


    # > greater
    def __gt__(self, other) -> bool:
        if self.year > other.year:
            return True

        elif self.year < other.year:
            return False

        else:
            if self.month > other.month:
                return True

            elif self.month < other.month:
                return False
            else:
                if self.day > other.day:
                    return True
                else:
                    return False

    # <= less equel
    def __le__(self, other) -> bool:
        pass
    # < less
    def __lt__(self, other) -> bool:
        if self.year < other.year:
            return True

        elif self.year > other.year:
            return False

        else:
            if self.month < other.month:
                return True

            elif self.month > other.month:
                return False
            else:
                if self.day < other.day:
                    return True
                else:
                    return False



    # ==
    # a == b
    # a = self; b = other
    def __eq__(self, other):
        return self.year == other.year and self.month == other.month and self.day == other.day
               #[                               БЛОК                                                ]

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

    def sort(self, comparator):
        sorted_plans = {}
#comparator (a, b) => True/False
        for task1 in self.plans:
            task = task1
            for task2 in self.plans:
                if task in sorted_plans:
                    continue

                if comparator(self.plans[task1], self.plans[task2]):
                    task = task2
            sorted_plans[task] = self.plans[task]
        pl = Planner()
        pl.plans = sorted_plans
        return pl


task1 = Task("Play Games 1", lambda: "We are playing games!")
task2 = Task("Play Games 2", lambda: "We are playing games!")
task3 = Task("Play Games 3", lambda: "We are playing games!")
task4 = Task("Play Games 4", lambda: "We are playing games!")
task5 = Task("Play Games 5", lambda: "We are playing games!")


day1 = Day(2, 10, 2024)
day2 = Day(1, 10, 2024)
day3 = Day(2, 7, 2023)
day4 = Day(2, 3, 2025)
day5 = Day(2, 11, 2004)

planner = Planner()
planner.add_task(task1, day1)
planner.add_task(task2, day2)
planner.add_task(task3, day3)
planner.add_task(task4, day4)
planner.add_task(task5, day5)

planner_days = [day1, day2, day3, day4, day5]
def days_sort(days, comparator):
    for i in range(len(days)):
        for j in range(len(days)):
            if comparator(days[i], days[j]):
                days[i], days[j] = days[j], days[i]

days_sort(planner_days, lambda a, b: a < b)
for day in planner_days:
    print(day)



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



print(day1>=day2)
print(day1>day2)
#print(day1 == day2)

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











