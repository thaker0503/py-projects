from tkinter import *
import tkinter as tk
import random
from functools import partial

# Create an instance of tkinter frame or window
win=Tk()

win.title("Auto Password Generator - Created by Yatharth")

# Set the size of the tkinter window
win.geometry("700x350")

def copy(a):
    win.clipboard_clear()
    win.clipboard_append(a)

def gen():
    lower_case = "abcdefghijklmnopqrstuvwxyz" 
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    symbols = "@!#$&*?\/"
    password = lower_case + upper_case + number + symbols
    pass_len = int(input_int.get())
    
    global gen_pass 
    gen_pass = "".join(random.sample(password,pass_len))
    label.config(text=gen_pass)

    

Label(win, text="Enter the length of your password", font=('Calibri 10')).pack()
input_int=Entry(win, width=35)
input_int.pack()

Button(win, text="Generate!", command=gen).pack()

label = Label(win, text="Generated Password", font=('Calibri 10'))
label.pack(pady=20)

Button(win, text='Copy Generated Password', command=lambda: copy(gen_pass)).pack()



win.mainloop()