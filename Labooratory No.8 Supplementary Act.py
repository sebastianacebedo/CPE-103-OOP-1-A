import tkinter as tk
import math

# Functions for calculations
def add():
    try:
        result.set(float(entry1.get()) + float(entry2.get()))
        update_history(f"{entry1.get()} + {entry2.get()} = {result.get()}")
    except ValueError:
        result.set("Invalid input: Use numeric value")

def subtract():
    try:
        result.set(float(entry1.get()) - float(entry2.get()))
        update_history(f"{entry1.get()} - {entry2.get()} = {result.get()}")
    except ValueError:
        result.set("Invalid input: Use numeric value")

def multiply():
    try:
        result.set(float(entry1.get()) * float(entry2.get()))
        update_history(f"{entry1.get()} * {entry2.get()} = {result.get()}")
    except ValueError:
        result.set("Invalid input: Use numeric value")

def divide():
    try:
        num2 = float(entry2.get())
        if num2 != 0:
            result.set(float(entry1.get()) / num2)
            update_history(f"{entry1.get()} / {entry2.get()} = {result.get()}")
        else:
            result.set("Error! Division by zero.")
    except ValueError:
        result.set("Invalid input: Use numeric value")

def square_root():
    try:
        num = float(entry1.get())
        res = math.sqrt(num)
        result.set(res)
        update_history(f"√{num} = {res}")
    except ValueError:
        result.set("Invalid input: Use numeric value")

def power():
    try:
        result.set(float(entry1.get()) ** float(entry2.get()))
        update_history(f"{entry1.get()} ^ {entry2.get()} = {result.get()}")
    except ValueError:
        result.set("Invalid input: Use numeric value")

def update_history(entry):
    history_list.insert(tk.END, entry)

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.set("")
    history_list.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple TUI Calculator")
root.geometry("400x510")
root.configure(bg="skyblue")

# Create StringVar to hold the result
result = tk.StringVar()

# Create the layout
tk.Label(root, text="Enter first number:", font=("Arial", 10, "bold"), bg="skyblue").grid(row=0, column=0)
entry1 = tk.Entry(root, font=("Arial", 10))
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter second number:", font=("Arial", 10, "bold"), bg="skyblue").grid(row=1, column=0)
entry2 = tk.Entry(root, font=("Arial", 10))
entry2.grid(row=1, column=1)

# Blank space for emphasis
tk.Label(root, text="", font=("Arial", 10), bg="skyblue").grid(row=2, column=0)

# Buttons for operations
tk.Button(root, text="Add", command=add, bg="green", fg="white").grid(row=3, column=0)
tk.Button(root, text="Subtract", command=subtract, bg="green", fg="white").grid(row=3, column=1)
tk.Button(root, text="Multiply", command=multiply, bg="green", fg="white").grid(row=4, column=0)
tk.Button(root, text="Divide", command=divide, bg="green", fg="white").grid(row=4, column=1)
tk.Button(root, text="Power", command=power, bg="green", fg="white").grid(row=5, column=0)
tk.Button(root, text="Square Root", command=square_root, bg="green", fg="white").grid(row=5, column=1)

# Blank space for emphasis
tk.Label(root, text="", font=("Arial", 10), bg="skyblue").grid(row=6, column=0)

# Label to show result
tk.Label(root, text="Result:", font=("Arial", 10, "bold"), bg="skyblue").grid(row=7, column=0)
result_label = tk.Label(root, textvariable=result, font=("Arial", 12), fg="black", bg="skyblue")
result_label.grid(row=7, column=1)

# Blank space under the result
tk.Label(root, text="", font=("Arial", 10), bg="skyblue").grid(row=8, column=0)

# History feature
tk.Label(root, text="History:", font=("Arial", 10, "bold"), bg="skyblue").grid(row=9, column=0)
history_list = tk.Listbox(root, height=11, width=60)
history_list.grid(row=10, column=0, columnspan=7, padx=10,pady=5)

# Blank space above the Clear All button
tk.Label(root, text="", font=("Arial", 10), bg="skyblue").grid(row=17, column=0)

# Clear All button aligned to the left
tk.Button(root, text="Clear All", command=clear, bg="red", fg="white").grid(row=18, column=0, columnspan=1, ipadx=20)

# Start the main loop
root.mainloop()
