# from tkinter.constants import Font,LEFT
import math
from tkinter import TOP, X, Button, Label, ttk
from math import sin, cos, tan, pi
import tkinter.messagebox
import tkinter as tk
import re

# ปุ่มแสดง

root = tk.Tk()
root.title("My GUI")
root.geometry("500x500")
root.configure(background='#31456e')
# root.mainloop()
equation = ""


def showmesage():
    print("KongCal")
    #ylabel = Label(root,text = "hello world", fg = "red", bg = "blue").place(x = 300, y=100)


def newWindow():
    myWindow = tk.Tk()
    myWindow.title("test")
    myWindow.geometry("200x200")


def openTest():
    myWindow = tk.Tk()
    myWindow.title("test")
    myWindow.geometry("200x200")

# message BOx


def aboutProgram():
    tkinter.messagebox.showinfo("info", "KongCal")

# exist program


def exitProgram():
    confirm = tkinter.messagebox.askquestion("ok", "do you want to extis?")
    if confirm == "yes":
        root.destroy()


def openTest():
    myWindow = tk.Tk()
    myWindow.title("test")
    myWindow.geometry("200x200")


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

        if "sin(" in equation:
            a = equation.find('sin(')
            sinn = equation[a:] + equation[:a]
            num = sinn
            res = re.findall('\d+', num)
            num2 = (str(res))
            result = ''.join([i for i in num2 if i.isdigit()])
            print(str(result))
            sinn2 = 'math.sin(math.radians(float(' + result + ')))'
            equation = sinn2
            print(equation)
            result = eval(equation)
            print(result)
            label_result.config(text=result)

        if "cos(" in equation:
            a = equation.find('cos(')
            cos = equation[a:] + equation[:a]
            num = cos
            res = re.findall('\d+', num)
            num2 = (str(res))
            result = ''.join([i for i in num2 if i.isdigit()])
            print(str(result))
            cos2 = 'math.cos(math.radians(float(' + result + ')))'
            equation = cos2
            print(equation)
            result = eval(equation)
            print(result)
            label_result.config(text=result)

        if "tan(" in equation:
            a = equation.find('tan(')
            tan = equation[a:] + equation[:a]
            num = tan
            res = re.findall('\d+', num)
            num2 = (str(res))
            result = ''.join([i for i in num2 if i.isdigit()])
            print(str(result))
            tan2 = 'math.tan(math.radians(float(' + result + ')))'
            equation = tan2
            print(equation)
            result = eval(equation)
            print(result)
            label_result.config(text=result)

        if "sinh(" in equation:
            a = equation.find('sinh(')
            sinh = equation[a:] + equation[:a]
            num = sinh
            res = re.findall('\d+', num)
            num2 = (str(res))
            result = ''.join([i for i in num2 if i.isdigit()])
            print(str(result))
            sinh2 = 'math.sinh(math.radians(float(' + result + ')))'
            equation = sinh2
            print(equation)
            result = eval(equation)
            print(result)
            label_result.config(text=result)

        if "cosh(" in equation:
            a = equation.find('cosh(')
            cosh = equation[a:] + equation[:a]
            num = cosh
            res = re.findall('\d+', num)
            num2 = (str(res))
            result = ''.join([i for i in num2 if i.isdigit()])
            print(str(result))
            cosh2 = 'math.cosh(math.radians(float(' + result + ')))'
            equation = cosh2
            print(equation)
            result = eval(equation)
            print(result)
            label_result.config(text=result)

        if "tanh(" in equation:
            a = equation.find('tanh(')
            tanh = equation[a:] + equation[:a]
            num = tanh
            res = re.findall('\d+', num)
            num2 = (str(res))
            result = ''.join([i for i in num2 if i.isdigit()])
            print(str(result))
            tanh2 = 'math.tanh(math.radians(float(' + result + ')))'
            equation = tanh2
            print(equation)
            result = eval(equation)
            print(result)
            label_result.config(text=result)

        if "pi" in equation:
            a = equation.find('pi')
            tanh = equation[a:] + equation[:a]
            num = tanh
            res = re.findall('\d+', num)
            num2 = (str(res))
            result = ''.join([i for i in num2 if i.isdigit()])
            print(str(result))
            tanh2 = 'math.pi *(' + result + ')'
            if tanh2 == "math.pi *()":
                if "math.pi *()" in equation:
                    equation = tanh2
            try:
                tanh2 = 'math.pi'
                result = eval(equation)
                print(result)
                label_result.config(text=result)
            except:
                tanh2 = 'math.pi *(' + result + ')'
                equation = tanh2
                print(equation)
                result = eval(equation)
                print(result)
                label_result.config(text=result)

        if "log" in equation:
            a = equation.find('log')
            log = equation[a:] + equation[:a]
            num = log
            res = re.findall('\d+', num)
            num2 = (str(res))
            result = ''.join([i for i in num2 if i.isdigit()])
            print(str(result))
            log2 = 'math.log(float(' + result + '))'
            equation = log2
            print(equation)
            result = eval(equation)
            print(result)
            label_result.config(text=result)

    try:
        result = eval(equation)
    except:
        result = "Error"
        equation = ""
    label_result.config(text=result)

    

# ช่องคำตอบ
label_result = Label(root, width=54, height=3, text="", font=(45))
label_result.pack()

# เครื่องคิดเลข

