import Test,Read_Data
import numpy as np
from tkinter import filedialog
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.interpolate import make_interp_spline

def Build_Plot(X, Y):
    # Convert inputs to numpy arrays (if they are not already)
    x = np.array(X)
    y = np.array(Y)
    
    # Spline interpolation
    x_y_Spline = make_interp_spline(x, y)
    x_smooth = np.linspace(x.min(), x.max(), 500)  # Generate smooth x values
    y_smooth = x_y_Spline(x_smooth)  # Generate corresponding smooth y values

    # Optional: Cubic interpolation (use either this or spline, not both)
    # cubic_interpolation_model = interp1d(x, y, kind="cubic")
    # y_cubic = cubic_interpolation_model(x_smooth)

    # Plot the smoothed signal
    plt.plot(x_smooth, y_smooth, label='Smooth Curve')
    
    # Adding grid and axis labels
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.grid(True)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Analog Signal')

    # Show the plot
    plt.legend()
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