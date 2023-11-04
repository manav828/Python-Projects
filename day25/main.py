
# import csv
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     # print(data_file)
#
#     for row in data:
#         if row[1] != 'temp':
#             temp.append(int(row[1]))
#     print(temp)


# data = pandas.read_csv('weather_data.csv')
# temp = data['temp']
# # avg = sum(temp)/len(temp )
# # print(avg)
# print(data[data.temp == temp.max()])

import pandas

data = pandas.read_csv('Squirrel_Data.csv')
# print(data)
d2 = data.pivot_table(index=['Primary Fur Color'], aggfunc='size')
print(d2)
d2.to_csv('squirrel_count.csv')