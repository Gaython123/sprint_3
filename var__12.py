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

class Run(Time):
    def __init__(self, minutes: int, seconds: int, runner_surname: str, distance: int):
        super().__init__(minutes, seconds)
        self.runner_surname = runner_surname
        self.distance = distance

    def __str__(self):
        return (f"{self.runner_surname} finished a {self.distance} meters race "
                f"in {self.minutes} minutes, {self.seconds} seconds'")

    def speed_avg(self):
        for distance in self.runner_surname:
            avg_speed = self.distance / (self.minutes * 60 + self.seconds)
            avg_speed *= 3.6
            return avg_speed

    def speed_difference(self, new_run):
        delta_speed = self.speed_avg() - new_run.speed_avg()
        return delta_speed


class Leaderboard:
    def __init__(self):
        self.sportsmen = []

    def add_sportsman(self, run:Run):
        if run.speed_avg() in self.sportsmen:
            return

        else:
            #a_run.runner_surname,#
            self.sportsmen.append(run.speed_avg())

    def best_runner(self):
        for i in range(len(self.sportsmen)):
            for j in range(len(self.sportsmen)):
                if self.sportsmen[i] > self.sportsmen[j]:
                    self.sportsmen[i], self.sportsmen[j] = self.sportsmen[j], self.sportsmen[i]
        return self.sportsmen[0]

Nazar_2004 = Run(3, 20, "Prots", 800)
print(Nazar_2004.speed_avg())

Ivan_2007 = Run(4, 40, "mykolenko",1000)
print(Nazar_2004.speed_difference(Ivan_2007))

runner_list = Leaderboard
runner_list.add_sportsman(Run(4, 4, "jj", 9))
runner_list.add_sportsman(Ivan_2007)

