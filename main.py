from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"


current_data={}
to_learn={}

try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    to_learn=original_data.to_dict("records")
else:
    to_learn=data.to_dict(orient="records")




def next_card():
    global current_data,flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_background,image=card_front)
    current_data = random.choice(to_learn)
    canvas.itemconfig(card_title,text='French',fill='black')
    canvas.itemconfig(card_word,text=current_data['French'],fill='black')
    flip_timer=window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title,text='English',fill='white')
    canvas.itemconfig(card_word,text=current_data['English'],fill='white')
    canvas.itemconfig(card_background,image=card_back)

def is_known():
    to_learn.remove(current_data)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()





window=Tk()
window.title('Flash Cards')
window.config(background=BACKGROUND_COLOR,padx=50,pady=50)

flip_timer=window.after(3000,func=flip_card)


canvas=Canvas(window,width=800,height=526)
card_front=PhotoImage(file='images/card_front.png')
card_background=canvas.create_image(400,263,image=card_front)
canvas.config(background=BACKGROUND_COLOR,highlightthickness=0)
card_back=PhotoImage(file='images/card_back.png')
card_title=canvas.create_text(400,150,text="TITLE",font=("Aerial",40,"italic"))
card_word=canvas.create_text(400,263,text="word",font=("Aerial",60,"bold"))

canvas.grid(row=0,column=0,columnspan=2)



correct_check=PhotoImage(file="./images/right.png")

correct_button = Button(image=correct_check, highlightthickness=0,command=next_card)
correct_button.grid(row=1,column=1)


wrong_check=PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_check, highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)

next_card()

window.mainloop()

