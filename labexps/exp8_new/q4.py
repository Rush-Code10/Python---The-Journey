from tkinter import *
window =Tk()
f1=LabelFrame(window)
f2=LabelFrame(window)

f1.pack(side=LEFT)
f2.pack(side=RIGHT)

Label(f1).pack(ipadx=75, ipady=50)

a=Checkbutton(f1,text="one").pack(anchor=S,side=LEFT)
b=Checkbutton(f1,text="two").pack(anchor=S,side=LEFT)
c=Checkbutton(f1,text="three").pack(anchor=S,side=LEFT)

Label(f2,text="").pack()
Label(f2,text="").pack()
Label(f2,text="Name").pack()
Label(f2,text="").pack()
Entry(f2).pack()
Label(f2,text="").pack()
Button(f2,text="Okay",width=10).pack(anchor=S,side=LEFT)
Button(f2,text="Cancel",width=10).pack(anchor=S,side=RIGHT)
window.mainloop()