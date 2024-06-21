import pandas
from tkinter import *
import random
BACKGROUND_COLOR = "#B1DDC6"
TIMER = None
current_card = ""
to_learn = {}
try:
    word_data = pandas.read_csv("data/New words to learn")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = word_data.to_dict(orient="records")


def new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(output_word, text=current_card["French"], fill="black")
    canvas.itemconfig(current_image, image=img)
    flip_timer = window.after(3000, func=card_flip)

def is_known():
    to_learn.remove(current_card)
    new_to_learn = pandas.DataFrame(to_learn)
    new_to_learn.to_csv("data/New words to learn", index=False)
    print(len(to_learn))
    new_word()


def card_flip():
    global current_card
    canvas.itemconfig(current_image, image=back_image)
    canvas.itemconfig(language, fill="white")
    canvas.itemconfig(output_word, fill="white")
    canvas.itemconfig(language, text="English")
    canvas.itemconfig(output_word, text=current_card["English"])


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=card_flip)

canvas = Canvas(width=850, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img = PhotoImage(file="images/card_front.png")
current_image = canvas.create_image(400, 263, image=img)
back_image = PhotoImage(file="images/card_back.png")
language = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
output_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=0)

wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=new_word)
unknown_button.grid(row=1, column=1)

new_word()




window.mainloop()
