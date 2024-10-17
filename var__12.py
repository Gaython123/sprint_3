class Time:
    def __init__(self, minutes: int, seconds: int):
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"time is {self.minutes} minutes {self.seconds} seconds"

    def display_time(self):
        print(f"Time is '{self.minutes} min. {self.seconds} sec.'")

    def time_in_seconds(self):
        return f"{self.minutes * 60 + self.seconds} second"


time_1 = Time(2, 4)
time_1.display_time()
print(time_1.time_in_seconds())