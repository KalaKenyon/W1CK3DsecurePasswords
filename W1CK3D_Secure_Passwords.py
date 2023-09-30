import tkinter as tk
import string
import random

def generate_secure_password(length=18):
    characters = string.ascii_letters + string.digits + string.punctuation
    secure_password = ''.join(random.choice(characters) for _ in range(length))
    return secure_password

def generate_password():
    secure_password.set(generate_secure_password())

# Create the main window
root = tk.Tk()
root.title("Secure Password Generator")

# Create a StringVar to store the generated password
secure_password = tk.StringVar()

# Create a label to display the generated password
password_label = tk.Label(root, textvariable=secure_password, font=("Arial", 14), wraplength=400)
password_label.pack(pady=20)

# Create a button to generate new passwords
generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12))
generate_button.pack()

# Run the main loop
root.mainloop()
