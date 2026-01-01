import tkinter as tk
import math

root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

expression = ""

def press(value):
    global expression
    expression += str(value)
    display.set(expression)

def clear():
    global expression
    expression = ""
    display.set("")

def backspace():
    global expression
    expression = expression[:-1]
    display.set(expression)

def calculate():
    global expression
    try:
        result = eval(expression)
        expression = str(result)
        display.set(expression)
    except:
        display.set("Error")
        expression = ""

def square():
    global expression
    try:
        expression = str(eval(expression) ** 2)
        display.set(expression)
    except:
        display.set("Error")
        expression = ""

def sqrt():
    global expression
    try:
        expression = str(math.sqrt(eval(expression)))
        display.set(expression)
    except:
        display.set("Error")
        expression = ""

display = tk.StringVar()

entry = tk.Entry(
    root, textvariable=display,
    font=("Segoe UI", 22),
    bg="#252526", fg="white",
    bd=0, justify="right"
)
entry.pack(fill="x", padx=20, pady=20, ipady=15)

btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(expand=True, fill="both")

buttons = [
    ("C", clear), ("⌫", backspace), ("(", lambda: press("(")), (")", lambda: press(")")),
    ("7", lambda: press(7)), ("8", lambda: press(8)), ("9", lambda: press(9)), ("/", lambda: press("/")),
    ("4", lambda: press(4)), ("5", lambda: press(5)), ("6", lambda: press(6)), ("*", lambda: press("*")),
    ("1", lambda: press(1)), ("2", lambda: press(2)), ("3", lambda: press(3)), ("-", lambda: press("-")),
    ("0", lambda: press(0)), (".", lambda: press(".")), ("+", lambda: press("+")), ("=", calculate),
    ("x²", square), ("√x", sqrt)
]

row = col = 0
for text, cmd in buttons:
    btn = tk.Button(
        btn_frame, text=text, command=cmd,
        font=("Segoe UI", 14),
        bg="#333333", fg="white",
        bd=0, activebackground="#555555"
    )
    btn.grid(row=row, column=col, sticky="nsew", padx=6, pady=6)
    col += 1
    if col == 4:
        col = 0
        row += 1

for i in range(4):
    btn_frame.columnconfigure(i, weight=1)
for i in range(6):
    btn_frame.rowconfigure(i, weight=1)

root.mainloop()
