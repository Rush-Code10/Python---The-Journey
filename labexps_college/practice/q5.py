import tkinter
from tkinter import*
from tkinter import messagebox

def huh():
   tkinter.messagebox.showinfo(entry1.get() ,"Username: "+entry2.get()+'\nPassword: '+entry3.get()+'\nGender: '+agreement.get())

window = tkinter.Tk()
window.title('Form')
window.geometry('260x150')
agreement = tkinter.StringVar()


name = Label(window,text='Name: ',font=('Times New Roman','12'))
name.grid(row=1,column=1)


entry1 = Entry(window,width = 20,justify=CENTER,font=('Times New Roman','12'))
entry1.grid(row=1,column=2)


username = Label(window,text='UserName: ',font=('Times New Roman','12'))
username.grid(row=2,column=1)


entry2 = Entry(window,width = 20,justify=CENTER,font=('Times New Roman','12'))
entry2.grid(row=2,column=2)


passkey = Label(window,text='Password: ',font=('Times New Roman','12'))
passkey.grid(row=3,column=1)


entry3 = Entry(window,width = 20,justify=CENTER,font=('Times New Roman','12'))
entry3.grid(row=3,column=2)


m = Checkbutton(window,text='Male',command=huh,variable=agreement,onvalue='Male',).grid(row=4,column=1)
f = Checkbutton(window,text='Female',command=huh,variable=agreement,onvalue='Female',).grid(row=4,column=2)

btn = Button(window,text='DONE',font=('Times New Roman','12'),command=huh)
btn.place(x=100,y=120)

window.mainloop()
