import csv
from datetime import datetime
from matplotlib import pyplot as plt

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
        y_avg_values = self.get_data_from_column('Data.Temperature.Avg Temp', year, month)
        y_min_values = self.get_data_from_column('Data.Temperature.Min Temp', year, month)
        y_max_values = self.get_data_from_column('Data.Temperature.Max Temp', year, month)
        x_values = self.get_date(year, month)

        plt.plot(x_values, y_min_values, label = 'MIN Temperatures', color = 'r')
        plt.plot(x_values, y_max_values, label='MAX Temperatures', color='g')
        plt.plot(x_values, y_avg_values, label='MIN Temperatures', color='b')
        plt.show()

city_one = City('Birmingham', 'BHM')
city_one.compare_temperatures(2016, 12)

