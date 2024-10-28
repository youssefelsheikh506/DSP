import tkinter as tk
from tkinter import messagebox
import Read_Data , Ploting
import Gui
root = tk.Tk()
root.title("DSP")
root.geometry("1000x1000")

instruction_label = tk.Label(root, text="Select Your File")
instruction_label.pack(pady=10)

lines = []
Prop = []
# 1) SignalType 2) IsPeriodic 3) Number of Samples

Gui.Generate(root,lines,Prop)

root.mainloop() 