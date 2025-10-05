import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength():
    password = entry.get()
    strength_points = 0

    # Length
    if len(password) >= 8: strength_points += 2
    elif len(password) >= 6: strength_points += 1

    # Upper & Lowercase
    if re.search("[a-z]", password) and re.search("[A-Z]", password): strength_points += 2
    elif re.search("[a-zA-Z]", password): strength_points += 1

    # Numbers
    if re.search("[0-9]", password): strength_points += 2

    # Special chars
    if re.search("[@#$%^&*()_+=!<>?/|]", password): strength_points += 2

    # Text & color
    if strength_points <= 3: text, color = "Weak 😕", "red"
    elif strength_points <= 6: text, color = "Medium 😐", "orange"
    else: text, color = "Strong 💪", "green"

    result_label.config(text=f"Strength: {text} ({strength_points}/8)", fg=color)

def toggle_password():
    entry.config(show="" if entry.cget('show') == "*" else "*")

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Checker")
root.geometry("400x250")
root.config(bg="#222")

tk.Label(root, text="🔐 Password Strength Checker", font=("Arial",16,"bold"), bg="#222", fg="white").pack(pady=10)
entry = tk.Entry(root, width=30, font=("Arial",14), show="*")
entry.pack(pady=5)

tk.Button(root, text="Check Strength", bg="#4CAF50", fg="white", command=check_password_strength).pack(pady=5)
tk.Button(root, text="👁️ Show/Hide", bg="#555", fg="white", command=toggle_password).pack(pady=5)
tk.Button(root, text="📋 Copy", bg="#555", fg="white", command=copy_password).pack(pady=5)

tk.Label(root, text="Use: Uppercase, lowercase, numbers, special chars", font=("Arial",10), bg="#222", fg="lightgrey").pack(pady=5)
result_label = tk.Label(root, text="", font=("Arial",14,"bold"), bg="#222")
result_label.pack(pady=10)

root.mainloop()
