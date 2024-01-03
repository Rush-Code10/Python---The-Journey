import random
import string
import tkinter as tk
from tkinter import *

# Define the GUI window
window = tk.Tk()
window.title("Password Generator")
window.configure(bg="black")

# Define the functions
def generate_password():
    password = ""
    length = int(length_entry.get())

    # Generate the password
    for i in range(length):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)

    # Update the password label
    password_label.config(text=password)

# Create the GUI elements
length_label = tk.Label(window, text="Length: ")
length_label.config(bg="black", fg="white", font=("Times New Roman", 12),relief=RAISED,bd=10)
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(window,justify=CENTER,font=('Times New Roman',10,'bold'),relief=SUNKEN,bd=10)
length_entry.config(width=30)
length_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(window, text="Generate", command=generate_password)
generate_button.config(bg="black", fg="white", font=("Times New Roman", 12),relief=RAISED,bd=10)
generate_button.grid(row=1, column=0, padx=10, pady=10)

password_label = tk.Label(window, text="")
password_label.config(bg="black", fg="white", font=("Times New Roman", 16))
password_label.grid(row=1, column=1, padx=10, pady=10)

# Start the GUI
window.mainloop()
