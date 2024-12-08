import tkinter as tk
from tkinter import ttk
from Read_Data import Read_Data
from Ploting import Build_Plot, Cos_Sin_plot
from Task2 import Add_Sub_Two_Signals,Normalize_Signal,Multi,accumulation_Signal
from Task_3 import Quntiz
from Task_4 import *
from Folding import *
from Task_5 import *
from Task_7 import *

def Generate(root, lines,Prop):
    var = tk.IntVar()
    var.set(0)  # Default value for Cos/Sin selection
    
    # Create radio buttons for Cos and Sin
    Cos_Radio = tk.Radiobutton(root, text="Cos", variable=var, value=0)
    Sin_Radio = tk.Radiobutton(root, text="Sin", variable=var, value=1)
    Cos_Radio.pack()
    Sin_Radio.pack()

    # Browse Button (to Read Data)
    path_button = tk.Button(root, text="Browse", command=lambda: Read_Data(lines,Prop))
    path_button.pack(pady=10)

    # Plot Button (now delayed using lambda)
    plot_button = tk.Button(root, text="Plot", command=lambda: Build_Plot(lines))
    plot_button.pack(pady=10)

    # Input fields for Amplitude, Analog Frequency, Sampling Frequency, and Phase Shift
    Amplitude = tk.Entry(root, width=30)
    Amplitude.pack(pady=10)
    
    AnalogFrequency = tk.Entry(root, width=30)
    AnalogFrequency.pack(pady=10)

    SamplingFrequency = tk.Entry(root, width=30)
    SamplingFrequency.pack(pady=10)

    PhaseShift = tk.Entry(root, width=30)
    PhaseShift.pack(pady=10)

    # Draw Button to plot Cos/Sin based on user input (using lambda to delay execution)
    Submit = tk.Button(root, text="Draw", 
                       command=lambda: Cos_Sin_plot(
                           float(Amplitude.get()), 
                           float(AnalogFrequency.get()), 
                           float(SamplingFrequency.get()), 
                           float(PhaseShift.get()), 
                           var.get()
                       ))
    Submit.pack(pady=10)

    Add_Sub = tk.IntVar()
    Add_Sub.set(0) 

    Add_Radio = tk.Radiobutton(root, text="Add", variable=Add_Sub, value=0)
    Sub_Radio = tk.Radiobutton(root, text="Sub", variable=Add_Sub, value=1)
    Add_Radio.pack()
    Sub_Radio.pack()

    Add_Two_Signals = tk.Button(root, text="Add Or Sub Two Signals", command=lambda: Add_Sub_Two_Signals(Add_Sub.get()))
    Add_Two_Signals.pack(pady=30)

    Multi_button = tk.Button(root, text="Multi Or Squaring", command=lambda: Mult_Window())
    Multi_button.pack(pady=10)

    Normalize = tk.IntVar()
    Normalize.set(0) 

    zero_to_one = tk.Radiobutton(root, text="[(0) -> (1)]", variable=Normalize, value=0)
    negative_to_postive = tk.Radiobutton(root, text="[(-1) -> (1)]", variable=Normalize, value=1)
    zero_to_one.pack()
    negative_to_postive.pack()

    Normalize_button = tk.Button(root, text="Normalize", command=lambda: Normalize_Signal(Normalize.get()))
    Normalize_button.pack(pady=10)

    Accumlate_button = tk.Button(root, text="Accumulation", command=lambda: accumulation_Signal())
    Accumlate_button.pack(pady=10)

    Lvl_or_bits = tk.IntVar()
    Lvl_or_bits.set(0) 

    bits = tk.Radiobutton(root, text="Bits", variable=Lvl_or_bits, value=0)
    lvl = tk.Radiobutton(root, text="Levels", variable=Lvl_or_bits, value=1)
    bits.pack()
    lvl.pack()

    value = tk.Entry(root, width=30)
    value.pack(pady=10)

    Quntaiz = tk.Button(root, text="Quntaiz", command=lambda: Quntiz(Lvl_or_bits.get(),value.get()))
    Quntaiz.pack(pady=10)

    task_4 = tk.Button(root, text="DFT", command=lambda: DFT())
    task_4.pack(pady=10)

    task_idft = tk.Button(root, text="IDFT", command=lambda: IDFT())
    task_idft.pack(pady=10)

    time_domain_button = tk.Button(root, text="Time Domain", command=lambda: Time_Domain(lines,Prop))
    time_domain_button.pack(pady=10)

def Mult_Window():

    root = tk.Tk()
    root.title("MUlti")
    
    plot_button = tk.Button(root, text="Genrate", command=lambda: Multi(value.get(),0))
    plot_button.pack(pady=10)

    Squaring_button = tk.Button(root, text="Square Signal", command=lambda: Multi(value.get(),1))
    Squaring_button.pack(pady=10)

    value = tk.Entry(root, width=30)
    value.pack(pady=10)

    root.geometry("400x400")
    root.mainloop()

