import csv
import pandas

# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()

# print(data)

with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
            print(row)

print()


data = pandas.read_csv("weather_data.csv")
print(data)

data_dict = data.to_dict()
data_list = data["temp"].to_list()
print(data_dict)
print(data_list)
# sum=0
# for data in data_list:
#     sum +=data
# print(sum/len(data_list))
#
# print(sum(data_list)/len(data_list))

data['temp'].mean()

print(data.temp.max())

print(data['condition'])
print(data.condition)


print(data[data.day == 'Monday'])
print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
print(monday.condition)

data =  pandas.read_csv('squirrels.csv')
grey_squirrels = len(data[data['Primary Fur Color'] == 'Gray'])
black_squirrels = len(data[data['Primary Fur Color'] == 'Black'])
red_squirrels = len(data[data['Primary Fur Color'] == 'Cinnamon'])

print(grey_squirrels)
print(red_squirrels)
print(black_squirrels)

rat_data = {
    "Fur Color": ['Gray', 'Cinnamon', 'Black'],
    'Count': [grey_squirrels, red_squirrels, black_squirrels]
}

df=pandas.DataFrame(rat_data)
df.to_csv("rat.csv")


