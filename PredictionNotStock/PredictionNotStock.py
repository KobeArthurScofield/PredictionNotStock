# A prediction of car numbers
# Kobe Arthur Scofield
# 2018-05-15
# Python: Anaconda 5.1.0.0 (Python V 3.6.2)
# IDE: Microsoft Visual Studio Community 15.7.1

print("Load libraries...")
import numpy as np
print("NumPy (1/4) loaded")
import pandas as pd
print("Pandas (2/4) loaded")
from sklearn import datasets, linear_model
print("Scikit-Learn (3/4) partial loaded")
import matplotlib.pyplot as mtpl
print("MatPlotLib.PyPlot (4/4) loaded")
from llib import iodp
from llib import analyzecore as anlz
print("MISC Library loaded")
print(" ")

file = iodp.filepath_trim(input("Please input the path of data: "))
l_Time, l_Value = iodp.dget_csv_data(file, "Seq", "Lowest")
a_Time, a_Value = iodp.dget_csv_data(file, "Seq", "Average")

l_xi, l_predict = anlz.get_data(l_Time, l_Value)
a_xi, a_predict = anlz.get_data(a_Time, a_Value)

print(l_xi, l_predict, a_xi, a_predict)

mtpl.figure(figsize=(6, 4), dpi=300)
mtpl.plot(l_Time, l_Value, label="Lowest")
mtpl.plot(a_Time, a_Value, label="Average")
mtpl.legend()
mtpl.show()
