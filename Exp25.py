import tkinter as tk
from tkinter import messagebox

def calculate(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if op == '+':
            result.set(num1 + num2)
        elif op == '-':
            result.set(num1 - num2)
        elif op == '*':
            result.set(num1 * num2)
        elif op == '/':
            result.set(num1 / num2)
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Simple Calculator")

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

for symbol in ['+', '-', '*', '/']:
    tk.Button(root, text=symbol, command=lambda s=symbol: calculate(s)).pack()

root.mainloop()
