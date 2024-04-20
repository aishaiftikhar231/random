# import csv

# with open("weather-data.csv") as datafile:
#
#     data=csv.reader(datafile)
#     temperature=[]
#     for row in data:
#         if row[1]!="temp":
#             temperature.append(row[1])
#     print(temperature)
import pandas
# data=pandas.read_csv("weather-data.csv")
# # new_tem=data["temp"].to_list()
# #
# # print(data[data.day=="Sunday"])
# monday=data[data.day=="Monday"]
# tem=monday.temp
# nt=tem*9/5
# print(nt)


import pandas
data=pandas.read_csv("C:\Users\Ahmed\Downloads\2018_Central_Park_Squirrel_Census_-_Squirrel_Data")
fur_color=data["Primary Fur Color"]=="Gray"


