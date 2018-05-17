# INput/Output operation module
# Kobe Arthur Scofield
# 2018-05-15
# Build 3
# Python: Anaconda3_64 5.0.1.0 (Python 3.6.2)
# IDE: MSVS2017_Community 15.7.1

import numpy as np
import pandas as pd
import matplotlib.pyplot as mtpl

def filepath_trim(path):
    """
    Trimming Path to prevent unexpected quotes problem.
    """
    if (path[0] == '"') or (path[0] == "'"):
        path = path[1:]
    if (path[-1] == '"') or (path[-1] == "'"):
        path = path[:-1]
    return path
#

def dget_csv_data(file_name, x_data, y_data):
    """
    Directly read X-Y Data from a CSV file.
    Parameters:
    file_name: The path of the csv data
    x_data: The label of X data in CSV file
    y_data: The label of Y data in CSV file
    """
    data = pd.read_csv(file_name)
    # print(data)
    X_parameter = []
    Y_parameter = []
    for single_square_feet ,single_price_value in zip(data[x_data],data[y_data]):   # To pack them all and send data to two variables
        X_parameter.append([float(single_square_feet)]) # Parameter required (and I don't know why)
        Y_parameter.append(float(single_price_value))
    # print(X_parameter)
    # print(Y_parameter)
    return X_parameter,Y_parameter
#

def read_csv_file(filepath, dttype = "str", skpfrw = 1, dlv = ','):
    """
    Data Readin
    """
    return np.loadtxt(filepath, dtype= dttype, skiprows= skpfrw, delimiter= dlv)

def stock_data_unpack(srclist):
    """
    For stock data only
    To unpack data for later process
    """
    dated = []
    for itemz in srclist[:, 0]:
        dated.append(datetime.datetime.strptime(itemz, '%Y/%m/%d'))
    dealdata = srclist[:, 1:-1].astype(float).reshape((-1, 4))
    volume = srclist[:, -1].astype(int).reshape((-1, 1))
    return (dated, dealdata, volume)
#

def imagesvdp(imgdata, showaxis = False, figsize = (8, 4), dpi = 72,save = True, saveasfig = False, display = True, filepath = "", **kwargs):
    """
    This function is used to save and display the figure.
    """
    mtpl.figure(figsize= figsize, dpi= dpi)
    mtpl.imshow(imgdata, interpolation= "none", **kwargs)
    if (save and len(filepath)):    # len(filepath) checks if you've not input a null string
        if saveasfig:
            mtpl.savefig(filepath)
        else:
            mtpl.imsave(arr= imgdata, fname= filepath)
    if display:     # Display the figure
        if showaxis:
            mtpl.axis("on")
        else:
            mtpl.axis("off")
        mtpl.show()
#
