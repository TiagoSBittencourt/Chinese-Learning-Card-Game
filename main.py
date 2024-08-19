from tkinter import *
from random import choice
import pandas as pd

TIMER = 3000
CARD_FRONT_IMAGE_PATH = "images/card_front.png"
CARD_BACK_IMAGE_PATH = "images/card_back.png"
WRONG_IMAGE_PATH = "images/wrong.png"
RIGHT_IMAGE_PATH = "images/right.png"

BACKGROUND_COLOR = "#B1DDC6"
WIDTH, HEIGHT = 800, 526

class FlashCardApp:
    def __init__(self, window):
        self.window = window
        self.currentWord = {}
        self.timer = None
        self.data = pd.read_csv("translationData.csv").to_dict(orient="records")
        
        # Setup the user interface
        self.setup_ui()
        

    def setup_ui(self):
        """Sets up the user interface."""
        self.canvas = Canvas(self.window, width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.card_front_img = PhotoImage(file=CARD_FRONT_IMAGE_PATH)
        self.card_back_img = PhotoImage(file=CARD_BACK_IMAGE_PATH)
        self.card = self.canvas.create_image(WIDTH//2, HEIGHT//2, image=self.card_front_img)
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.cardTitle = self.canvas.create_text(WIDTH//2, HEIGHT//5, text="", font=("Ariel", 35, "italic"))
        self.cardWord = self.canvas.create_text(WIDTH//2, HEIGHT//2, text="START", font=("Times", 65, "bold"))
        self.cardSubtext = self.canvas.create_text(WIDTH//2, HEIGHT*7//10, text="", font=("Ariel", 40, "italic"))
    
        self.wrong_image = PhotoImage(file=WRONG_IMAGE_PATH)
        self.wrong_button = Button(self.window, image=self.wrong_image, command=self.next_card)
        self.wrong_button.grid(row=1, column=0)
        
        self.right_image = PhotoImage(file=RIGHT_IMAGE_PATH)
        self.right_button = Button(self.window, image=self.right_image, command=self.next_card)
        self.right_button.grid(row=1, column=1)

    def next_card(self):
        """Selects a new card and updates the canvas with its content."""
        if self.timer:
            self.window.after_cancel(self.timer)
        
        self.currentWord = choice(self.data)
        self.canvas.itemconfig(self.card, image=self.card_front_img)
        self.canvas.itemconfig(self.cardTitle, text="Chinese", fill="black")
        self.canvas.itemconfig(self.cardWord, text=self.currentWord["zh"], fill="black")
        self.canvas.itemconfig(self.cardSubtext, text=self.currentWord["zh_fone"], fill="black")
        self.timer = self.window.after(TIMER, self.show_answer)

    def show_answer(self):
        """Displays the answer on the card."""
        self.canvas.itemconfig(self.cardTitle, text="English", fill="white")
        self.canvas.itemconfig(self.cardWord, text=self.currentWord["en"], fill="white")
        self.canvas.itemconfig(self.cardSubtext, text="")
        self.canvas.itemconfig(self.card, image=self.card_back_img)

if __name__ == "__main__":
    root = Tk()
    root.title("Flashy")
    root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    app = FlashCardApp(root)
    root.mainloop()