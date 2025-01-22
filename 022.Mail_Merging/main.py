PLACEHOLDER = "[Name]"

with open(r"Programming-in-Python\022.Mail_Merging\Input\Names\invited_names.txt") as names_file:
    names = names_file.readlines()

with open(r"Programming-in-Python\022.Mail_Merging\Input\Letters\starting_letter.docx") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        
        with open(fr"Programming-in-Python\022.Mail_Merging\Output\ReadyToSend\letter_for_{stripped_name}", mode="w") as completed_letter:
            completed_letter.write(new_letter)