from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

def answer():
    final_ans = float(miles_input.get()) * 1.609
    answer_label.config(text=final_ans)

miles_input = Entry()
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

answer_label = Label(text="0")
answer_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

cal_button = Button(text="Calculate", command=answer)
cal_button.grid(row=2, column=1)


window.mainloop()