import tkinter as tk
from tkinter import ttk
import math

# Constants
c = 299792  # speed of light in km/s (299,792,458 m/s)

# Functions
def calculate_time_dilation():
    velocity_unit = velocity_unit_var.get()
    v = float(entry_velocity.get())
    t = float(entry_time.get())
    
    # Convert velocity to km/s if needed
    if velocity_unit == "m/s":
        v = v / 1000  # Convert m/s to km/s
    elif velocity_unit == "C":
        v = v * c  # Convert fraction of C to km/s
    
    t_prime = t / math.sqrt(1 - (v ** 2 / c ** 2))
    result_var.set(f"Time Dilation: {t_prime:.4f} seconds")

def calculate_length_contraction():
    velocity_unit = velocity_unit_var.get()
    v = float(entry_velocity.get())
    l = float(entry_length.get())
    
    # Convert velocity to km/s if needed
    if velocity_unit == "m/s":
        v = v / 1000  # Convert m/s to km/s
    elif velocity_unit == "C":
        v = v * c  # Convert fraction of C to km/s
    
    l_prime = l * math.sqrt(1 - (v ** 2 / c ** 2))
    result_var.set(f"Length Contraction: {l_prime:.4f} kilometers")

# GUI Setup
root = tk.Tk()
root.title("Special Relativity Calculator")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Velocity input
ttk.Label(frame, text="Velocity:").grid(column=0, row=0, sticky=tk.W)
entry_velocity = ttk.Entry(frame)
entry_velocity.grid(column=1, row=0)

# Velocity unit selection
velocity_unit_var = tk.StringVar(value="km/s")
velocity_unit_choices = ["km/s", "m/s", "C"]
ttk.Label(frame, text="Unit:").grid(column=2, row=0, sticky=tk.W)
velocity_unit_menu = ttk.OptionMenu(frame, velocity_unit_var, velocity_unit_var.get(), *velocity_unit_choices)
velocity_unit_menu.grid(column=3, row=0, sticky=tk.W)

# Time input for time dilation
ttk.Label(frame, text="Time (seconds):").grid(column=0, row=1, sticky=tk.W)
entry_time = ttk.Entry(frame)
entry_time.grid(column=1, row=1)

# Length input for length contraction
ttk.Label(frame, text="Length (kilometers):").grid(column=0, row=2, sticky=tk.W)
entry_length = ttk.Entry(frame)
entry_length.grid(column=1, row=2)

# Buttons for calculations
ttk.Button(frame, text="Calculate Time Dilation", command=calculate_time_dilation).grid(column=0, row=3, sticky=tk.W, pady=5)
ttk.Button(frame, text="Calculate Length Contraction", command=calculate_length_contraction).grid(column=1, row=3, sticky=tk.W, pady=5)

# Result display
result_var = tk.StringVar()
ttk.Label(frame, textvariable=result_var).grid(column=0, row=4, columnspan=4)

root.mainloop()
