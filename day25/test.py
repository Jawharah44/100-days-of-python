# with open("day25/weather_data.csv") as weather_info:
#     data = weather_info.readlines()

# import csv

# with open("day25/weather_data.csv") as weather_info:
#     data = csv.reader(weather_info)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(row)
#     print(temperatures)

import pandas as pd
data = pd.read_csv("day25/squirrel_data.csv")

grey_squirrels = data[data["Primary Fur Color"] == "Gray" ]
print(grey_squirrels)