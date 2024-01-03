import tkinter
from tkinter import*
from tkinter import messagebox

window = tkinter.Tk()
window.title('Form')
window.geometry('260x150')

def huh():
    tkinter.messagebox.showinfo(entry1.get() ,"Username: "+entry2.get()+'\nPassword: '+entry3.get())

name = Label(window,text='NAME',font=('Times New Roman','12'))
name.grid(row=1,column=1)

entry1 = Entry(window,width = 20,justify=CENTER,font=('Times New Roman','12'))
entry1.grid(row=1,column=2)

username = Label(window,text='USERNAME',font=('Times New Roman','12'))
username.grid(row=2,column=1)

entry2 = Entry(window,width = 20,justify=CENTER,font=('Times New Roman','12'))
entry2.grid(row=2,column=2)

passkey = Label(window,text='PASSWORD',font=('Times New Roman','12'))
passkey.grid(row=3,column=1)

entry3 = Entry(window,width = 20,justify=CENTER,font=('Times New Roman','12'))
entry3.grid(row=3,column=2)

btn = Button(window,text='DONE',font=('Times New Roman','12'),command=huh)
btn.place(x=100,y=75)

window.mainloop()