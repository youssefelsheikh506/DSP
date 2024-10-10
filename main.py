import tkinter as tk
import GetPath , Ploting
root = tk.Tk()
root.title("DSP")
root.geometry("600x600")

instruction_label = tk.Label(root, text="Select Your File")
instruction_label.pack(pady=10)

lines = []
Prop = []
# 1) SignalType 2) IsPeriodic 3) Number of Samples

def find_path():
    GetPath.Get_Path(lines,Prop)

def plot_button():

    Ploting.Build_Plot(lines)

# Create a button to trigger the greeting
path_button = tk.Button(root,text="Browse",command=find_path)
path_button.pack(pady=10)

path_button = tk.Button(root,text="Plot",command=plot_button)
path_button.pack(pady=10)

root.mainloop()