import csv
from datetime import datetime
from types import new_class

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

    #def get_data(self, column, year, month):
    #    self.data = []
    #    self.date = []
    #    with open('weather.csv', mode ='r') as csv_file:
    #        csv_reader = csv.DictReader(csv_file)
    #        for row in csv_reader:
    #            #'Station.City мусимо вказувати як у csv file дослівно'
    #            if row['Station.City'] == self.station_city:
    #                row_date = datetime.strptime(row['Date.Full'], '%Y-%m-%d')
    #                if row_date.year == year and row_date.month == month:
    #                    self.data.append(row[column])
    #                    self.data = [*map(float, self.data)] #map - це розпакоУка елементів та надання їм типу даних
    #                    #це тіпа recursion чи шо я єбу
#
#
    #                    new_city = City('Birmingham', 'BMH')
    #                    self.date.append(new_city.get_data('Date.Full', year, month))
#
    #        plt.plot(self.date, self.data)
    #        plt.show()
#
    #    return self.data

    def get_data_from_column(self, column, year, month):
        self.data = []
        with open('weather.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                # 'Station.City мусимо вказувати як у csv file дослівно'
                if row['Station.City'] == self.station_city:
                    row_date = datetime.strptime(row['Date.Full'], '%Y-%m-%d')
                    if row_date.year == year and row_date.month == month:
                        self.data.append(row[column])
                        self.data = [*map(float, self.data)]  # map - це розпакоУка елементів та надання їм типу даних
                        # це тіпа recursion чи шо я єбу
        return self.data

    def get_date(self, year, month):
        self.date = []
        with open('weather.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                # 'Station.City мусимо вказувати як у csv file дослівно'
                if row['Station.City'] == self.station_city:
                    row_date = datetime.strptime(row['Date.Full'], '%Y-%m-%d')
                    if row_date.year == year and row_date.month == month:
                        self.date.append(row['Date.Full'])

        return self.date

    def create_plot(self, column, year, month):
        date_values_x = self.get_date(year, month)
        statistics_values_y = self.get_data_from_column(column, year, month)

        plt.plot(date_values_x, statistics_values_y)
        plt.xlabel('Date')
        plt.ylabel(column)
        plt.title(f'{column} in {self.station_city}, #{self.station_code} for {year}/{month}')

        plt.show()

city_one = City('Birmingham', 'BHM')

#city_one.create_plot('Data.Temperature.Avg Temp', 2016, 1)

city_two = City('Dillon', 'DLN')
city_two.create_plot('Data.Wind.Speed', 2016, 4)


