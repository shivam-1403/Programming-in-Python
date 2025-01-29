with open(r"D:\Python Code\Programming-in-Python\027.List_Comprehensions\Practice\Hard_Ques\file1.txt") as file1:
    file_1_data = file1.readlines()
with open(r"D:\Python Code\Programming-in-Python\027.List_Comprehensions\Practice\Hard_Ques\file2.txt") as file2:
    file_2_data = file2.readlines()

result = [int(num) for num in file_1_data if num in file_2_data]
print(result)