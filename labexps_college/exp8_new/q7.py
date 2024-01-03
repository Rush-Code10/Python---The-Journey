import tkinter as tk
from tkinter import Menu
root = tk.Tk()

def _quit():
    root.quit()
    root.destroy()
    exit()

menuBar=Menu(root)
root.config(menu=menuBar)

fileMenu= Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New File")
fileMenu.add_command(label="New Project")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)

menuBar.add_cascade(label="File", menu=fileMenu)

editMenu = Menu(menuBar, tearoff=0)
editMenu.add_command(label="Cut")
editMenu.add_command(label="Copy")
editMenu.add_separator()
editMenu.add_command(label="Paste")

menuBar.add_cascade(label="Edit", menu=editMenu)
root.mainloop()