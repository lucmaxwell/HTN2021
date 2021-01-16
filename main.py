# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 00:12:46 2021

@author: User
"""



"""
Loose groups and teams for the project

1. GUI (tkinter)
2. Graphs, stats and data-analysis (statitstics and matplotlib for graphs)
3. AI and predictive analysis (tensorflow and scikit)

"""



import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import statistics


root = tk.Tk()
root.iconbitmap(r'icon.ico')
root.geometry("500x500")
root.resizable(True, True)
root.title("Stock tracker")
root.configure(bg = "#a2a2a2")


def acceptFile():
    fileName = fileInput.get()
    data = ""
    try:
        data = pd.read_csv(fileName)
    except Exception as e:
        messagebox.showerror(title = "Invalid file", message = "Please ensure file is in current working directory and the correct name was entered!")
        print(e)

fileInput = tk.Entry(root, width = 55, bd = 2, justify = "left", font = "TkDefault 10")
fileInput.grid(row = 0, column = 0)

fileAccept = tk.Button(root, text = "Submit", font = "TkDefault 10", command = acceptFile)
fileAccept.grid(row = 0, column = 1)




root.mainloop()


## convert date into some numeric variable from a given origin
## i think shifting 1993-01-29 to 0 and 2021-01-14 to 7041 should be good
#r = datetime.strptime("1993-02-01", "%Y-%m-%d")

#for i in range(len(spy_data)):
#    spy_data.Date[i] = datetime.strptime(spy_data.Date[i], "%Y-%m-%d")

## this is questionably done
## alternatively this could be done with the time package but idk about
    ## that epoch stuff
## not sure if we should leave the datetime object as is


## basic linear approximation with given variables
## idk about close in this case
## does volume have to be adjusted for