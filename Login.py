from tkinter import *
from tkinter import messagebox
import os
import pickle
import subprocess  # Import the subprocess module

import secrets

# Initialize the main window
root = Tk()
root.title('Login System')
root.geometry('300x150')  # Set the window size


# Style options
font_large = ('Arial', 12)
padding = {'padx': 5, 'pady': 5}

# Check if the database file exists and load/create if necessary
if os.path.exists('logins.pkl'):
    with open('logins.pkl', 'rb') as f:
        logins = pickle.load(f)
else:
    logins = {}
    with open('logins.pkl', 'wb') as f:
        pickle.dump(logins, f)

# Function to check if the login details are correct
def check_login():
    email = email_entry.get()
    password = password_entry.get()
    if email in logins and logins[email] == password:
        messagebox.showinfo('Login Successful', 'You have successfully logged in')
        random_string = generate_random_string(10)
        messagebox.showinfo('Random String', f'Random String: {random_string}')
        input_window = Toplevel(root)
        input_window.title('Input Random String')
        input_window.geometry('300x100')
        Label(input_window, text='Enter Random String:', font=font_large).pack(**padding)
        random_string_entry = Entry(input_window, font=font_large)
        random_string_entry.pack(**padding)
        Button(input_window, text='Submit', command=lambda: validate_random_string(random_string, random_string_entry.get()), font=font_large, width=10).pack(**padding)
    else:
        messagebox.showerror('Login Failed', 'Incorrect email or password')

# Function to create a new login
def create_login():
    email = email_entry.get()
    password = password_entry.get()
    if email in logins:
        messagebox.showerror('Error', 'Email already in use')
    else:
        logins[email] = password
        with open('logins.pkl', 'wb') as f:
            pickle.dump(logins, f)
        messagebox.showinfo('Success', 'New login created')


# Function to check for bots, random string should be remembered
def generate_random_string(length):
    length = 3
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(secrets.choice(alphabet) for _ in range(length))

# Function to validate the random string
def validate_random_string(random_string, input_string):
    if random_string == input_string:
        try:
            subprocess.Popen(['python', 'other_program.py'])
        except Exception as e:
            messagebox.showerror('Error', f'Failed to start the program: {str(e)}')
    else:
        messagebox.showerror('Error', 'Incorrect random string')
        email_entry.delete(0, END)
        password_entry.delete(0, END)
        del logins[email_entry.get()]
        with open('logins.pkl', 'wb') as f:
            pickle.dump(logins, f)

        
# Setting up the GUI layout
Label(root, text='Email:', font=font_large).grid(row=0, column=0, **padding)
Label(root, text='Password:', font=font_large).grid(row=1, column=0, **padding)
email_entry = Entry(root, font=font_large)
password_entry = Entry(root, font=font_large, show='*')
email_entry.grid(row=0, column=1, **padding)
password_entry.grid(row=1, column=1, **padding)
Button(root, text='Login', command=check_login, font=font_large, width=10).grid(row=2, column=0, sticky=W, **padding)
Button(root, text='Create Login', command=create_login, font=font_large, width=12).grid(row=2, column=1, sticky=W, **padding)

root.mainloop()