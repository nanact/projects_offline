import tkinter as tk

from tkinter import ttk

def answer():
    number1 = numbers1.get()
    number2 = numbers2.get()
    number1 = int(number1)
    number2 = int(number2)
    total = number1 * number2
    solution.config(text = total)
    

window = tk.Tk() 

window.title("mutliplying numbers")

window.geometry("600x400")

label = ttk.Label(text = "mutliplying",font=(1))

label.pack()

label1 = ttk.Label(text = "number1")

label1.pack()

numbers1 = ttk.Entry()

numbers1.pack()

label2 = ttk.Label(text = "number2")

label2.pack()

numbers2 = ttk.Entry()

numbers2.pack()

submit = ttk.Button(text = "submit", command=answer)

submit.pack()

solution = ttk.Label(text = "no answer provide")

solution.pack()

window.mainloop()