def Time_Domain(lines,prop):

    lines_2 = []
    prop_2 = []

    root = tk.Tk()
    root.title("Time Domain")
    root.geometry("800x800")

    select_btn = tk.Button(root, text="Select File", command=lambda: Read_Data(lines,prop))
    select_btn.pack(pady=10)

    select_btn_2 = tk.Button(root, text="Select File", command=lambda: Read_Data(lines_2,prop_2))
    select_btn_2.pack(pady=10)

    value = tk.Entry(root, width=30)
    value.pack(pady=10)

    fold_or_not = tk.Entry(root, width=30)
    fold_or_not.pack(pady=10)

    plot_button_1 = tk.Button(root, text="Fold and Sheift", command=lambda: fold_signal(*Procces_file(lines),int(fold_or_not.get()),int(value.get())))
    plot_button_1.pack(pady=10)

    Derivateive = tk.Button(root, text="Derivative Signal", command=lambda: DerivativeSignal())
    Derivateive.pack(pady=10)

    dct_bnt = tk.Button(root, text="DCT Signal", command=lambda: dct(*Procces_file(lines)))
    dct_bnt.pack(pady=10)

    moving_avg = tk.Entry(root, width=30)
    moving_avg.pack(pady=10)

    Smoothing_bnt = tk.Button(root, text="Smoothing", command=lambda: smooth_signal(*Procces_file(lines),moving_avg.get(),prop))
    Smoothing_bnt.pack(pady=10)

    remove_dc = tk.Button(root, text="Remove DC", command=lambda: Reomve_DC(*Procces_file(lines)))
    remove_dc.pack(pady=10)

    conv_bnt = tk.Button(root, text="Convolution", command=lambda: Convolution(*Procces_file(lines),*Procces_file(lines_2),prop,prop_2))
    conv_bnt.pack(pady=10)

    conr_bnt = tk.Button(root, text="Correlation", command=lambda: Correlation(*Procces_file(lines),*Procces_file(lines_2),prop,prop_2))
    conr_bnt.pack(pady=10)

    Fir_filter = tk.Button(root, text="Fir_Filter", command=lambda: Fir_fillter())
    Fir_filter.pack(pady=10)

    root.mainloop()

def Fir_fillter():
    root = tk.Tk()
    root.title("Time Domain")
    root.geometry("800x800")
    # Label
    label = tk.Label(root, text="Select Filter Type: 0(Low)  1(High)  2(Band pass)  3(Band stop)", font=("Arial", 12))
    label.pack(pady=10)
    type = tk.Entry(root, width=30)
    type.pack(pady=10)

    fs_lablel = tk.Label(root,text="FS", font=("Arial", 10))
    fs_lablel.pack(pady=10)
    fs = tk.Entry(root, width=30)
    fs.pack(pady=10)

    cutoff_lablel = tk.Label(root,text="FC", font=("Arial", 10))
    cutoff_lablel.pack(pady=10)
    cutoff = tk.Entry(root, width=30)
    cutoff.pack(pady=10)

    cutoff_lablel_1 = tk.Label(root,text="F1", font=("Arial", 10))
    cutoff_lablel_1.pack(pady=10)
    cutoff_1 = tk.Entry(root, width=30)
    cutoff_1.pack(pady=10)

    cutoff_lablel_2 = tk.Label(root,text="F2", font=("Arial", 10))
    cutoff_lablel_2.pack(pady=10)
    cutoff_2 = tk.Entry(root, width=30)
    cutoff_2.pack(pady=10)

    transition_band_labl = tk.Label(root,text="TransitionBand", font=("Arial", 10))
    transition_band_labl.pack(pady=10)
    transition_band = tk.Entry(root, width=30)
    transition_band.pack(pady=10)

    stop_band_labl = tk.Label(root,text="StopBandAttenuation", font=("Arial", 10))
    stop_band_labl.pack(pady=10)
    stop_band = tk.Entry(root, width=30)
    stop_band.pack(pady=10)

    Draw_btn = tk.Button(root, text="Draw", command=lambda: calculate_FIR(int(fs.get()),int(type.get()),int(cutoff.get()),int(cutoff_1.get()),int(cutoff_2.get()),int(transition_band.get()),int(stop_band.get()),int(check_bnt.get())))
    Draw_btn.pack(pady=10)

    draw_check = tk.Label(root,text="0 (Filter)  1(Apply Filter)", font=("Arial", 10))
    draw_check.pack(pady=10)

    check_bnt = tk.Entry(root, width=30)
    check_bnt.pack(pady=10)

    root.mainloop()
    
def Procces_file(lines):
    x = []
    y = []
    for line in lines:
        line = line.split("\n")
        line = line[0].split(" ")
        x.append(float(line[0]))
        y.append(float(line[1]))
    return x,y