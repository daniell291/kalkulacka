import tkinter as tk
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

root=tk.Tk()
root.title("Kalkulačka")
root.iconbitmap(resource_path('ikona.ico')) 
root.geometry("300x385")
example=""
text=""
result=0
display_text = tk.StringVar(value="0")
display_text2 = tk.StringVar(value="")

label = tk.Label(root, textvariable=display_text2, font=("arial",15),)
label.pack(padx=20, pady=0)

label = tk.Label(root, textvariable=display_text, font=("arial", 35),)
label.pack(padx=20, pady=0)

def reset_text(input_text):
    global example
    global text
    example+=input_text
    text=""
    display_text.set(input_text)
    display_text.set("0")
    display_text2.set(example)

def add_text(input_text):
    global example
    global text
    example+=input_text
    text+=input_text
    display_text.set(text)
    display_text2.set(example)

def CE():
    global example
    global text
    global result
    example=""
    text=""
    result=0
    display_text.set("0")
    display_text2.set("")

def equals():
    global result
    global example
    if not example.endswith("+") or example.endswith("-") or example.endswith("*") or example.endswith("/"):
        result=eval(example)
        display_text.set(result)

def klick_1(): add_text("1")
def klick_2(): add_text("2")
def klick_3(): add_text("3")
def klick_4(): add_text("4")
def klick_5(): add_text("5")
def klick_6(): add_text("6")
def klick_7(): add_text("7")
def klick_8(): add_text("8")
def klick_9(): add_text("9")
def klick_0(): add_text("0")
def klick_plus(): reset_text("+")
def klick_minus(): reset_text("-")
def klick_times(): reset_text("*")
def klick_devide(): reset_text("/")

buttonframe=tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=("arial", 18), command=klick_1, bg="lightgray")
btn1.grid(row=0, column=0, sticky=tk.W+tk.E, pady=5, padx=5)

btn2 = tk.Button(buttonframe, text="2", font=("arial", 18), command=klick_2, bg="lightgray")
btn2.grid(row=0, column=1, sticky=tk.W+tk.E, pady=5, padx=5)

btn3 = tk.Button(buttonframe, text="3", font=("arial", 18), command=klick_3, bg="lightgray")
btn3.grid(row=0, column=2, sticky=tk.W+tk.E, pady=5, padx=5)

btn4 = tk.Button(buttonframe, text="4", font=("arial", 18), command=klick_4, bg="lightgray")
btn4.grid(row=1, column=0, sticky=tk.W+tk.E, pady=5, padx=5)

btn5 = tk.Button(buttonframe, text="5", font=("arial", 18), command=klick_5, bg="lightgray")
btn5.grid(row=1, column=1, sticky=tk.W+tk.E, pady=5, padx=5)

btn6 = tk.Button(buttonframe, text="6", font=("arial", 18), command=klick_6, bg="lightgray")
btn6.grid(row=1, column=2, sticky=tk.W+tk.E, pady=5, padx=5)

btn7 = tk.Button(buttonframe, text="7", font=("arial", 18), command=klick_7, bg="lightgray")
btn7.grid(row=2, column=0, sticky=tk.W+tk.E, pady=5, padx=5)

btn8 = tk.Button(buttonframe, text="8", font=("arial", 18), command=klick_8, bg="lightgray")
btn8.grid(row=2, column=1, sticky=tk.W+tk.E, pady=5, padx=5)

btn9 = tk.Button(buttonframe, text="9", font=("arial", 18), command=klick_9, bg="lightgray")
btn9.grid(row=2, column=2, sticky=tk.W+tk.E, pady=5, padx=5)

btn0 = tk.Button(buttonframe, text="0", font=("arial", 18), command=klick_0, bg="lightgray")
btn0.grid(row=3, column=1, sticky=tk.W+tk.E, pady=5, padx=5)

btn_plus = tk.Button(buttonframe, text="+", font=("arial", 18) , command=klick_plus, bg="lightblue")
btn_plus.grid(row=3, column=3, sticky=tk.W+tk.E, pady=5, padx=5,)

btn_minus = tk.Button(buttonframe, text="-", font=("arial", 18), command=klick_minus, bg="lightblue")
btn_minus.grid(row=2, column=3, sticky=tk.W+tk.E, pady=5, padx=5)

btn_times = tk.Button(buttonframe, text="×", font=("arial", 18), command=klick_times,bg="lightblue")
btn_times.grid(row=1, column=3, sticky=tk.W+tk.E, pady=5, padx=5)

btn_devide = tk.Button(buttonframe, text="÷", font=("arial", 18), command=klick_devide,bg="lightblue")
btn_devide.grid(row=0, column=3, sticky=tk.W+tk.E, pady=5, padx=5)

btn_equal = tk.Button(buttonframe, text="=", font=("arial", 18), command=equals, bg="orange")
btn_equal.grid(row=3, column=2, sticky=tk.W+tk.E, pady=5, padx=5)

btn_ce = tk.Button(buttonframe, text="CE", font=("arial", 18), command=CE, bg="blue")
btn_ce.grid(row=3, column=0, sticky=tk.W+tk.E, pady=5, padx=5)
buttonframe.pack(fill="x")

textbox=tk.Text(root, height=2,font=("arial", 16), bg="lightgray")
textbox.pack(padx=10, pady=10)

root.mainloop()