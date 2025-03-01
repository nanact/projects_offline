import tkinter as tk
from tkinter import messagebox

def convert_to_cm():
    try:
        inches = float(entry_inches.get())
        centimeters = inches * 2.54
        messagebox.showinfo("Result", f"{inches} inches is equal to {centimeters:.2f} cm")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

root = tk.Tk()
root.title("Inches to Centimeters Converter")

tk.Label(root, text="Length in Inches:").grid(row=0, column=0, padx=10, pady=5)
entry_inches = tk.Entry(root)
entry_inches.grid(row=0, column=1, padx=10, pady=5)

button_convert = tk.Button(root, text="Convert", command=convert_to_cm)
button_convert.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
