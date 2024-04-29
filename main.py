import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    password_length = int(length_entry.get())

    if password_length <= 0:
        password_label.config(text="Invalid length")
        return

    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))
    password_label.config(text="Generated Password: " + password)

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Create label and entry for password length
length_label = ttk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5)

length_entry = ttk.Entry(root)
length_entry.grid(row=0, column=1, padx=5, pady=5)

# Create button to generate password
generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, columnspan=2, padx=5, pady=5)

# Create label to display generated password
password_label = ttk.Label(root, text="")
password_label.grid(row=2, columnspan=2, padx=5, pady=5)

root.mainloop()

