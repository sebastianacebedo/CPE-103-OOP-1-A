import tkinter as tk
import math
from tkinter import messagebox


expression = ""


def press(num):
    global expression
    expression += str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except ZeroDivisionError:
        equation.set("Error: Div by 0")
        expression = ""
        messagebox.showerror("Calculation Error", "Cannot divide by zero.")
    except Exception as e:
        equation.set("Error")
        expression = ""
        messagebox.showerror("Calculation Error", f"Invalid Input or Expression:\n{e}")


def clear():
    global expression
    expression = ""
    equation.set("")

def calculate_sqrt():
    global expression
    try:
        expression = str(math.sqrt(float(expression)))
        equation.set(expression)
    except Exception as e:
        equation.set("Error")
        expression = ""
        messagebox.showerror("Calculation Error", f"Invalid Input or Expression:\n{e}")

def calculate_trig(operation):
    global expression
    try:
        value = float(expression)
        if operation == "sin":
            result = math.sin(value)
        elif operation == "cos":
            result = math.cos(value)
        elif operation == "tan":
            result = math.tan(value)
        equation.set(str(result))
        expression = str(result)
    except ValueError:
        equation.set("Error")
        expression = ""
        messagebox.showerror("Calculation Error", "Invalid input for trigonometric function.")
    except Exception as e:
        equation.set("Error")
        expression = ""
        messagebox.showerror("Calculation Error", f"An unexpected error occurred:\n{e}")


window = tk.Tk()
window.title("Functional Calculator")
window.geometry("400x550")
window.configure(bg="#96D4CC")


equation = tk.StringVar()
display_entry = tk.Entry(window, textvariable=equation, font=('Arial', 24), borderwidth=2, relief="sunken", justify='right')
display_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
equation.set('')


for i in range(4):
    window.columnconfigure(i, weight=1)
for i in range(8):
    window.rowconfigure(i, weight=1)


button_font = ('Arial', 18)
button_padx = 5
button_pady = 5
button_sticky = "nsew"

# Row 1: Clear
btn_c = tk.Button(window, text="C", font=button_font, bg="#FFA6AB", padx=button_padx, pady=button_pady, command=clear)
btn_c.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky=button_sticky)

# Row 2: 7, 8, 9, /
btn_7 = tk.Button(window, text="7", bg="#9AACFC", font=button_font, command=lambda: press(7))
btn_7.grid(row=2, column=0, padx=5, pady=5, sticky=button_sticky)

btn_8 = tk.Button(window, text="8", bg="#9AACFC", font=button_font, command=lambda: press(8))
btn_8.grid(row=2, column=1, padx=5, pady=5, sticky=button_sticky)

btn_9 = tk.Button(window, text="9", bg="#9AACFC", font=button_font, command=lambda: press(9))
btn_9.grid(row=2, column=2, padx=5, pady=5, sticky=button_sticky)

btn_div = tk.Button(window, text="/", bg="#FFF7BA", font=button_font, command=lambda: press("/"))
btn_div.grid(row=2, column=3, padx=5, pady=5, sticky=button_sticky)

# Row 3: 4, 5, 6, *
btn_4 = tk.Button(window, text="4", bg="#9AACFC", font=button_font, command=lambda: press(4))
btn_4.grid(row=3, column=0, padx=5, pady=5, sticky=button_sticky)

btn_5 = tk.Button(window, text="5", bg="#9AACFC", font=button_font, command=lambda: press(5))
btn_5.grid(row=3, column=1, padx=5, pady=5, sticky=button_sticky)

btn_6 = tk.Button(window, text="6", bg="#9AACFC", font=button_font, command=lambda: press(6))
btn_6.grid(row=3, column=2, padx=5, pady=5, sticky=button_sticky)

btn_mul = tk.Button(window, text="*", bg="#FFF7BA", font=button_font, command=lambda: press("*"))
btn_mul.grid(row=3, column=3, padx=5, pady=5, sticky=button_sticky)

# Row 4: 1, 2, 3, -
btn_1 = tk.Button(window, text="1", bg="#9AACFC", font=button_font, command=lambda: press(1))
btn_1.grid(row=4, column=0, padx=5, pady=5, sticky=button_sticky)

btn_2 = tk.Button(window, text="2", bg="#9AACFC", font=button_font, command=lambda: press(2))
btn_2.grid(row=4, column=1, padx=5, pady=5, sticky=button_sticky)

btn_3 = tk.Button(window, text="3", bg="#9AACFC", font=button_font, command=lambda: press(3))
btn_3.grid(row=4, column=2, padx=5, pady=5, sticky=button_sticky)

btn_sub = tk.Button(window, text="-", bg="#FFF7BA", font=button_font, command=lambda: press("-"))
btn_sub.grid(row=4, column=3, padx=5, pady=5, sticky=button_sticky)

# Row 5: 0, ., +
btn_0 = tk.Button(window, text="0", bg="#9AACFC", font=button_font, command=lambda: press(0))
btn_0.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky=button_sticky)

btn_dot = tk.Button(window, text=".", bg="#FFF7BA", font=button_font, command=lambda: press("."))
btn_dot.grid(row=5, column=2, padx=5, pady=5, sticky=button_sticky)

btn_add = tk.Button(window, text="+", bg="#FFF7BA", font=button_font, command=lambda: press("+"))
btn_add.grid(row=5, column=3, padx=5, pady=5, sticky=button_sticky)

# Row 6: Square Root, sin, cos, tan
btn_sqrt = tk.Button(window, text="√", bg="#C1AFE0", font=button_font, command=calculate_sqrt)
btn_sqrt.grid(row=6, column=0, padx=5, pady=5, sticky=button_sticky)

btn_sin = tk.Button(window, text="sin", bg="#C1AFE0", font=button_font, command=lambda: calculate_trig("sin"))
btn_sin.grid(row=6, column=1, padx=5, pady=5, sticky=button_sticky)

btn_cos = tk.Button(window, text="cos", bg="#C1AFE0", font=button_font, command=lambda: calculate_trig("cos"))
btn_cos.grid(row=6, column=2, padx=5, pady=5, sticky=button_sticky)

btn_tan = tk.Button(window, text="tan", bg="#C1AFE0", font=button_font, command=lambda: calculate_trig("tan"))
btn_tan.grid(row=6, column=3, padx=5, pady=5, sticky=button_sticky)

# Row 7: Equals
btn_eq = tk.Button(window, text="=", bg="#D3F0C5", font=button_font, command=equalpress)
btn_eq.grid(row=7, column=0, columnspan=4, padx=5, pady=5, sticky=button_sticky)

window.mainloop()
