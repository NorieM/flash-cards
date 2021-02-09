from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/french_words.csv')

vocabulary = data.to_dict(orient='records')
current_card = {}


# ---------- TRACK PROGRESS ------- #
def knows_word():
    vocabulary.remove(current_card)
    pd.DataFrame(vocabulary).to_csv('data/words_to_learn.csv', index=False)
    next_card()


# -------------- NEXT CARD -------------- #
def next_card():
    global current_card, flip_timer
    current_card = random.choice(vocabulary)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_image, image=card_front_img)
    window.after_cancel(flip_timer)
    flip_timer = window.after(3000, flip_card)


# -------------- FLIP CARD -------------- #
def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_image, image=card_back_img)

# -------------- CREATE UI --------------- #


window = Tk()

window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

card_front_img = PhotoImage(file='./images/card_front.png')
card_back_img = PhotoImage(file='./images/card_back.png')
cross_image = PhotoImage(file='./images/wrong.png')
tick_image = PhotoImage(file='./images/right.png')

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400, 150, text='Title', font=('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='Word', font=('Arial', 60, 'bold'))

unknown_button = Button(image=cross_image, command=next_card, borderwidth=0, highlightthickness=0)
unknown_button.grid(row=1, column=0)

known_button = Button(image=tick_image, command=knows_word, borderwidth=0, highlightthickness=0)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
