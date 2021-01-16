"""
Different teams for the project (see discord for the rest of the information)

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

data = ""
def acceptFile():
    fileName = fileInput.get()
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


