import csv
from datetime import datetime

from fontTools.misc.cython import returns
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
                    row_date = datetime.strptime(row['Date.Full'], '%Y-%m-%d')
                    if row_date.year == year and row_date.month == month:
                        self.data.append((row_date, row[column]))


        return self.data

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    return lst


city_one = City('Birmingham', 'BHM')
data = city_one.get_data('Data.Temperature.Avg Temp', 2016, 1)

#x_values = []
#y_values = []
#for item in data:
#    x_value = item[0]
#    y_value = item[1]
#    x_values.append(x_value)
#    y_value.append(x_value)
#    return x_values, y_values


print(data)
#x_values = city_one.get_data('Date.Full', 2016, 1)
#y_values = city_one.get_data('Data.Temperature.Avg Temp', 2016, 1)


#sorted_data = bubble_sort(data)
#x_values = [item[0] for item in sorted_data]
#y_values = [item[1] for item in sorted_data]
x_values = []
y_values = []
i=0
for elem in range(len(data)):
    x_values.append(data[0])
    y_values.append(data[1])
    i +=1


plt.style.use('ggplot')
plt.plot(x_values, y_values)
plt.show()




