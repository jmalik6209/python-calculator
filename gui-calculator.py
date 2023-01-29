import tkinter as tk
from tkinter import font

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("900x600")

# Set the row and column options for the grid cells
for i in range(5):
    window.columnconfigure(i, weight=1)
for i in range(5):
    window.rowconfigure(i, weight=1)


font_large = font.Font(size=50)
font_medium = font.Font(size=20)

# Create the display
display = tk.Entry(window, width=50, bg="white", font=font_large)
display.grid(row=0, column=0, columnspan=5, sticky="nsew")

# Create the buttons
button_1 = tk.Button(window, text="1", width=5, bg="white", fg="black", font=font_medium)
button_2 = tk.Button(window, text="2", width=5, bg="white", fg="black", font=font_medium)
button_3 = tk.Button(window, text="3", width=5, bg="white", fg="black", font=font_medium)
button_4 = tk.Button(window, text="4", width=5, bg="white", fg="black", font=font_medium)
button_5 = tk.Button(window, text="5", width=5, bg="white", fg="black", font=font_medium)
button_6 = tk.Button(window, text="6", width=5, bg="white", fg="black", font=font_medium)
button_7 = tk.Button(window, text="7", width=5, bg="white", fg="black", font=font_medium)
button_8 = tk.Button(window, text="8", width=5, bg="white", fg="black", font=font_medium)
button_9 = tk.Button(window, text="9", width=5, bg="white", fg="black", font=font_medium)
button_0 = tk.Button(window, text="0", width=5, bg="white", fg="black", font=font_medium)
button_add = tk.Button(window, text="+", width=5, bg="black", fg="white", font=font_medium)
button_subtract = tk.Button(window, text="-", width=5, bg="black", fg="white", font=font_medium)
button_multiply = tk.Button(window, text="*", width=5, bg="black", fg="white", font=font_medium)
button_divide = tk.Button(window, text="/", width=5, bg="black", fg="white", font=font_medium)
button_equal = tk.Button(window, text="=", width=5, bg="black", fg="white", font=font_medium)
button_clear = tk.Button(window, text="Clear", width=5, bg="black", fg="white", font=font_medium)

# Place the buttons in a grid
button_1.grid(row=1, column=0, sticky="nsew")
button_2.grid(row=1, column=1, sticky="nsew")
button_3.grid(row=1, column=2, sticky="nsew")
button_4.grid(row=2, column=0, sticky="nsew")
button_5.grid(row=2, column=1, sticky="nsew")
button_6.grid(row=2, column=2, sticky="nsew")
button_7.grid(row=3, column=0, sticky="nsew")
button_8.grid(row=3, column=1, sticky="nsew")
button_9.grid(row=3, column=2, sticky="nsew")
button_0.grid(row=4, column=0, sticky="nsew")
button_add.grid(row=1, column=3, sticky="nsew")
button_subtract.grid(row=2, column=3, sticky="nsew")
button_multiply.grid(row=3, column=3, sticky="nsew")
button_divide.grid(row=4, column=3, sticky="nsew")
button_equal.grid(row=4, column=2, sticky="nsew")
button_clear.grid(row=4, column=1, sticky="nsew")

# Create the event handlers for the buttons
def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(number))

def button_clear_click():
    display.delete(0, tk.END)

def button_add_click():
    global first_number
    global math
    math = "addition"
    first_number = int(display.get())
    display.delete(0, tk.END)

def button_subtract_click():
    global first_number
    global math
    math = "subtraction"
    first_number = int(display.get())
    display.delete(0, tk.END)

def button_multiply_click():
    global first_number
    global math
    math = "multiplication"
    first_number = int(display.get())
    display.delete(0, tk.END)

def button_divide_click():
    global first_number
    global math
    math = "division"
    first_number = int(display.get())
    display.delete(0, tk.END)

def button_equal_click():
    second_number = int(display.get())
    display.delete(0, tk.END)
    if math == "addition":
        display.insert(0, first_number + second_number)
    if math == "subtraction":
        display.insert(0, first_number - second_number)
    if math == "multiplication":
        display.insert(0, first_number * second_number)
    if math == "division":
        display.insert(0, first_number / second_number)

# Tell the buttons what to do when they are clicked
button_1.config(command=lambda: button_click(1))
button_2.config(command=lambda: button_click(2))
button_3.config(command=lambda: button_click(3))
button_4.config(command=lambda: button_click(4))
button_5.config(command=lambda: button_click(5))
button_6.config(command=lambda: button_click(6))
button_7.config(command=lambda: button_click(7))
button_8.config(command=lambda: button_click(8))
button_9.config(command=lambda: button_click(9))
button_0.config(command=lambda: button_click(0))
button_clear.config(command=button_clear_click)
button_add.config(command=button_add_click)
button_subtract.config(command=button_subtract_click)
button_multiply.config(command=button_multiply_click)
button_divide.config(command=button_divide_click)
button_equal.config(command=button_equal_click)

# Run the main loop
window.mainloop()