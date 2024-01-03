import tkinter
from tkinter import*

window = tkinter.Tk()
window.title('Form')
window.geometry('200x100')

def prix():
    print(entry.get())
    selection = entry.get()
    label.config(text=selection)

entry = Entry(window,width = 20,justify=CENTER,font=('Times New Roman','12'))
entry.pack()

submit = Button(window,text='Submit',font=('Times New Roman','12'),command=prix)
submit.pack()

label = Label(window)
label.pack()

window.mainloop()