from tkinter import*
window=Tk()
window.title("Image View")
#img=PhotoImage(file="pup.png")
img = PhotoImage(file="D:\\Users\\Rushabh\\Documents\\Programming\\Python\\labexps\\exp8_new\\pup.png")
label1 = Label(window, image=img)
label1.pack()
window.mainloop()