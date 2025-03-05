import tkinter as tk
from tkinter import StringVar, Button, Entry
import tkinter.font as font

okno = tk.Tk()
okno.title("Calculator")

myFont = font.Font(family='Arial', size=20, weight='bold')

ans_entry = Entry(okno, bd=5, width=20, font=myFont, bg="gray", fg="white")
ans_entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '÷',
    '4', '5', '6', 'x',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

equation = ""

row = 1
col = 0
for button in buttons:
    btn = Button(okno, text=button, padx=20, pady=10, font=myFont)
    btn.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

def calculate(expression):
    try:
        expression = expression.replace('x', '*').replace('÷', '/')
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "ERROR: Division by zero!"
    except:
        return "ERROR"

def mouse_button_release(event):
    global equation

    widg = event.widget
    text = widg.cget("text")

    if text in "0123456789+-x÷":
        equation += text
        ans_entry.delete(0, tk.END)
        ans_entry.insert(0, equation)

    elif text == "C":
        equation = ""
        ans_entry.delete(0, tk.END)

    elif text == "=":
        result = calculate(equation)
        equation = str(result)
        ans_entry.delete(0, tk.END)
        if result == "ERROR" or "ERROR" in str(result):
            equation = ""
        ans_entry.insert(0, str(result))

okno.bind("<ButtonRelease-1>", mouse_button_release)

okno.mainloop()
