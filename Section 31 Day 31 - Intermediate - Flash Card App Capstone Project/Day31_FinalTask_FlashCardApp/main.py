from tkinter import *
import pandas
import random
random_card = {}


def change_word():
    global random_card, timer
    window.after_cancel(timer)
    random_card = random.choice(data_dict)
    card_front_canvas.itemconfig(title_text, text="French", fill="black")
    card_front_canvas.itemconfig(word_text, text=random_card["French"], fill="black")
    card_front_canvas.itemconfig(front_image, image=card_front_image)
    timer = window.after(3 * 1000, give_answer)


def remove_word():
    data_dict.remove(random_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    change_word()


def give_answer():
    card_front_canvas.itemconfig(front_image, image=card_back_image)
    card_front_canvas.itemconfig(title_text, text="English", fill="white")
    card_front_canvas.itemconfig(word_text, text=random_card["English"], fill="white")


try:
    data_df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data_df = pandas.read_csv("data/french_words.csv")
finally:
    data_dict = data_df.to_dict(orient="records")


# UI Setup
BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")

window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
timer = window.after(3 * 1000, func=give_answer)

card_front_canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
front_image = card_front_canvas.create_image(400, 263, image=card_front_image)
title_text = card_front_canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = card_front_canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
card_front_canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=change_word)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=remove_word)
right_button.grid(column=1, row=1)

change_word()

window.mainloop()
