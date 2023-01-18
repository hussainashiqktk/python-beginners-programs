import random
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = int(length_entry.get())
    password = ''.join(random.choices(characters, k=length))
    messagebox.showinfo("Password", password)

root = tk.Tk()
root.title("Password Generator")

label = tk.Label(root, text="Enter the desired length of the password:")
label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

root.mainloop()
