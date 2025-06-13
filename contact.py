import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

CONTACT_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, 'r') as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(CONTACT_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

def refresh_list():
    contact_list.delete(0, tk.END)
    for contact in load_contacts():
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone are required.")
        return

    contacts = load_contacts()
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    save_contacts(contacts)
    refresh_list()
    clear_fields()
    messagebox.showinfo("Success", "Contact added!")

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def search_contact():
    query = simpledialog.askstring("Search", "Enter name or phone number:")
    if not query:
        return
    contacts = load_contacts()
    results = [c for c in contacts if query.lower() in c['name'].lower() or query in c['phone']]
    contact_list.delete(0, tk.END)
    for contact in results:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def delete_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Delete", "Please select a contact.")
        return
    selected_text = contact_list.get(selected[0])
    phone = selected_text.split(" - ")[1]
    contacts = load_contacts()
    contacts = [c for c in contacts if c['phone'] != phone]
    save_contacts(contacts)
    refresh_list()
    messagebox.showinfo("Deleted", "Contact deleted.")

def update_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Update", "Please select a contact.")
        return
    selected_text = contact_list.get(selected[0])
    phone = selected_text.split(" - ")[1]
    contacts = load_contacts()
    for contact in contacts:
        if contact['phone'] == phone:
            new_name = simpledialog.askstring("Update", f"Name ({contact['name']}):", initialvalue=contact['name'])
            new_email = simpledialog.askstring("Update", f"Email ({contact['email']}):", initialvalue=contact['email'])
            new_address = simpledialog.askstring("Update", f"Address ({contact['address']}):", initialvalue=contact['address'])
            contact['name'] = new_name or contact['name']
            contact['email'] = new_email or contact['email']
            contact['address'] = new_address or contact['address']
            save_contacts(contacts)
            refresh_list()
            messagebox.showinfo("Updated", "Contact updated.")
            return

# GUI Setup
root = tk.Tk()
root.title("Colorful Contact Manager")
root.geometry("500x550")
root.configure(bg="#f0f8ff")  # Light blue background

# Header
header = tk.Label(root, text="Contact Book", font=("Helvetica", 18, "bold"), bg="#00bcd4", fg="white", pady=10)
header.pack(fill=tk.X)

# Input Section
frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=10)

def make_label(text):
    return tk.Label(frame, text=text, bg="#f0f8ff", fg="#333", font=("Arial", 10, "bold"))

make_label("Name:").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(frame, width=40)
name_entry.grid(row=0, column=1, padx=5, pady=5)

make_label("Phone:").grid(row=1, column=0, sticky="w")
phone_entry = tk.Entry(frame, width=40)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

make_label("Email:").grid(row=2, column=0, sticky="w")
email_entry = tk.Entry(frame, width=40)
email_entry.grid(row=2, column=1, padx=5, pady=5)

make_label("Address:").grid(row=3, column=0, sticky="w")
address_entry = tk.Entry(frame, width=40)
address_entry.grid(row=3, column=1, padx=5, pady=5)

# Buttons
btn_frame = tk.Frame(root, bg="#f0f8ff")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Contact", command=add_contact, bg="#4caf50", fg="white", width=15).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Search", command=search_contact, bg="#2196f3", fg="white", width=15).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Update", command=update_contact, bg="#ff9800", fg="white", width=15).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Delete", command=delete_contact, bg="#f44336", fg="white", width=15).grid(row=1, column=1, padx=5, pady=5)

# Contact List
tk.Label(root, text="Saved Contacts", bg="#f0f8ff", font=("Arial", 12, "bold")).pack(pady=5)
contact_list = tk.Listbox(root, width=60, height=10, bg="#ffffff", fg="#000000", font=("Courier", 10))
contact_list.pack(padx=10, pady=5)

# Footer
tk.Label(root, text="Developed with ♥ in Python", bg="#f0f8ff", fg="#555", font=("Arial", 9, "italic")).pack(side="bottom", pady=10)

# Initialize
refresh_list()
root.mainloop()
