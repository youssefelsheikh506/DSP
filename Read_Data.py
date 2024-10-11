import tkinter as tk
from tkinter import filedialog

def Read_Data(lines,Prop):
    path = filedialog.askopenfilename()
    if path:
        with open(path,'r') as file:
            for line in file:
                line = line.split("\n")
                lines.append(line[0])    
        Prop.append(lines[0])
        Prop.append(lines[1])
        Prop.append(lines[2])
        del lines[0]
        del lines[0]
        del lines[0]
    else:
         print("Invalid")