import tkinter as tk
from Read_Data import Read_Data
from Ploting import Build_Plot, Cos_Sin_plot
from Task2 import Add_Sub_Two_Signals,Normalize_Signal,Multi,accumulation_Signal
from Task_3 import Quntiz

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