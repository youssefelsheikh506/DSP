import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.interpolate import make_interp_spline

def Build_Plot(lines):
    x = []
    y = []
    for points in lines:
        point = points.split(' ')
        #  print(point)
        x.append(float(point[0]))
        y.append(float(point[1]))

    x = np.array(x)
    y = np.array(y)
    
    x_y_Spline = make_interp_spline(x, y)
    x_quad = np.linspace(x.min(), x.max(), 500)
    y_quad = x_y_Spline(x_quad)

    cubic_interpolation_model = interp1d(x, y, kind = "cubic")
    x_cubic = np.linspace(x.min(), x.max(), 500)
    y_cubic = cubic_interpolation_model(x_cubic)

    plt.plot(x_cubic,y_cubic)
    plt.style.use('fivethirtyeight')
    plt.xlabel('Time')
    plt.ylabel('A')
    plt.title('Time Domain')
    plt.legend()
    plt.show()