import pandas

data = pandas.read_csv(r"Programming-in-Python\024.Pandas_Library\weather_data.csv")
# print(data)
# print(data["temp"])  can also be selcted as   print(data.temp)

# data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()

# Finding average of temp
# avg = sum(temp_list)/(len(temp_list))
# print(avg)

#There's a method in pandas to give you average
# print(data["temp"].mean())

# print(data["temp"].max())


#Get data in row
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])


#Get condition of a an item of a row
# monday = data[data.day == "Monday"]
# print(monday.condition)

#Converting monday's temp to Farenheit
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_farenheit = (monday_temp * (9/5)) + 32
# print(monday_temp_farenheit)


#Generating a DataFrame
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_file.csv")