import random
from tkinter import *

root = Tk()

root.title('Dice Stimulator')
root.geometry('600x500')
label = Label(root, font = ("Helvitica", 300, "bold"))
label.pack()

def roll_dice():
    label.configure(text= random.randint(1,6))
    label.pack()

button =Button(root, font = ("Helvitica", 30, "bold"), text = "Dice Roll", command = roll_dice)
button.pack()

root.mainloop()
