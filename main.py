from tkinter import * 
from random import choice
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
WIDTH, HEIGHT = 800, 526

# Window basic configs
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

def nextCard():
    global currentWord, timer
    window.after_cancel(timer)
    currentWord = choice(data)
    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(cardTitle, text="Chinese", fill="black")
    canvas.itemconfig(cardWord, text=currentWord["zh"], fill="black")
    canvas.itemconfig(cardSubtext, text=currentWord["zh_fone"], fill="black")
    timer = window.after(3000, func=showAnswer)


def showAnswer():
    global currentWord
    canvas.itemconfig(cardTitle, text="English", fill="white")
    canvas.itemconfig(cardWord, text=currentWord["en"], fill="white")
    canvas.itemconfig(cardSubtext, text="")
    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(card, image=card_back_img)

# globals
currentWord = {}
timer = window.after(3000,func=showAnswer)

# Translation data as dict
data = pd.read_csv("translationData.csv").to_dict(orient="records")

canvas = Canvas(width=WIDTH, height=HEIGHT)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card = canvas.create_image(WIDTH//2,263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
cardTitle = canvas.create_text(WIDTH//2, HEIGHT*1/5, text="", font= ("Ariel", 35, "italic"))
cardWord = canvas.create_text(WIDTH//2, HEIGHT//2, text="START", font= ("Times", 65, "bold"))
cardSubtext = canvas.create_text(WIDTH//2, HEIGHT*7/10, text="", font= ("Ariel", 40, "italic"))

wrongImage = PhotoImage(file="images/wrong.png")
wrongButton = Button(image=wrongImage, command=nextCard)
wrongButton.grid(row=1, column=0)

rightImage = PhotoImage(file="images/right.png")
rightButton = Button(image=rightImage, command=nextCard)
rightButton.grid(row=1,column=1)

window.mainloop()
