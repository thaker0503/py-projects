from lib2to3.pgen2.token import RIGHTSHIFT
from tkinter import *
import wikipedia as wiki

root = Tk()
root.title("Yatharth - Wikipedia")
root.geometry("700x675")

#Clear
def clear():
    my_entry.delete(0, END)
    my_text.delete(0.0, END)

#Search
def search():
    data = wiki.page(my_entry.get())
    #Clear Screen
    clear()
    #Output Wiki Results to text box
    my_text.insert(0.0, data.content)


my_label_frame = LabelFrame(root, text="Search Wikipedia:")
my_label_frame.pack(pady=20)

#Create etry box
my_entry = Entry(my_label_frame, font=("Helvetica,18"), width=47)
my_entry.pack(pady=20,padx=20)

#Create textbox frame
my_frame = Frame(root)
my_frame.pack(pady=5)

#vertical scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#Horizontal scrollbar
hor_scroll = Scrollbar(my_frame, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)

#Create textbox
my_text = Text(my_frame, yscrollcommand=text_scroll.set, wrap = "none", xscrollcommand=hor_scroll.set)
my_text.pack()

#Configure Scrollbars
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

#Button frame
button_frame = Frame(root)
button_frame.pack(pady=10)

#buttons
search_button = Button(button_frame, text="Search", font=("Helvetica", 30), fg="#3a3a3a", command=search)
search_button.grid(row=0,column=0, padx=20)

clear_button = Button(button_frame, text="Clear", font=("Helvetica", 30), fg="#3a3a3a", command=clear)
clear_button.grid(row=0,column=1)


root.mainloop()