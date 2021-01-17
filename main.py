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
from matplotlib import pyplot as pp
from datetime import datetime, date, timedelta
import statistics
from dateutil.relativedelta import relativedelta
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Windows settings
root = tk.Tk()
#root.iconbitmap(r'icon.ico')
root.geometry("600x500")
root.resizable(True, True)
root.title("Stock tracker")
root.configure(bg = "#a2a2a2")

class point:
    def __init__(self, colData):
        dates, self.open, self.high, self.low, self.close, self.adjClose, self.volume = colData
        year, month, day = dates.split('-')
        self.date = date(int(year), int(month), int(day))
        
# Reading the data files (format Datasets\File.csv)
def acceptFile(fileName):
    try:
        data = pd.read_csv(fileName)
        return data
    except Exception:
        messagebox.showerror(title = "Invalid file", message = "Please ensure file is in current working directory and the correct name was entered!")


def subtractDay(dateObj, num):
    return dateObj - timedelta(num)

def subtractMonth(dateObj, num):
    return dateObj - relativedelta(months=num)

def subtractYear(dateObj, num):
    return dateObj - relativedelta(years=num)


def searchTicker():
    ticker = fileInput.get()
    data = acceptFile('SPY_max.csv').transpose() # change to ticker at the end. Changed to  for testing
    dateObj = []
    for colNum, colData in data.iteritems():
        obj = point(colData)
        dateObj.append(obj)

    dataDates = date.today()

    dateSelection = optionList.get()
    if dateSelection[1] == 'D':
        dataDates = subtractDay(dataDates, int(dateSelection[0]))
    elif dateSelection[1] == 'W':
        dataDates = subtractDay(dataDates, int(dateSelection[0])*7)
    elif dateSelection[1] == 'M':
        dataDates = subtractMonth(dataDates, int(dateSelection[0]))
    elif dateSelection[1] == 'Y':
        dataDates = subtractYear(dataDates, int(dateSelection[0]))
    else:
        dataDates = date(1, 1, 1)
    
    filteredData = set()
    for obj in dateObj:
        if obj.date >= dataDates:
            filteredData.add(obj)


# Frames for organization
topFrame = tk.Frame(master = root)
bodyFrame = tk.Frame(master = root)

# Text box for stock ticker
fileInput = tk.Entry(master = topFrame, width = 55, bd = 2, justify = "left", font = "TkDefault 10")
fileInput.grid(row = 0, column = 0)

# Drop down box to add time frame
timeOptions = ["1D", "1W", "1M", "3M", "6M", "1Y", "5Y", "max"]
optionList = tk.StringVar(topFrame)
optionList.set(timeOptions[0])
timePeriod = tk.OptionMenu(topFrame, optionList, *timeOptions)
timePeriod.config(width = 3, font = "TKDefault 10")
timePeriod.grid(row = 0, column = 1)

# Button to commence search for data
fileAccept = tk.Button(master = topFrame, text = "Submit", font = "TkDefault 10", command = searchTicker)
fileAccept.grid(row = 0, column = 2)

topFrame.pack()

#random data to add to the GUI
data1 = {'Year': [1993,1994,1995,1996,1997,1998,1999,2000],
         'Opening_Price': [41,42,43,44,45,46,47,48.]
        }  
df1 = pd.DataFrame(data1,columns=['Year','Opening_Price'])

#adds the graph to the GUI (under the topFrame and bodyFrame)
figure1 = pp.Figure(figsize=(4,4), dpi=100)
ax1 = figure1.add_subplot(111) # 111 represents how much of the whitespace that the graph fills
line1 = FigureCanvasTkAgg(figure1, root)
line1.get_tk_widget().pack(fill=tk.BOTH)
df1 = df1[['Year','Opening_Price']].groupby('Year').sum()
df1.plot(kind='line', legend=True, ax=ax1, color='r',marker='o', fontsize=10)
ax1.set_title('Year Vs. Opening_Price')

bodyFrame.pack()

root.mainloop()

















"""
# Temporary place for graphing utility
# scope is a list of Day
def graphData(scope):
    x_values = []
    y_values = []

    for i in scope:
        x_values.append(i.date)     # open price
        y_values.append(i.open)

        x_values.append(i.date)     # close price
        y_values.append(i.close)

    pp.plot(x_values, y_values)
    pp.show()
"""