import csv
from datetime import datetime
from matplotlib import pyplot as plt
import pandas as pd

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

    def get_data_whole_period(self, column):
        self.data = []
        with open('weather.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                # 'Station.City мусимо вказувати як у csv file дослівно'
                if row['Station.City'] == self.station_city:
                    row_date = datetime.strptime(row['Date.Full'], '%Y-%m-%d')
                    self.data.append(row[column])
                    self.data = [*map(float, self.data)]  # map - це розпакоУка елементів та надання їм типу даних
                    # це тіпа recursion чи шо я єбу
        return self.data

    def get_all_time_date(self):
        self.date = []
        with open('weather.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                # 'Station.City мусимо вказувати як у csv file дослівно'
                if row['Station.City'] == self.station_city:
                    row_date = datetime.strptime(row['Date.Full'], '%Y-%m-%d')
                    self.date.append(row['Date.Full'])

        return self.date

    def create_plot_show(self, column: str, year: int, month: int, color_line_marker: str, linewidth_value: float, label_legend):
        """
        :param column: column to take data from
        :param year: range for data
        :param month: range for data
        :param color_line_marker: stands for 'color', 'line' and 'marker' styles
        :param linewidth_value: the width of line
        :param label_legend: legend
        :return: creates and returns a graph
        """
        date_values_x = self.get_date(year, month)
        statistics_values_y = self.get_data_from_column(column, year, month)

        plt.plot(date_values_x, statistics_values_y, color_line_marker, linewidth = linewidth_value, label = label_legend)
        plt.grid(True)
        plt.xlabel('Date')
        plt.ylabel(column)
        plt.title(f'{column} in {self.station_city}, ({self.station_code}) for {year}/{month}')
        plt.legend()
        plt.show()

    def plot_max_temperature(self, year: int, month: int, color_line_marker: str, linewidth_value: float, label_legend):
        """
        :param year: range for data
        :param month: range for data
        :param color_line_marker: stands for 'color', 'line' and 'marker' styles
        :param linewidth_value: the width of line
        :param label_legend: legend
        :return: creates and returns a graph
        """
        date_values_x = self.get_date(year, month)
        statistics_values_y = self.get_data_from_column('Data.Temperature.Max Temp', year, month)

        plt.plot(date_values_x, statistics_values_y, color_line_marker, linewidth = linewidth_value, label = label_legend)
        plt.grid(True)
        plt.xlabel('Date')
        plt.ylabel('Highest Temperature (°F)')
        plt.title(f' The highest temperature in {self.station_city}, ({self.station_code}) for {year}/{month}')
        plt.legend()
        plt.show()

    def plot_min_temperature(self, year: int, month: int, color_line_marker: str, linewidth_value: float, label_legend):
        """
        :param year: range for data
        :param month: range for data
        :param color_line_marker: stands for 'color', 'line' and 'marker' styles
        :param linewidth_value: the width of line
        :param label_legend: legend
        :return: creates and returns a graph
        """
        date_values_x = self.get_date(year, month)
        statistics_values_y = self.get_data_from_column('Data.Temperature.Min Temp', year, month)

        plt.plot(date_values_x, statistics_values_y, color_line_marker, linewidth = linewidth_value, label = label_legend)
        plt.grid(True)
        plt.xlabel('Date')
        plt.ylabel('Lowest Temperature (°F)')
        plt.title(f' The lowest temperature in {self.station_city}, ({self.station_code}) for {year}/{month}')
        plt.legend()
        plt.show()

    def plot_avg_temperature(self, year: int, month: int, color_line_marker: str, linewidth_value: float, label_legend):
        """
        :param year: range for data
        :param month: range for data
        :param color_line_marker: stands for 'color', 'line' and 'marker' styles
        :param linewidth_value: the width of line
        :param label_legend: legend
        :return: creates and returns a graph
        """
        date_values_x = self.get_date(year, month)
        statistics_values_y = self.get_data_from_column('Data.Temperature.Avg Temp', year, month)

        plt.plot(date_values_x, statistics_values_y, color_line_marker, linewidth = linewidth_value, label = label_legend)
        plt.grid(True)
        plt.xlabel('Date')
        plt.ylabel('Average Temperature (°F)')
        plt.title(f' Average temperature in {self.station_city}, ({self.station_code}) for {year}/{month}')
        plt.legend()
        plt.show()

    def plot_wind_direction(self, year: int, month: int, color_line_marker: str, linewidth_value: float, label_legend):
        """
        :param year: range for data
        :param month: range for data
        :param color_line_marker: stands for 'color', 'line' and 'marker' styles
        :param linewidth_value: the width of line
        :param label_legend: legend
        :return: creates and returns a graph
        """
        date_values_x = self.get_date(year, month)
        statistics_values_y = self.get_data_from_column('Data.Wind.Direction', year, month)

        plt.plot(date_values_x, statistics_values_y, color_line_marker, linewidth = linewidth_value, label = label_legend)
        plt.grid(True)
        plt.xlabel('Date')
        plt.ylabel('Wind Direction')
        plt.title(f' Wind Direction in {self.station_city}, ({self.station_code}) for {year}/{month}')
        plt.legend()
        plt.show()

    def plot_wind_speed(self, year: int, month: int, color_line_marker: str, linewidth_value: float, label_legend):
        """
        :param year: range for data
        :param month: range for data
        :param color_line_marker: stands for 'color', 'line' and 'marker' styles
        :param linewidth_value: the width of line
        :param label_legend: legend
        :return: creates and returns a graph
        """
        date_values_x = self.get_date(year, month)
        statistics_values_y = self.get_data_from_column('Data.Wind.Speed', year, month)

        plt.plot(date_values_x, statistics_values_y, color_line_marker, linewidth = linewidth_value, label = label_legend)
        plt.grid(True)
        plt.xlabel('Date')
        plt.ylabel('Wind Speed (m/s)')
        plt.title(f'Wind Speed (m/s) in {self.station_city}, ({self.station_code}) for {year}/{month}')
        plt.legend()
        plt.show()

    def compare_temperatures(self, year: int, month: int):
        """
        :param year: year of data needed
        :param month: month of data needed
        :return: The highest, lowest and average temperatures during certain period
        """
        y_avg_values = self.get_data_from_column('Data.Temperature.Avg Temp', year, month)
        y_min_values = self.get_data_from_column('Data.Temperature.Min Temp', year, month)
        y_max_values = self.get_data_from_column('Data.Temperature.Max Temp', year, month)
        x_values = self.get_date(year, month)

        plt.plot(x_values, y_min_values, label = 'MIN Temperatures', color = 'r', marker = '.', linestyle = '-')
        plt.plot(x_values, y_max_values, label='MAX Temperatures', color='g', marker = '.', linestyle = '--')
        plt.plot(x_values, y_avg_values, label='AVG Temperatures', color='b', marker = '.', linestyle = ':')

        plt.title(f"MAX, MIN and AVG Temperatures for {self.station_city}, {year}/{month}")
        plt.xlabel('Date')
        plt.ylabel('Temperature (°F)')
        plt.legend()
        plt.grid(True)
        plt.show()

    def compare_temperatures_all_time(self):
        """
        :return: The highest, lowest and average temperatures for the whole time
        """
        plt.style.use('ggplot')
        y_avg_values = self.get_data_whole_period('Data.Temperature.Avg Temp')
        y_min_values = self.get_data_whole_period('Data.Temperature.Min Temp')
        y_max_values = self.get_data_whole_period('Data.Temperature.Max Temp')
        x_values = self.get_all_time_date()

        plt.plot(x_values, y_min_values, label = 'MIN Temperatures', color = 'r', marker = '', linestyle = '-', linewidth = 1.5)
        plt.plot(x_values, y_max_values, label='MAX Temperatures', color='g', marker = '', linestyle = '-', linewidth = 1.5)
        plt.plot(x_values, y_avg_values, label='AVG Temperatures', color='b', marker = '', linestyle = '-', linewidth = 0.5)

        plt.title(f"MAX, MIN and AVG Temperatures for {self.station_city}", fontsize = 16, color = '#013220')
        plt.xlabel('Date', color = '#C76E00')
        plt.ylabel('Temperature (°F)', fontsize = 14, color = '#191970')

        plt.legend()
        #plt.grid(True)
        plt.xticks(fontsize=10, color = '#C76E00')
        plt.gca().xaxis.set_major_locator(plt.MaxNLocator(5))
        plt.ylim(min(y_min_values) - 5, max(y_max_values) + 5)

        plt.show()

    def bar_avg_temperature(self, year: int, month: int):
        """
        :param year: range for data
        :param month: range for data
        :return: creates and returns a graph
        """
        date_values_x = self.get_date(year, month)
        statistics_values_y = self.get_data_from_column('Data.Temperature.Avg Temp', year, month)

        plt.bar(date_values_x, statistics_values_y, width = 0.25)
        plt.grid(False)
        plt.xlabel('Date')
        plt.ylabel('Average Temperature (°F)')
        plt.title(f' Average temperature in {self.station_city}, ({self.station_code}) for {year}/{month}')
        plt.legend()
        plt.show()

    def bar_compare_temperatures_all_time(self):
        x_values = self.get_all_time_date()
        y_avg_values = self.get_data_whole_period('Data.Temperature.Avg Temp')
        y_min_values = self.get_data_whole_period('Data.Temperature.Min Temp')
        y_max_values = self.get_data_whole_period('Data.Temperature.Max Temp')

        plt.bar(x_values, y_max_values, color = 'g', width = 0.3, label = 'Max temperature')
        plt.bar(x_values, y_avg_values, color = 'b', width = 0.4, label = 'Average temperature')
        plt.bar(x_values, y_min_values, color = 'r', width = 0.5, label =  'Min temperature')

        plt.xlabel('Date', fontsize = 10)
        plt.ylabel('Temperature in F')
        plt.title(f'Min, Avg and Max temperature in {self.station_city} (#{self.station_code}) for the whole time')
        plt.grid(False)
        plt.legend()
        plt.gca().xaxis.set_major_locator(plt.MaxNLocator(6))

        plt.show()

    def wind_speed_bar(self):
        x_values = self.get_all_time_date()
        y_values = self.get_data_whole_period('Data.Wind.Speed')

        plt.bar(x_values, y_values, color = 'c')
        plt.title(f'Histogram for Wind speed, {self.station_city} #{self.station_code}', fontsize = 25)
        plt.xlabel('Date', fontsize = 20)
        plt.ylabel('Wind speed', fontsize = 20)

        plt.gca().xaxis.set_major_locator(plt.MaxNLocator(11))
        plt.xticks(rotation=40)
        plt.show()

    def histogram_wind_speed(self):
        y_values = self.get_data_whole_period('Data.Wind.Speed')
        x_bins = [1,2,3,4,5,6,7,8,9,10,11,12,13,14] #bins - це корзини на які розподіляються вибрані величини для порівняння)

        counts, bins, _ = plt.hist(y_values, bins = x_bins, color = 'cyan',edgecolor = 'grey')

        plt.title(f'Histogram of Wind speed for {self.station_city} #{self.station_code}')
        plt.xlabel('Wind speed (m/s)')
        plt.ylabel('Numbers of speed measured')

        max_count = max(counts)
        # Знаходимо індекси всіх кошиків, які мають найбільше значення
        max_count_indices = [i for i, count in enumerate(counts) if count == max_count]
        # Додаємо мітки для кожного з найбільш поширених діапазонів швидкості вітру
        for i, index in enumerate(max_count_indices):
            most_common_range = (f'{bins[index]}-{bins[index + 1]}')
            plt.annotate(f'Most common: {most_common_range} m/s', xy=((bins[index] + bins[index + 1]) / 2, max_count),
                         xytext=((bins[index] + bins[index + 1]) / 2, max_count + (i + 1) * 0.5),
                         arrowprops=dict(facecolor='navy', shrink=0.05), ha='center', fontsize=10, color='navy')
        plt.show()

    def precipitation_level_bar(self, year, month):
        y_values = self.get_data_from_column('Data.Precipitation', year, month)
        x_values = self.get_date(year, month)

        colors =['#1E90FF' if value > 10 else '#1034A6' for value in y_values]
        plt.bar(x_values, y_values, color = colors)
        for i in y_values:
            if i >10:
                plt.axhline(y=10, color = 'red')
                plt.legend(['10mm of precipitation',' Precipitation < 10 mm'], loc = 'upper right')

        plt.xlabel('Data')
        plt.ylabel('Precipitation level')
        plt.title(f'Precipitation level in {self.station_city}/#{self.station_code} for {month}/{year}')
        plt.xticks(rotation=45)
        plt.show()