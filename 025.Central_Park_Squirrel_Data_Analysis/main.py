import pandas
data = pandas.read_csv(r"Programming-in-Python\025.Central_Park_Squirrel_Data_Analysis\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250120.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "color" : ["Gray", "Cinnamon", "Black"],
    "count" : [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")