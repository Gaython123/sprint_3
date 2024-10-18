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
            return round(avg_speed, 2)

    def speed_difference(self, new_run):
        delta_speed = self.speed_avg() - new_run.speed_avg()
        return delta_speed

class Leaderboard:
    def __init__(self):
        self.sportsmen = []

    def __str__(self):
        return f"{self.sportsmen}"

    def add_sportsman(self, run:Run):
        if run in self.sportsmen:
            return

        self.sportsmen.append(run)

    def best_runner(self, n:int):
        for i in range(len(self.sportsmen)):
            for j in range(len(self.sportsmen)):
                if self.sportsmen[i].speed_avg() > self.sportsmen[j].speed_avg():
                    self.sportsmen[i], self.sportsmen[j] = self.sportsmen[j], self.sportsmen[i]

        best_runners = []
        for run in self.sportsmen[:n]:
            best_runners.append(f"{run.runner_surname} : {run.speed_avg()}")
            #якщо ми напишемо ретурн з табуляцією то він поверне тільки 1 спортсмена
            # (тобто лише один раз виконає цикл) а якщо без табуляції то допоки
            # не пройде всю дистанцію (тобто 'n')
        return best_runners


Nazar_2004 = Run(3, 20, "Prots", 800)
Ivan_2007 = Run(4, 40, "mykolenko",1000)
Olena_2006 = Run(5, 40, "mykolencik",1000)
Alex_2003 = Run(4, 20, "mykolenkavsky",1000)

runner_list = Leaderboard()

runner_list.add_sportsman(Ivan_2007)
runner_list.add_sportsman(Nazar_2004)
runner_list.add_sportsman(Olena_2006)
runner_list.add_sportsman(Alex_2003)

print(runner_list.best_runner(3))








