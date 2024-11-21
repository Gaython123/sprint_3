import csv
from datetime import datetime
from matplotlib import pyplot as plt

    #for row in csv_file:
    #    print(row)
    #row = next(csv_reader)
    #print(row['Data.Temperature.Avg Temp'].split(';'))

class City:
    def __init__(self, station_city: str, station_code: str):
        self.station_city = station_city
        self.station_code = station_code
        self.date = []
        self.temp_avg = []
        self.temp_max = []
        self.temp_min = []
        self.wind_dir = []
        self.wind_speed = []

    def __str__(self):
        return (f"{self.station_city}, [{self.station_code}]  "
                f"had this statistics:\n"
                f"Average temperature - {self.temp_avg}; "
                f"Max temp - {self.temp_max}; "
                f"Min Temp - {self.temp_min}; "
                f"Wind direction - {self.wind_dir}; "
                f"Wind speed - {self.wind_speed}; ")

    def get_data(self, column, year, month):
        self.data = []
        with open('weather.csv', mode ='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                #'Station.City мусимо вказувати як у csv file дослівно'
                if row['Station.City'] == self.station_city:
                    row_date = datetime.strptime(row['Date.Full'], '%d %m %Y')
                    if row_date.year == year and row_date.month == month:
                        self.data.append(row[column])

        return self.data


city_one = City('Birmingham', 'BHM')
print(city_one.get_data('Data.Temperature.Avg Temp', '2016', '12'))




