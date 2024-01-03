import tkinter as tk

window = tk.Tk()
window.geometry("600x210")

frame1 = tk.Frame(master=window, height=30, bg="red")
frame1.pack(fill=tk.X,pady=2)

frame2 = tk.Frame(master=window, height=30, bg="green")
frame2.pack(fill=tk.X,pady=2)

frame3 = tk.Frame(master=window, height=30, bg="orange")
frame3.pack(fill=tk.X,pady=2)

frame4 = tk.Frame(master=window, height=30, bg="white")
frame4.pack(fill=tk.X,pady=2)

frame5 = tk.Frame(master=window, height=30, bg="yellow")
frame5.pack(fill=tk.X,pady=2)

frame6 = tk.Frame(master=window, height=30, bg="blue")
frame6.pack(fill=tk.X,pady=2)

c1 = tk.Button(window,text='red',font=('Times New Roman','12'),width=20)
c1.place(x=1,y=0)

c2 = tk.Button(window,text='green',font=('Times New Roman','12'),width=20)
c2.place(x=1,y=35)

c3 = tk.Button(window,text='orange',font=('Times New Roman','12'),width=20)
c3.place(x=1,y=70)

c4 = tk.Button(window,text='white',font=('Times New Roman','12'),width=20)
c4.place(x=1,y=103)

c5 = tk.Button(window,text='yellow',font=('Times New Roman','12'),width=20)
c5.place(x=1,y=137)

c6 = tk.Button(window,text='blue',font=('Times New Roman','12'),width=20)
c6.place(x=1,y=171)

window.mainloop()