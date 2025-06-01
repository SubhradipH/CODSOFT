import tkinter as tk
from tkinter import messagebox
import string
import random

def gen_pass():
    try:
        length=int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4")

        all_chars=string.ascii_letters+string.digits+string.punctuation
        password=[
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation),
        ]
        password+=random.choices(all_chars,k=length-4)
        random.shuffle(password)
        generated_password.set(''.join(password))
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

root = tk.Tk()
root.title(" Password Generator")
root.geometry("400x200")
root.resizable(False, False)
root.configure(bg="#70b1ea")  

frame = tk.Frame(root, bg="#cc8cee")
frame.pack(pady=15)


tk.Label(frame, text="Password Length:", font=("Helvetica", 12, "bold"), bg="#cc8cee", fg="#333").pack(side=tk.LEFT, padx=10)
length_entry = tk.Entry(frame, width=10, font=("Helvetica", 12))
length_entry.pack(side=tk.LEFT)


tk.Button(root, text="Generate Password", command=gen_pass,
          bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"),
          activebackground="#45a049", padx=10, pady=5).pack(pady=10)


generated_password = tk.StringVar()
output_entry = tk.Entry(root, textvariable=generated_password,
                        font=("Courier", 14, "bold"), width=30,
                        justify='center', bg="#fffacd", fg="#00008b")
output_entry.pack(pady=10)

root.mainloop()