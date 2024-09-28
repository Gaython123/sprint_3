from datetime import datetime

class Day:
    def __init__(self, date):
        self.date = date
        #date = datetime.uptime(date, '%d/%m/%Y')

    def display(self):
        print(self.date)

day2 = Day(datetime.today())
day1 = Day("28/09/2024")
day1.display()
day2.display()