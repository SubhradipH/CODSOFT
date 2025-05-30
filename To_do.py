import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from datetime import datetime

class To_do:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal To-Do List")
        self.root.geometry("700x400")
        self.root.configure(bg="#f0f4f7")  # Light background color

        self.tasks = []  # Initialize task list

        # Treeview styling
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#e6f2ff",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#e6f2ff")
        style.map('Treeview', background=[('selected', '#3399ff')])

        # Treeview setup
        self.tree = ttk.Treeview(root, columns=('Task', 'Due Date', 'Priority', 'Status'), show='headings')
        self.tree.heading('Task', text='Task')
        self.tree.heading('Due Date', text='Due Date')
        self.tree.heading('Priority', text='Priority')
        self.tree.heading('Status', text='Status')
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Button frame
        frame = tk.Frame(root, bg="#f0f4f7")
        frame.pack(pady=10)

        # Colored buttons
        self.create_colored_button(frame, " Add Task", "#28a745", self.add_task, 0)
        self.create_colored_button(frame, " Mark Completed", "#17a2b8", self.mark_completed, 1)
        self.create_colored_button(frame, " Delete Task", "#dc3545", self.delete_task, 2)
        self.create_colored_button(frame, " Exit", "#6c757d", root.quit, 3)

    def create_colored_button(self, parent, text, color, command, column):
        button = tk.Button(parent, text=text, command=command,
                           bg=color, fg="white", font=("Arial", 10, "bold"), padx=10, pady=5)
        button.grid(row=0, column=column, padx=5)

    def add_task(self):
        task = simpledialog.askstring("Task", "Enter Task:")
        if not task:
            return

        due_date = simpledialog.askstring("Due Date", "Enter Due Date (DD/MM/YYYY):")
        try:
            if due_date:
                # Validate format
                datetime.strptime(due_date, "%d/%m/%Y")
        except ValueError:
            messagebox.showerror("Invalid Date", "Enter date in DD/MM/YYYY format.")
            return

        priority = simpledialog.askstring("Priority", "Enter Priority (High/Medium/Low):")
        if priority:
            priority = priority.capitalize()

        self.tasks.append([task, due_date, priority, "Pending"])
        self.tree.insert('', tk.END, values=(task, due_date, priority, "Pending"))

    def mark_completed(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Select Task", "Please select a task to mark as completed.")
            return

        for item in selected_item:
            values = self.tree.item(item, "values")
            self.tree.item(item, values=(values[0], values[1], values[2], "Completed"))

    def delete_task(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Select Task", "Please select a task to delete.")
            return

        for item in selected_item:
            self.tree.delete(item)

# Main run
if __name__ == "__main__":
    root = tk.Tk()
    app = To_do(root)
    root.mainloop()
