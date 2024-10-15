import Test,Read_Data
import numpy as np
from tkinter import filedialog
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.interpolate import make_interp_spline

def Build_Plot(lines):
    x = []
    y = []
    for points in lines:
        if len(points.split(' ')) != 2:
            continue
        point = points.split(' ')
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

    frame,(Continuous,Discrete) = plt.subplots(1,2,figsize=(10,4))

    Continuous.plot(x_quad,y_quad)
    Continuous.axhline(0, color='black',linewidth=1)
    Continuous.axvline(0, color='black',linewidth=1) 
    Continuous.grid(True)
    Continuous.set_xlabel('Time')
    Continuous.set_ylabel('Amplitude')
    Continuous.set_title('Analog Signal')

    # Remove The Red Line on The X-axis (basefmt)
    Discrete.stem(x, y,basefmt='none',linefmt='k-',markerfmt="C0o")
    Discrete.axhline(0, color='black', linewidth=1)
    Discrete.axvline(0, color='black', linewidth=1)
    Discrete.grid(True)
    Discrete.set_xlabel('Time')
    Discrete.set_ylabel('Amplitude')
    Discrete.set_title('Digital Signal')

    plt.show()

def Cos_Sin_plot(A,F,Fs,Theta,type):
    x = np.arange(0,Fs,1)
    print()
    if type == 0:
        y = A * np.cos(2 * np.pi * F * x / Fs + Theta)
    else:
        y = A * np.sin(2 * np.pi * F * x  / Fs + Theta)

    # x_y_Spline = make_interp_spline(x, y)
    # x_quad = np.linspace(x.min(), x.max(), 500)
    # y_quad = x_y_Spline(x_quad)

    Read_Data.Write_Data(x,y)
   
    plt.plot(x,y)
    # plt.xlim([0, 0.1])
    plt.axhline(0,color='black',linewidth=1)
    plt.axvline(0,color='black',linewidth=1)
    plt.grid(True)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("Sin-Signal" if type == 1 else "Cos-Signal")
    plt.show()


    print(len(x),len(y))
    Check = filedialog.askopenfilename()
    Test.SignalSamplesAreEqual(Check,x,y)