import tkinter as tk
from tkinter import filedialog
from Read_Data import Read_Data
from Ploting import Build_Plot
from Test import SignalSamplesAreEqual
def Add_Sub_Two_Signals(sign):
    first_Signal = Read_Data([])
    first_dic = {}
    for points in first_Signal:
        point = points.split(' ')
        first_dic[float(point[0])] = float(point[1])
 
    secound_Signal = Read_Data([])
    secound_dic = {}
    for points in secound_Signal:
        point = points.split(' ')
        secound_dic[float(point[0])] = float(point[1])
    
    total_x = []
    total_y = []

    all_keys = set(first_dic.keys()).union(set(secound_dic.keys()))
    for key in all_keys:
        value1 = first_dic.get(key, 0)
        value2 = secound_dic.get(key, 0)    
        if(sign == 0):
            total_value = value1 + value2
        else:
            total_value = value2 - value1 
        total_x.append(key)
        total_y.append(total_value)

    compare_path = filedialog.askopenfilename()
    SignalSamplesAreEqual(compare_path,total_x,total_y)
    Build_Plot([],1,total_x,total_y)

def Multi(value,check):
    signal =  Read_Data([])

    x = []
    y = []

    for points in signal:
        point = points.split(' ')
        x.append(float(point[0]))
        y.append(float(point[1]))

    if check == 0:
        y = [x * float(value) for x in y]
    else:
        y = [x * x for x in y]

    compare_path = filedialog.askopenfilename()
    SignalSamplesAreEqual(compare_path,x,y)
    Build_Plot([],1,x,y)

def Normalize_Signal(check):
    signal = Read_Data([])

    x = []
    y = []

    for points in signal:
        point = points.split(' ')
        x.append(float(point[0]))
        y.append(float(point[1]))

    min_element = min(y)
    max_element = max(y)

    if check == 0:
        y = [(x - min_element) / (max_element - min_element) for x in y]
    else:
        y = [2 * (x - min_element) / (max_element - min_element) - 1 for x in y]

    compare_path = filedialog.askopenfilename()
    SignalSamplesAreEqual(compare_path,x,y)
    Build_Plot([],1,x,y)

def accumulation_Signal():
    signal = Read_Data([])
    x = []
    y = []
    y_out = []
    for points in signal:
        point = points.split(' ')
        x.append(float(point[0]))
        y.append(float(point[1]))
    size = len(y)
    y_out.append(y[0])
    for i in range(1,size):
        y_out.append(y_out[i - 1] + y[i])

    compare_path = filedialog.askopenfilename()
    SignalSamplesAreEqual(compare_path,x,y_out)
    Build_Plot([],1,x,y)