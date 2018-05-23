# Analyze core
# Kobe Arthur Scofield
# 2018-05-16
# Build 1
# Python: Anaconda 5.1.0.0 (Python 3.6.2)
# IDE: Microsoft Visual Studio Community 15.7.1

# import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

def predict_value(time, data, future):
    prd = linear_model.LinearRegression()
    prd.fit(time, data)
    prdvalue = prd.predict(future)
    return prdvalue
#
