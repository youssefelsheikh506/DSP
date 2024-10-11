import tkinter as tk
import Read_Data , Ploting
root = tk.Tk()
root.title("DSP")
root.geometry("600x600")

instruction_label = tk.Label(root, text="Select Your File")
instruction_label.pack(pady=10)

lines = []
Prop = []
# 1) SignalType 2) IsPeriodic 3) Number of Samples

def Read():
    lines.clear()
    Prop.clear()
    Read_Data.Read_Data(lines,Prop)

def plot_button():
    Ploting.Build_Plot(lines)

def Sumbit_Button():
    A = float(Amplitude.get())
    F = float(AnalogFrequency.get())
    Fs = float(SamplingFrequency.get())
    Theta = float(PhaseShift.get())
    Ploting.Cos_plot(A,F,Fs,Theta,var.get())

var = tk.IntVar()
var.set(0)

Cos_Radio = tk.Radiobutton(root,text="Cos",variable=var,value=0)
Sin_Radio = tk.Radiobutton(root,text="Sin",variable=var,value=1)

Cos_Radio.pack()
Sin_Radio.pack()

path_button = tk.Button(root,text="Browse",command=Read)
path_button.pack(pady=10)

path_button = tk.Button(root,text="Plot",command=plot_button)
path_button.pack(pady=10)

Amplitude = tk.Entry(root, width=30)
Amplitude.pack(pady=10)

AnalogFrequency = tk.Entry(root, width=30)
AnalogFrequency.pack(pady=10)

SamplingFrequency = tk.Entry(root, width=30)
SamplingFrequency.pack(pady=10)

PhaseShift = tk.Entry(root, width=30)
PhaseShift.pack(pady=10)

Submit = tk.Button(root,text="Draw",command=Sumbit_Button)
Submit.pack(pady=10)

root.mainloop()