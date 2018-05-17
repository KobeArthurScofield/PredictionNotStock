# Analyze core
# Kobe Arthur Scofield
# 2018-05-16
# Build 1
# Python: Anaconda 5.1.0.0 (Python 3.6.2)
# IDE: Microsoft Visual Studio Community 15.7.1

def get_data(x_axis, y_axis):
    x_parameter = []
    y_parameter = []
    for x1,y1 in zip(x_axis, y_axis):
        x_parameter.append([float(x1)])
        y_parameter.append(float(y1))
    return x_parameter, y_parameter
#
