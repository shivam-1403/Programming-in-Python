student_dict = {
    "students" : ["Angela", "James", "Lily"],
    "scores" : [56, 76, 98]
}

import pandas
student_data_frame = pandas.DataFrame(student_dict)

# for (key, value) in student_data_frame.items():
#     print(value)

#iterate over rows:
for(index, row) in student_data_frame.iterrows():
    print(row)