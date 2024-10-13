from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
#--------------PANDAS-----------#
try:
    data = pandas.read_csv('data/words_to_learn.csv', sep=';')
except FileNotFoundError:
    original_data = pandas.read_csv("data/german_words.csv", sep=';')
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Deutsch",fill="black")
    canvas.itemconfig(card_word, text=current_card["Deutsch"],fill="black")
    canvas.itemconfig(card_bg, image=front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="Türkçe",fill="white")
    canvas.itemconfig(card_word, text=current_card["Turkce"],fill="white")
    canvas.itemconfig(card_bg, image=back_image)
    
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False, sep=';')
    next_card()
    
#--------------WINDOW---------#   
window =  Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
#-----------------CANVAS-------------#
canvas = Canvas(width=800,height=526)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400,263,image=front_image)
card_title = canvas.create_text(400, 150,text="",font=("Ariel",20,"italic"))
card_word = canvas.create_text(400, 263,text="",font=("Ariel",25,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)
#---------------BUTTONS----------------#
right_image = PhotoImage(file="C:/Users/elanu/OneDrive/Desktop/flash-card-project-start/images/right.png")
button_r = Button(image=right_image,command=is_known)
button_r.config(bg=BACKGROUND_COLOR,highlightthickness=0)
button_r.grid(column=1,row=1)

wrong_image = PhotoImage(file="C:/Users/elanu/OneDrive/Desktop/flash-card-project-start/images/wrong.png")
button_w = Button(image=wrong_image,command=next_card)
button_w.config(bg=BACKGROUND_COLOR,highlightthickness=0)
button_w.grid(column=0,row=1)

next_card()




window.mainloop()
