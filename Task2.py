import tkinter as tk
from tkinter import filedialog
from Read_Data import Read_Data
from Ploting import Build_Plot
from Test import SignalSamplesAreEqual
def Add_Sub_Two_Signals(sign):
    rows = []
    first_Signal = Read_Data(rows)
    first_dic = {}
    for points in rows:
        point = points.split(' ')
        first_dic[float(point[0])] = float(point[1])
 
    secound_Signal = Read_Data(rows)
    secound_dic = {}
    for points in rows:
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