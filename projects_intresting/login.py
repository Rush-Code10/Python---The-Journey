import tkinter as tk

# Create the login window
login_window = tk.Tk()
login_window.title("Login")

# Define the login function
def do_login():
    # Get the entered username and password
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username and password are correct
    if username == "admin" and password == "password":
        # Close the login window and open the main window
        login_window.destroy()
        main_window = tk.Tk()
        main_window.title("Main")
        main_window.mainloop()
    else:
        # Display an error message
        error_label.config(text="Invalid username or password")

# Create the username label and entry
username_label = tk.Label(login_window, text="Username:")
username_label.grid(row=0, column=0)
username_entry = tk.Entry(login_window)
username_entry.grid(row=0, column=1)

# Create the password label and entry
password_label = tk.Label(login_window, text="Password:")
password_label.grid(row=1, column=0)
password_entry = tk.Entry(login_window, show="*")
password_entry.grid(row=1, column=1)

# Create the login button
login_button = tk.Button(login_window, text="Login", command=do_login)
login_button.grid(row=2, column=1)

# Create the error label
error_label = tk.Label(login_window, fg="red")
error_label.grid(row=3, columnspan=2)

# Start the main loop
login_window.mainloop()
