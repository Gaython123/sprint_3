class Time:
    def __init__(self, hours:int, minutes: int):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return f"Time - {self.hours}:{self.minutes}"

    def display(self):
        print(f"Time - {self.hours}:{self.minutes}")

    def minutes_remaining(self):
        print(f"{60*24 - self.hours * 60 - self.minutes} minutes till day ends ")

new_time = Time(12, 30)
new_time.minutes_remaining()