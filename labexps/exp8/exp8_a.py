# Registration Form

import tkinter
from tkinter import*

s=tkinter.Tk()
s.title("Registration Form")
s.geometry('300x350')

line=Label(s,text="Full name: ").grid(row=1,column=1)
e=Entry(s,width=30).grid(row=1,column=2)
line1=Label(s,text="Email Address: ").grid(row=2,column=1)
e1=Entry(s,width=30).grid(row=2,column=2)

var=IntVar()
Radiobutton(s,text="Male",variable=var,value=1).place(x=51,y=53)
Radiobutton(s,text="Female",variable=var,value=2).place(x=51,y=70)
Radiobutton(s,text="Other",variable=var,value=3).place(x=51,y=87)

line2=Label(s,text="Residence: ").place(x=1,y=115)
line1=Listbox(s)
line1.insert(1,'India')
line1.insert(2,'USA')
line1.insert(3,'UK')
line1.place(x=90,y=115)

line3=Label(s,text="Programming: ").place(x=1,y=285)
var1=IntVar()
cb1=Checkbutton(s,text='C',variable=var1,offvalue=0,onvalue=1).place(x=100,y=285)
var2=IntVar()
cb2=Checkbutton(s,text='Python',variable=var2,offvalue=0,onvalue=1).place(x=150,y=285)

b1=Button(s,text="Submit",bg='light blue').place(x=150,y=315)
s.mainloop()