subMenu = tk.Menu()
subMenu.add_command(label="new file", command=openTest)
subMenu.add_command(label="save")
subMenu.add_command(label="exist", command=exitProgram)


myMenu = tk.Menu()
root.config(menu=myMenu)
myMenu.add_cascade(label="file", menu=subMenu)

myMenu.add_cascade(label="edit")
myMenu.add_cascade(label="view")


f1 = tk.Frame(root, bg='#31456e')
f1.place(x=0, y=0)
f2 = tk.Frame(root, bg='#366e31')
f2.place(x=1, y=70)
f3 = tk.Frame(root, bg='#6e3131')
f3.place(x=283, y=70)




for c in ['C']:
    tk.Button(f2, text=c, width=10, height=3, command=lambda: clear()
              ).grid(row=0, column=0, padx=10, pady=10)

for c in ['+']:
    tk.Button(f2, text=c, width=8, height=3, command=lambda: show(
        "+")).grid(row=1, column=2, padx=10, pady=10)

for c in ['-']:
    tk.Button(f2, text=c, width=8, height=3, command=lambda: show(
        "-")).grid(row=0, column=2, padx=10, pady=10)

for c in ['x']:
    tk.Button(f2, text=c, width=8, height=3, command=lambda: show(
        "*")).grid(row=1, column=0, padx=10, pady=10)

for c in ['%']:
    tk.Button(f2, text=c, width=8, height=3, command=lambda: show(
        "/")).grid(row=1, column=1, padx=10, pady=10)

for c in ['=']:
    tk.Button(f2, text=c, width=8, height=3, command=lambda: calculate()
              ).grid(row=0, column=1, padx=10, pady=10)


for c in ['sin']:
    tk.Button(f2, text=c, width=8, height=3, command=lambda: show("sin(")).grid(
        row=2, column=0, padx=10, pady=10)

for c in ['cos']:
    tk.Button(f2, text=c, width=8, height=3, command=lambda: show("cos(")).grid(
        row=2, column=1, padx=10, pady=10)
for c in ['tan']:
    tk.Button(f2, text=c, width=8, height=3, command=lambda: show("tan(")).grid(
        row=2, column=2, padx=10, pady=10)

for c in ['sinh']:
    tk.Button(f2, text=c, width=8, height=3, command=lambda: show("sinh(")).grid(
        row=3, column=0, padx=10, pady=10)
for c in ['cosh']:
    tk.Button(f2, text=c, width=8, height=3, command=lambda: show("cosh(")).grid(
        row=3, column=1, padx=10, pady=10)
for c in ['tanh']:
    tk.Button(f2, text=c, width=8, height=3, command=lambda: show("tanh(")).grid(
        row=3, column=2, padx=10, pady=10)

for c in ['pi']:
    tk.Button(f2, text=c, width=8, height=3, command=lambda: show("pi")).grid(
        row=4, column=0, padx=10, pady=10)
for c in ['log']:
    tk.Button(f2, text=c, width=8, height=3, command=lambda: show("log")).grid(
        row=4, column=1, padx=10, pady=10)


for i, c in enumerate("1"):
    tk.Button(f3, text=c, width=6, height=3, command=lambda: show("1")).grid(
        row=0, column=0, padx=10, pady=10)

for i, c in enumerate("2"):
    tk.Button(f3, text=c, width=6, height=3, command=lambda: show("2")).grid(
        row=0, column=1, padx=10, pady=10)

for i, c in enumerate("3"):
    tk.Button(f3, text=c, width=6, height=3, command=lambda: show("3")).grid(
        row=0, column=2, padx=10, pady=10)

for i, c in enumerate("4"):
    tk.Button(f3, text=c, width=6, height=3, command=lambda: show("4")).grid(
        row=1, column=0, padx=10, pady=10)

for i, c in enumerate("5"):
    tk.Button(f3, text=c, width=6, height=3, command=lambda: show("5")).grid(
        row=1, column=1, padx=10, pady=10)

for i, c in enumerate("6"):
    tk.Button(f3, text=c, width=6, height=3, command=lambda: show("6")).grid(
        row=1, column=2, padx=10, pady=10)

for i, c in enumerate("7"):
    tk.Button(f3, text=c, width=6, height=3, command=lambda: show("7")).grid(
        row=2, column=0, padx=10, pady=10)

for i, c in enumerate("8"):
    tk.Button(f3, text=c, width=6, height=3, command=lambda: show("8")).grid(
        row=2, column=1, padx=10, pady=10)

for i, c in enumerate("9"):
    tk.Button(f3, text=c, width=6, height=3, command=lambda: show("9")).grid(
        row=2, column=2, padx=10, pady=10)

for i, c in enumerate("0"):
    tk.Button(f3, text=c, width=6, height=3, command=lambda: show("0")).grid(
        row=3, column=1, padx=10, pady=10)

for i, c in enumerate("."):
    tk.Button(f3, text=c, width=6, height=3, command=lambda: show(".")).grid(
        row=3, column=2, padx=10, pady=10)

for i, c in enumerate(")"):
    tk.Button(f3, text=c, width=6, height=3, command=lambda: show(")")).grid(
        row=3, column=0, padx=10, pady=10)
for i, c in enumerate("("):
    tk.Button(f3, text=c, width=6, height=3, command=lambda: show("(")).grid(
        row=4, column=0, padx=10, pady=10)

root.mainloop()
