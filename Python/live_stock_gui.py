from tkinter import *

import numpy as np
import pandas as pd
import pandas_datareader as pdr
import yfinance as yf
import tkinter as tk
import plotly.graph_objs as go

def do_something(stock):
    yf.pdr_override()

    df = yf.download(tickers=stock,period='1d',interval='1h')

    
    return df


def do_onething():
    pass

def main():
    root = tk.Tk()
    root.title("Live Stock Price") #Title of the app

    tk.Label(root, text="Please enter Stock Symbol: ").grid(row=0) #Text Display
    user_input = tk.Entry(root)                                    #To Take User Input
    user_input.grid(row=0, column=1)
    result1 = tk.Label(root, text='STOCK Details')
    result1.grid(row=2, column=0, columnspan=2)
    result2 = tk.Label(root, text='STOCK Graph')
    result2.grid(row=3, column=0, columnspan=2)
    btn = tk.Button(root, text='Fetch Details')
    btn.config(command=lambda: [result1.config(text=do_something(user_input.get()))][result2.config(text=do_onething())])
    btn.grid(row=1, column=1, sticky=tk.W, pady=4)

    root.mainloop()

if __name__ == "__main__":
    main()