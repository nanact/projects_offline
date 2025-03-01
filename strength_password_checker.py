import tkinter as tk
from tkinter import messagebox

def check_password_strength():
    password = entry.get()
    length = len(password)
    
    if length == 0:
        strength = "No password entered"
    elif length < 6:
        strength = "Weak"
    elif 6 <= length < 10:
        strength = "Moderate"
    else:
        strength = "Strong"
    
    label_result.config(text=f"Password Strength: {strength}")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x200")

label = tk.Label(root, text="Enter Password:")
label.pack(pady=10)

entry = tk.Entry(root, show="*", width=30)
entry.pack()

button = tk.Button(root, text="Check Strength", command=check_password_strength)
button.pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
