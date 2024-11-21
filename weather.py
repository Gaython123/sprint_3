import csv
from matplotlib import pyplot as plt

with open('weather.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    #for row in csv_file:
    #    print(row)


    #row = next(csv_reader)
    #print(row['Data.Temperature.Avg Temp'].split(';'))

class Weather:
    def __init__(self, station_city: str, station_code: str, date: int,  temp_avg: float, temp_max: float,
                 temp_min: float, wind_dir: float, wind_speed: float):

        self.station_city = station_city
        self.station_code = station_code
        self.date = date
        self.temp_avg = temp_avg
        self.temp_max = temp_max
        self.temp_min = temp_min
        self.wind_dir = wind_dir
        self.wind_speed = wind_speed

    def __str__(self):
        return (f"{self.station_city}, [{self.station_code}] in year {self.year}, "
                f"had this statistics:\n"
                f"Average temperature - {self.temp_avg}; "
                f"Max temp - {self.temp_max}; "
                f"Min Temp - {self.temp_min}; "
                f"Wind direction - {self.wind_dir}; "
                f"Wind speed - {self.wind_speed}; ")



