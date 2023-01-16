"""
Here is a simple Python GUI app using the Tkinter library that allows a user to input a string and displays the reversed string:
"""

import tkinter as tk

def reverse_string():
    original = entry.get()
    reversed_string = original[::-1]
    label.config(text = reversed_string)

root = tk.Tk()
root.title("String Reverser")

label = tk.Label(root, text="Enter a string to reverse:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Reverse", command=reverse_string)
button.pack()

root.mainloop()
