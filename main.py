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
import tensorflow as tf
from tensorflow import keras
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras import layers
from tensorflow.keras import callbacks
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# Windows settings
root = tk.Tk()
#root.iconbitmap(r'icon.ico')
root.geometry("600x500")
root.resizable(True, True)
root.title("Stock Tracker Portal")
root.configure(bg = "#282C2F")

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
instructionFrame = tk.Frame(master = root)
topFrame = tk.Frame(master = root)
bodyFrame = tk.Frame(master = root)

# User instructions
instructions = tk.Label(
    master = instructionFrame,
    text = "1. Select timeframe of prices.\n2. Click Submit.\n3. Produce results!",
    font = 'TkDefault 16',
    foreground = 'white',
    background = '#303030'
    )
instructions.grid(row=0, column = 0)
instructionFrame.pack()

# Text box for stock ticker
fileInput = tk.Entry(master = topFrame, width = 55, bd = 2, justify = "left", font = "TkDefault 10")
fileInput.grid(row = 1, column = 0)

# Drop down box to add time frame
timeOptions = ["1D", "1W", "1M", "3M", "6M", "1Y", "5Y", "max"]
optionList = tk.StringVar(topFrame)
optionList.set(timeOptions[0])
timePeriod = tk.OptionMenu(topFrame, optionList, *timeOptions)
timePeriod.config(width = 3, font = "TKDefault 10")
timePeriod.grid(row = 1, column = 1)

# Button to commence search for data
fileAccept = tk.Button(master = topFrame, text = "Submit", font = "TkDefault 10", command = searchTicker)
fileAccept.grid(row = 1, column = 2)
topFrame.pack()

# Immediate Predictions
result1 = tk.Label(
    master = bodyFrame,
    text = "Price is going: [UP/DOWN]\n",
    font = 'TkDefault 16',
    foreground = 'white',
    background = '#303030'
    )
result1.grid(row = 2, column = 0)
result2 = tk.Label(
    master = bodyFrame,
    text = "Predicted Price: ",
    font = 'TkDefault 12',
    foreground = 'white',
    background = '#303030'
    )
result2.grid(row = 3, column = 0)
result3 = tk.Label(
    master = bodyFrame,
    text = "Percent change from yesterday: ",
    font = 'TkDefault 12',
    foreground = 'white',
    background = '#303030'
    )
result3.grid(row = 4, column = 0)
bodyFrame.pack()

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


root.mainloop()







def some_prep(data):
    new_data = data[["Date", "Adj Close"]].shift(-1)
    new_data[['Open', 'High', 'Low', 'Close', 'Volume']] =  data[
        ['Open', 'High', 'Low', 'Close', 'Volume']]
    to_predict = new_data.iloc[-1:]
    return new_data, to_predict
    
    
def get_data(data):
    val_size = data.shape[0]
    val_size = 2112
    train_size = 4931
    data = data.drop("Date", axis = 1)
    cols = data.columns
    scaler = MinMaxScaler(feature_range=(0, 1)) 
    data = pd.DataFrame(scaler.fit_transform(data), columns = cols)
    data_x = (data.copy()).drop("Adj Close", axis = 1)
    data_y = data["Adj Close"]
    X_train = data_x.iloc[:train_size]
    X_val = data_x.iloc[val_size:]
    Y_train =  data_y.iloc[:train_size]
    Y_val = data_y.iloc[val_size:]
    return X_train, X_val, Y_train, Y_val
    
def model_deep(data):
    # normalize the dataset 
    X_train, X_valid, y_train, y_valid = get_data(data)
    input_shape = [data.shape[1] - 1]
    model = keras.Sequential([
    layers.BatchNormalization(input_shape=input_shape),
    layers.Dense(512, activation='relu'),
    layers.BatchNormalization(),
    layers.Dense(512, activation='relu'),
    layers.BatchNormalization(),
    layers.Dense(512, activation='relu'),
    layers.BatchNormalization(),
    layers.Dense(1),
    ])
    model.compile(
    optimizer='sgd',
    loss='mae',
    metrics=['mae'],
    )
    EPOCHS = 100
    history = model.fit(
        X_train, y_train,
        validation_data=(X_valid, y_valid),
        batch_size=64,
        epochs=EPOCHS,
        verbose=0,
        )

    history_df = pd.DataFrame(history.history)
    return history_df
    
    
def linear_reg(data):
    input_shape = [data.shape[1] - 1]
    data_x = data["Date"]
    data_y = data["Adj Close"]
    model = keras.Sequential([layers.Dense(units=1, input_shape = [6])])
    model(data_x)
    weights = model.get_weights()
    return weights
    
#df['Date'] = pd.to_datetime(df.Date,format='%Y-%m-%d')







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


