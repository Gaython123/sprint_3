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

    def find_by_day(self):
        for values in plans:
            if Day in plans:
                plans[Planner] = Day
                print(f"for {Day} you have {Planner}")

class Planner:
    def __init__(self, task: str):
        self.task = task

    def __str__(self):
        return f"{self.task}"

    def display(self):
        print(f"The plan is '{self.task}'")

    def add_a_day(Planner, Day):
        new_plan = Planner
        new_day = Day
        plans[new_plan] = [new_day]
        print(f"You have planned '{new_plan}' to day '{new_day}'")


    def change_plan(self):

        old_plan = Planner
        old_date = Day
        plans = {old_plan: old_date}

        #for old_date in plans:
        new_plan = Planner(input("Enter new plan"))
        old_plan = new_plan
        print(plans)

            #plans = {new_plan.__str__() : old_date}


wash_mother = Planner("wash penis")
first_plan = Day(12,9,2025)

wash_mother.add_a_day(first_plan)
wash_mother.change_plan()
wash_mother.change_plan()





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











