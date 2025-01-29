from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

def button_clicked():
    print("Clicked.")

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack()
my_label.grid(row=0, column=0)

button = Button(text="Click Me !", command=button_clicked)
# button.pack()
button.grid(row=1, column=1)

new_button = Button(text="Click Me !", command=button_clicked)
# new_button.pack()
new_button.grid(row=0, column=2)

input = Entry(width=10)
# input.pack()
input.grid(row=2, column=3)


window.mainloop()