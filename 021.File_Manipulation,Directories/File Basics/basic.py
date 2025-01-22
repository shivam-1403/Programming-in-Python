# file = open(r"D:\Python Code\Programming-in-Python\021.File_Manipulation,Directories\File Basics\my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# for reading
with open("./my_file.txt") as file:
    contents = file.read()
    print(contents)

# for writing
with open("./my_file.txt", mode="w") as file:
    file.write("New Text.")