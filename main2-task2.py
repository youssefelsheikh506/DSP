import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox, StringVar, Label, Entry, Button, OptionMenu
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SignalProcessor:
    def __init__(self, master):
        self.master = master
        master.title("Signal Processor")
        master.geometry("800x600")

        self.signal1 = None
        self.signal2 = None
        self.result_signal = None

        self.constant = StringVar()
        self.normalize_option = StringVar(value="0 to 1")  # Default normalization option

        # Create the GUI components
        self.create_widgets()

    def create_widgets(self):
        # Buttons to load signals from files
        Button(self.master, text="Load Signal 1", command=lambda: self.load_signal(1)).grid(row=0, column=0)
        Button(self.master, text="Load Signal 2", command=lambda: self.load_signal(2)).grid(row=1, column=0)

        # Operation Buttons
        Button(self.master, text="Add Signals", command=self.add_signals).grid(row=2, column=0)
        Button(self.master, text="Subtract Signals", command=self.subtract_signals).grid(row=3, column=0)
        Button(self.master, text="Multiply Signal 1", command=self.multiply_signal).grid(row=4, column=0)
        Button(self.master, text="Square Signal 1", command=self.square_signal).grid(row=5, column=0)
        Button(self.master, text="Shift Signal 1", command=self.shift_signal).grid(row=6, column=0)
        Button(self.master, text="Accumulate Signal 1", command=self.accumulate_signal).grid(row=7, column=0)  # New button for accumulation
        Button(self.master, text="Normalize Signal 1", command=self.normalize_signal).grid(row=8, column=0)

        # Input for constant value
        Label(self.master, text="Enter Constant:").grid(row=4, column=1)
        Entry(self.master, textvariable=self.constant).grid(row=4, column=2)

        # Dropdown Menu for Normalization Options
        Label(self.master, text="Normalization Option:").grid(row=8, column=1)
        OptionMenu(self.master, self.normalize_option, "0 to 1", "-1 to 1").grid(row=8, column=2)

        # Canvas for Plotting Results
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, self.master)
        self.canvas.get_tk_widget().grid(row=9, column=0, columnspan=4)

    def load_signal(self, signal_number):
        """Load a signal from a text file and store it."""
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not file_path:
            return  # User cancelled the file dialog

        try:
            data = np.loadtxt(file_path)  # Load as 2D array
            signal = data[:, 1]  # Extract the second column (signal values)

            if signal_number == 1:
                self.signal1 = signal
                messagebox.showinfo("Success", "Signal 1 loaded successfully!")
            elif signal_number == 2:
                self.signal2 = signal
                messagebox.showinfo("Success", "Signal 2 loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load signal: {e}")

    def add_signals(self):
        """Add two signals and display the result."""
        if self.signal1 is not None and self.signal2 is not None:
            self.result_signal = self.signal1 + self.signal2
            self.plot_signal(self.result_signal, "Addition Result")
        else:
            messagebox.showwarning("Warning", "Please load both signals.")

    def subtract_signals(self):
        """Subtract two signals and display the result."""
        if self.signal1 is not None and self.signal2 is not None:
            self.result_signal = self.signal1 - self.signal2
            self.plot_signal(self.result_signal, "Subtraction Result")
        else:
            messagebox.showwarning("Warning", "Please load both signals.")

    def multiply_signal(self):
        """Multiply Signal 1 by a constant and display the result."""
        if self.signal1 is not None:
            try:
                constant = float(self.constant.get())
                self.result_signal = self.signal1 * constant
                self.plot_signal(self.result_signal, "Multiplication Result")
            except ValueError:
                messagebox.showerror("Error", "Enter a valid constant value.")
        else:
            messagebox.showwarning("Warning", "Please load Signal 1.")

    def square_signal(self):
        """Square Signal 1 and display the result."""
        if self.signal1 is not None:
            self.result_signal = np.square(self.signal1)
            self.plot_signal(self.result_signal, "Squared Signal")
        else:
            messagebox.showwarning("Warning", "Please load Signal 1.")

    def shift_signal(self):
        """Shift Signal 1 by a constant and display the result."""
        if self.signal1 is not None:
            try:
                constant = float(self.constant.get())
                self.result_signal = self.signal1 + constant
                self.plot_signal(self.result_signal, "Shifted Signal")
            except ValueError:
                messagebox.showerror("Error", "Enter a valid constant value.")
        else:
            messagebox.showwarning("Warning", "Please load Signal 1.")

    def accumulate_signal(self):
        """Accumulate Signal 1 and display the result."""
        if self.signal1 is not None:
            self.result_signal = np.cumsum(self.signal1)
            self.plot_signal(self.result_signal, "Accumulated Signal")
        else:
            messagebox.showwarning("Warning", "Please load Signal 1.")

    def normalize_signal(self):
        """Normalize Signal 1 based on user choice and display the result."""
        if self.signal1 is not None:
            if self.normalize_option.get() == "0 to 1":
                self.result_signal = (self.signal1 - np.min(self.signal1)) / (np.max(self.signal1) - np.min(self.signal1))
            else:
                self.result_signal = 2 * (self.signal1 - np.min(self.signal1)) / (np.max(self.signal1) - np.min(self.signal1)) - 1
            self.plot_signal(self.result_signal, "Normalized Signal")
        else:
            messagebox.showwarning("Warning", "Please load Signal 1.")

    def plot_signal(self, signal, title):
        """Plot the signal on the canvas."""
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(signal)
        ax.set_title(title)
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = SignalProcessor(root)
    root.mainloop()
