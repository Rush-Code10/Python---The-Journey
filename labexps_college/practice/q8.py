from tkinter import*
root =Tk()
root.geometry("400x130")

frame1 = Frame(root,bg="Red",relief=RIDGE,)
frame2 = Frame(root,bg="Green",relief=RIDGE)
frame3 = Frame(root,bg="Orange",relief=RIDGE)
frame4 = Frame(root,bg="White",relief=RIDGE)
frame5 = Frame(root,bg="Yellow",relief=RIDGE)
frame6 = Frame(root,bg="Blue",relief=RIDGE)

frame1.pack(fill=X, padx=5)
frame2.pack(fill=X, padx=5)
frame3.pack(fill=X, padx=5)
frame4.pack(fill=X, padx=5)
frame5.pack(fill=X, padx=5)
frame6.pack(fill=X, padx=5)


label1=Label(frame1,text="Red",relief=RIDGE,width=10)
label2=Label(frame2,text="Green",relief=RIDGE,width=10)
label3=Label(frame3,text="Orange",relief=RIDGE,width=10)
label4=Label(frame4,text="White",relief=RIDGE,width=10)
label5=Label(frame5,text="Yellow",relief=RIDGE,width=10)
label6=Label(frame6,text="Blue",relief=RIDGE,width=10)


label1.pack(side=LEFT)
label2.pack(side=LEFT)
label3.pack(side=LEFT)
label4.pack(side=LEFT)
label5.pack(side=LEFT)
label6.pack(side=LEFT)



root.mainloop()
