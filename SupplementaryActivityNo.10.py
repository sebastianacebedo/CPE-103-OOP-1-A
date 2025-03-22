import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Main window
window = tk.Tk()
window.title("The Selection Widgets using Pycharm")
window.geometry('400x350')

# Guide
guide_frame = ttk.LabelFrame(window, text="Guide", padding=10)
guide_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

guide_text = ("1. Select your birth month, day, and year.\n"
              "2. Click 'Show Info' to confirm your selection.\n"
              "3. The selected birth date will be displayed in a message box.")
ttk.Label(guide_frame, text=guide_text).grid(row=0, column=0)

# Frame
form_frame = ttk.LabelFrame(window, text="Enter Your Birth Date", padding=10)
form_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

form_frame.configure(labelwidget=ttk.Label(
    form_frame, text="Enter Your Birth Date", font=("Arial", 14, "bold"), foreground="red"
))

# Labels
ttk.Label(form_frame, text="Month:", font=("Arial", 11, "bold")).grid(row=0, column=0, padx=5, pady=5)
ttk.Label(form_frame, text="Day:", font=("Arial", 11, "bold")).grid(row=1, column=0, padx=5, pady=5)
ttk.Label(form_frame, text="Year:", font=("Arial", 11, "bold")).grid(row=2, column=0, padx=5, pady=5)

# Variables for Comboboxes
month_var = tk.StringVar()
day_var = tk.StringVar()
year_var = tk.StringVar()

# Create Comboboxes
month_cb = ttk.Combobox(form_frame, width=15, textvariable=month_var)
day_cb = ttk.Combobox(form_frame, width=5, textvariable=day_var)
year_cb = ttk.Combobox(form_frame, width=7, textvariable=year_var)

# Adding values to Comboboxes
month_cb['values'] = ('January', 'February', 'March', 'April', 'May', 'June',
                      'July', 'August', 'September', 'October', 'November', 'December')
day_cb['values'] = [str(i) for i in range(1, 32)]
year_cb['values'] = [str(i) for i in range(1900, 2026)]

# Positioning Comboboxes
month_cb.grid(row=0, column=1, padx=5, pady=5)
day_cb.grid(row=1, column=1, padx=5, pady=5)
year_cb.grid(row=2, column=1, padx=5, pady=5)

# Setting default selections
month_cb.current(0)  # Default to January
day_cb.current(0)    # Default to 1
year_cb.current(125) # Default to year 2000

#Function
def show_info():
    showinfo(
        title="Selected Birth Date",
        message=f'Your Birth Date: {month_var.get()} {day_var.get()}, {year_var.get()}'
    )

# Show Info Button
ttk.Button(form_frame, text="Show Info", command=show_info).grid(row=3, column=0, columnspan=2, pady=10)

# Run the main application loop
window.mainloop()
