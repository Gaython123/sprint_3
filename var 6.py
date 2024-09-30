import datetime

Days = []
plans = {}
class Day:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"Date is day: {self.day}/{self.month}/{self.year}")

    def add_day(self):
        Days.append(self)

    def days_to_end_of_month(self):
        if self.month == 2 and self.year % 4 == 0 or self.year % 100 == 0 and self.year % 400 == 0:
            if self.day != 29:
                print(f"To the end of month are '{29 - self.day}' days left\n")
            else:
                print("It's the last day of month\n")

        elif self.month == 2:
            if self.day != 28:
                print(f"To the end of month are '{28 - self.day}' days left\n")
            else:
                print("It's the last day of month\n")

        elif self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7 or self.month == 8 or self.month == 10 or self.month == 12:
            if self.day != 31:
                print(f"To the end of month are '{31 - self.day}' days left\n")
            else:
                print("It's the last day of month\n")
                
        else:
            if self.day != 30:
                print(f"To the end of month are '{30 - self.day}' days left\n")
            else:
                print("It's the last day of month\n")

class Planner:
    def __init__(self, task: str):
        self.task = task

    def display(self):
        print(f"The plan is '{self.task}'")

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

new_plan_creating()











