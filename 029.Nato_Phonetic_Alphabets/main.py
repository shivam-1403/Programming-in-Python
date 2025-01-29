import pandas
nato_data_frame = pandas.read_csv(r"D:\Python Code\Programming-in-Python\029.Nato_Phonetic_Alphabets\nato_phonetic_alphabets.csv")

phonetic_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}

word = input("Enter a word : ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)