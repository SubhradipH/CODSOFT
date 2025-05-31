import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
        else:
            messagebox.showerror("Error", "Please select a valid operation.")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Calculator")
root.geometry("350x300")
root.configure(bg="#278ac7")

label_font = ("Arial", 12, "bold")
entry_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")

tk.Label(root, text="Enter first number:", font=label_font, bg="#f0fff6").pack(pady=5)
entry1 = tk.Entry(root, font=entry_font, bg="#e6f7ff", fg="black")
entry1.pack(pady=5)

tk.Label(root, text="Enter second number:", font=label_font, bg="#f0f8ff").pack(pady=5)
entry2 = tk.Entry(root, font=entry_font, bg="#e6f7ff", fg="black")
entry2.pack(pady=5)

tk.Label(root, text="Choose operation:", font=label_font, bg="#f0f8ff").pack(pady=5)
operation_var = tk.StringVar()
operation_var.set('+')
operations_menu = tk.OptionMenu(root, operation_var, '+', '-', '*', '/')
operations_menu.config(font=entry_font, bg="#ccf2ff", fg="black", width=10)
operations_menu.pack(pady=5)

tk.Button(root, text="Calculate", command=calculate, font=button_font,
          bg="#66ccff", fg="white", activebackground="#3399ff", width=15).pack(pady=10)


result_label = tk.Label(root, text="Result:", font=("Arial", 14, "bold"), bg="#2d81c9", fg="blue")
result_label.pack(pady=10)

root.mainloop()