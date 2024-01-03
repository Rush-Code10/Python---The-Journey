# import the modules
from tkinter import*
from tkinter import ttk
import tkinter
import random

# list of possible colour.
colours = ['Red','Blue','Green','Pink','Yellow','Orange','White','Purple','Brown']

score = 0
timeleft = 45

def startGame(event):
    if timeleft == 45:
        countdown()
    nextColour()


def nextColour():
    global score
    global timeleft
    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score: " + str(score))



def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text = "Time left: "+
                                str(timeleft))
        timeLabel.after(1000, countdown)


root = tkinter.Tk()

root.title("COLOR GAME")
root.configure(bg='#000000')
root.geometry("400x275")

instructions = tkinter.Label(root,
                             text = "Type in the colour"" of the words, and not the word text!\n",
                             font = ('Times New Roman', 12),
                             foreground="white",
                             background="black")
instructions.pack()

scoreLabel = tkinter.Label(root,
                           text = "Press enter to start",
                           font = ('Times New Roman', 12),
                           foreground="white",
                           background="black",
                           relief=SUNKEN,
                           bd=10,
                           padx=15,
                           pady=4,
                           )
scoreLabel.pack()

timeLabel = tkinter.Label(root,
                          text = "\nTime left: " + str(timeleft),
                          font = ('Times New Roman', 12),
                          foreground="white",
                          background="black",
                          )

timeLabel.pack()

label = tkinter.Label(root,
                      font = ('Times New Roman', 50),
                      foreground="white",
                      background="black")
label.pack()

separator1 = ttk.Separator(root, orient='horizontal')
separator1.pack(fill='x')

e = tkinter.Entry(root,justify=CENTER,font=('Times New Roman',10,'bold'),relief=SUNKEN,bd=10)

root.bind('<Return>', startGame)
e.pack()

e.focus_set()

separator2 = ttk.Separator(root, orient='horizontal')
separator2.pack(fill='x')

root.mainloop()
