from tkinter import *

def sel():
   selection = "You selected the Bank " + str(var.get())
   label.config(text = selection)

root = Tk()
root.geometry("250x150")
root.title("Select a bank")
var = IntVar()
R1 = Radiobutton(root, text="Bank 1", variable=var, value=1, command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Bank 2", variable=var, value=2, command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Bank 3", variable=var, value=3, command=sel)
R3.pack( anchor = W)

R4 = Radiobutton(root, text="Bank 4", variable=var, value=4, command=sel)
R4.pack( anchor = W)

R5 = Radiobutton(root, text="Bank 5", variable=var, value=5, command=sel)
R5.pack( anchor = W)

label = Label(root)
label.pack()
root.mainloop()