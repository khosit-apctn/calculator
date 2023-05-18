from tkinter.constants import END
from tkinter import TOP, X, Button, Label, ttk
import tkinter.messagebox
import tkinter as tk
import math

root = tk.Tk()
root.title("Calculator")
root.geometry("500x500")

equation = ""

def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "Error"
            equation = ""
    label_result.config(text=result)

def cos(x): 
    return math.cos(x)
def sin(x): 
    return math.sin(x)
def tan(x): 
    return math.tan(x)

def openTest():
    myWindow = tk.Tk()
    myWindow.title("KONG")
    myWindow.geometry("200x200")

def exitProgram():
    confirm = tkinter.messagebox.askquestion("Exit Calculator", "Do you want to exit?")
    if confirm == "yes":
        root.destroy()

def aboutProgram():
    tkinter.messagebox.showinfo("Calculator", "This is a simple calculator program.")

subMenu = tk.Menu()
subMenu.add_command(label="New File", command=openTest)
subMenu.add_command(label="Save")
subMenu.add_command(label="Exit",command = exitProgram)

myMenu = tk.Menu()
root.config(menu = myMenu)
myMenu.add_cascade(label="File", menu=subMenu)
myMenu.add_cascade(label="Edit")
myMenu.add_cascade(label="View")

f1 = tk.Frame(root, bg='green')
f1.place(x=0,y=0)
f2 = tk.Frame(root, bg='red')
f2.place(x=1,y=50)
f3 = tk.Frame(root, bg='blue')
f3.place(x=270,y=50)

label_result = Label(f1, width=68, text="", font=("Arial", 9))
label_result.pack(padx=10, pady=10)

tk.Button(f2, text="C", width=30, command=lambda: clear()).pack(fill=X, padx=20, pady=10)
tk.Button(f2, text="+", width=30, command=lambda: show("+")).pack(fill=X, padx=20, pady=10)
tk.Button(f2, text="-", width=30, command=lambda: show("-")).pack(fill=X, padx=20, pady=10)
tk.Button(f2, text="*", width=30, command=lambda: show("*")).pack(fill=X, padx=20, pady=10)
tk.Button(f2, text="/", width=30, command=lambda: show("/")).pack(fill=X, padx=20, pady=10)
tk.Button(f2, text="%", width=30, command=lambda: show("%")).pack(fill=X, padx=20, pady=10)
tk.Button(f2, text="sin", width=30, command=lambda: show("xmath.sin(")).pack(fill=X, padx=20, pady=10)
tk.Button(f2, text="=", width=30, command=lambda: calculate()).pack(fill=X, padx=20, pady=10)

# Create a list of tuples, where each tuple contains the text for the button and its corresponding action command
button_data = [
    ("1", lambda: show("1")),
    ("2", lambda: show("2")),
    ("3", lambda: show("3")),
    ("4", lambda: show("4")),
    ("5", lambda: show("5")),
    ("6", lambda: show("6")),
    ("7", lambda: show("7")),
    ("8", lambda: show("8")),
    ("9", lambda: show("9")),
    ("0", lambda: show("0")),
    (".", lambda: show(".")),
    (")", lambda: show(")")),
    ("(", lambda: show("(")),
]

for i, (x, y) in enumerate(button_data):
    tk.Button(f3, text=x, width=5, height=4, font=("Arial", 10, "bold"), bd=1, fg="#2a2d36", command=y).grid(row=i // 3, column=i % 3, padx=10, pady=10)

root.mainloop()