import tkinter as tk
root = tk.Tk()
root.title("DSP")
root.geometry("600x600")

instruction_label = tk.Label(root, text="Enter your Text file Name")
instruction_label.pack(pady=10)

path_entry = tk.Entry(root, width=30)
path_entry.pack(pady=10)

path = "C:/Users/lenovo/Desktop/DSP/Test/"
file_name = ""
lines = []

def show_path():
    file_name = path_entry.get()
    print(path + file_name + ".txt")
    with open (path + file_name + ".txt",'r') as file:
        for line in file:
            line = line.split("\n")
            lines.append(line[0])
        print(lines)

# Create a button to trigger the greeting
path_button = tk.Button(root,text="Enter",command=show_path)
path_button.pack(pady=100)

root.mainloop()