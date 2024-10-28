import tkinter as tk
import math
from tkinter import filedialog
from Read_Data import Read_Data
from Test import QuantizationTest1,QuantizationTest2
def Quntiz(level,value):
    lines = Read_Data([])
    x = []
    y = []
    for points in lines:
        if len(points.split(' ')) != 2:
            continue
        point = points.split(' ')
        x.append(float(point[0]))
        y.append(float(point[1]))
    min_el = min(y)
    max_el = max(y)

    num_bits = 0

    if level == 1:
        div =  math.ceil(math.log2(int(value)))
        num_bits = div
        div = pow(2,int(div))
    else:
        num_bits = int(value)    
        div = pow(2,int(value))

    delta = round((max_el - min_el) / div,3)
    
    Ranges = []
    Ranges.append(min_el)
    for i in range (1,div + 1):        
        Ranges.append(round(Ranges[i - 1],1) + delta)
    
    midpoints = [round(min_el + delta * (i + 0.5),3) for i in range(div)]

    max_bits = num_bits
    midpoints_dict = {midpoint: format(i, f'0{max_bits}b') for i, midpoint in enumerate(midpoints)}

    pair_dic = {}

    for i in range(len(Ranges) - 1):
        key = (Ranges[i],Ranges[i + 1])
        pair_dic[key] = midpoints[i]

    x_out = []
    y_out = []
    error = []
    interval = []

    for i in y:
        values = find_enclosing_values_and_midpoint(i,Ranges,midpoints)
        encode = midpoints_dict[pair_dic[(values[0]),values[1]]]
        quntaiz_value = pair_dic[(values[0]),values[1]]
        y_out.append(quntaiz_value)
        x_out.append(encode)
        error.append(round(quntaiz_value - i,3))
        interval.append(int(encode,2) + 1)

    if level == 1:
        QuantizationTest2(filedialog.askopenfilename(),interval,x_out,y_out,error)
    else:
        QuantizationTest1(filedialog.askopenfilename(),x_out,y_out)

            
def find_enclosing_values_and_midpoint(value, range_values, midpoints):
    for i in range(len(range_values) - 1):
        if range_values[i] <= value <= range_values[i + 1]:
            return range_values[i], range_values[i + 1]
