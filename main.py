"""
Different teams for the project (see discord for the rest of the information)

1. GUI (tkinter)
2. Graphs, stats and data-analysis (statitstics and matplotlib for graphs)
3. AI and predictive analysis (tensorflow and scikit)

"""


#import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import datetime
import statistics
#from matplotlib import pyplot

# Windows settings
root = tk.Tk()
#root.iconbitmap(r'icon.ico')
root.geometry("600x500")
root.resizable(True, True)
root.title("Stock tracker")
root.configure(bg = "#a2a2a2")


data = ""
# Reading the data files (format Datasets\File.csv)
def acceptFile(fileName):
    try:
        data = pd.read_csv(fileName)
    except Exception as e:
        messagebox.showerror(title = "Invalid file", message = "Please ensure file is in current working directory and the correct name was entered!")
        print(e)

# Finding the corresponding data file for the current ticker + time period
def searchTicker():
    ticker = fileInput.get()
    time = optionList.get()
    try:
       acceptFile("Datasets\\" + ticker.upper() + "_" + time + ".csv")
    except Exception as e:
        messagebox.showerror(title="Invalid file", message="Please ensure file is in current working directory and the correct name was entered!")
        print(e)



# Frames for organization
topFrame = tk.Frame(master = root)
bodyFrame = tk.Frame(master = root)

# Text box for stock ticker
# TODO implement smart search of ticker to generate file
fileInput = tk.Entry(master = topFrame, width = 55, bd = 2, justify = "left", font = "TkDefault 10")
fileInput.grid(row = 0, column = 0)

# Drop down box to add time frame
timeOptions = ["1D", "1W", "1M", "3M", "6M", "1Y", "5Y", "max"]
optionList = StringVar(topFrame)
optionList.set(timeOptions[0])
timePeriod = tk.OptionMenu(topFrame, optionList, *timeOptions)
timePeriod.config(width = 3, font = "TKDefault 10")
timePeriod.grid(row = 0, column = 1)


# Button to commence search for data
fileAccept = tk.Button(master = topFrame, text = "Submit", font = "TkDefault 10", command = searchTicker)
fileAccept.grid(row = 0, column = 2)


topFrame.pack()
bodyFrame.pack()

root.mainloop()

