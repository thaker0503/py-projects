import time
from tkinter import *

app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("1920x1080")
app_window.resizable(1,1)



text_font = ("Boulder", 128, 'bold')
background = "#000000"
foreground= "#FFFFFF"
border_width = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground,bd=border_width)
 
label.grid(row=2, column=2)
label.place(relx=0.5, rely=0.5, anchor= CENTER)


def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)

digital_clock()
app_window.mainloop()