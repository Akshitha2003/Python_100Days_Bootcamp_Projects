from tkinter import *

FONT = ("Arial", 15, "normal")


def calculate():
    miles = float(input_value.get())
    answer.config(text=str(round(miles*1.609, 2)))


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=100, height=100)
window.config(padx=50, pady=50)

input_value = Entry(width=10, font=FONT)
input_value.grid(column=1, row=0)

my_label = Label(text="Miles", font=FONT)
my_label.grid(column=2, row=0)

my_label = Label(text="is equal to", font=FONT)
my_label.grid(column=0, row=1)

answer = Label(font=FONT)
answer.grid(column=1, row=1)

my_label = Label(text="Km", font=FONT)
my_label.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate, font=FONT)
button.grid(column=1, row=2)

window.mainloop()
