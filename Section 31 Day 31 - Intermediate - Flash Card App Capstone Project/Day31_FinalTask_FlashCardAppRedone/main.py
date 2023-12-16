from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
random_card = {}


def give_french_word():
    global random_card, timer
    window.after_cancel(timer)
    random_card = random.choice(data_dict)
    card_canvas.itemconfig(card_image, image=card_front_image)
    card_canvas.itemconfig(language_text, text="French", fill="black")
    card_canvas.itemconfig(word_text, text=random_card["French"], fill="black")
    timer = window.after(3000, flip_card)


def flip_card():
    global random_card
    card_canvas.itemconfig(card_image, image=card_back_image)
    card_canvas.itemconfig(language_text, text="English", fill="white")
    card_canvas.itemconfig(word_text, text=random_card["English"], fill="white")


def remove_card():
    global random_card
    data_dict.remove(random_card)
    to_learn_data_df = pandas.DataFrame(data_dict)
    to_learn_data_df.to_csv("data/words_to_learn.csv", index=False)
    give_french_word()


# Read data
try:
    data_df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data_df = pandas.read_csv("data/french_words.csv")
    data_dict = data_df.to_dict(orient="records")
else:
    data_dict = data_df.to_dict(orient="records")


# UI SETUP
window = Tk()
window.title("Learn French via Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
timer = window.after(3000, flip_card)

card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_image = card_canvas.create_image(400, 263, image=card_front_image)
language_text = card_canvas.create_text(400, 150, text="", font=("Ariel", 40, "normal"), fill="black")
word_text = card_canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
card_canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_image, bg=BACKGROUND_COLOR, command=give_french_word)
wrong_button.grid(column=0, row=1)

tick_image = PhotoImage(file="images/right.png")
right_button = Button(image=tick_image, bg=BACKGROUND_COLOR, command=remove_card)
right_button.grid(column=1, row=1)

give_french_word()

window.mainloop()
