import tkinter as tk
from tkinter import messagebox, simpledialog
import json

# Global dictionary to store contacts
contacts = {}

def load_contacts():
    global contacts
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}

def save_contacts():
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)

def add_contact():
    name = simpledialog.askstring("Input", "Enter the contact's name:")
    if name:
        phone = simpledialog.askstring("Input", "Enter the contact's phone number:")
        email = simpledialog.askstring("Input", "Enter the contact's email:")
        address = simpledialog.askstring("Input", "Enter the contact's address:")
        
        contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        save_contacts()
        messagebox.showinfo("Success", "Contact added successfully.")
        update_contact_list()

def view_contacts():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name} - {details['phone']}")

def search_contact():
    search_term = simpledialog.askstring("Input", "Enter the name to search:")
    if search_term:
        contact_list.delete(0, tk.END)
        found = False
        for name, details in contacts.items():
            if search_term.lower() in name.lower():
                contact_list.insert(tk.END, f"Name: {name}")
                contact_list.insert(tk.END, f"Phone: {details['phone']}")
                contact_list.insert(tk.END, f"Email: {details['email']}")
                contact_list.insert(tk.END, f"Address: {details['address']}")
                contact_list.insert(tk.END, "")
                found = True
        if not found:
            contact_list.insert(tk.END, "No contact found.")

def update_contact():
    name = simpledialog.askstring("Input", "Enter the name of the contact to update:")
    if name in contacts:
        phone = simpledialog.askstring("Input", f"Enter new phone number (current: {contacts[name]['phone']}):")
        email = simpledialog.askstring("Input", f"Enter new email (current: {contacts[name]['email']}):")
        address = simpledialog.askstring("Input", f"Enter new address (current: {contacts[name]['address']}):")
        
        contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        save_contacts()
        messagebox.showinfo("Success", "Contact updated successfully.")
        update_contact_list()
    else:
        messagebox.showwarning("Not Found", "Contact not found.")

def delete_contact():
    name = simpledialog.askstring("Input", "Enter the name of the contact to delete:")
    if name in contacts:
        del contacts[name]
        save_contacts()
        messagebox.showinfo("Success", "Contact deleted successfully.")
        update_contact_list()
    else:
        messagebox.showwarning("Not Found", "Contact not found.")

def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name} - {details['phone']}")

# Create the main window
root = tk.Tk()
root.title("Contact Book")

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Create buttons for each function
tk.Button(button_frame, text="Add Contact", command=add_contact).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="View Contacts", command=view_contacts).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Search Contact", command=search_contact).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Update Contact", command=update_contact).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Delete Contact", command=delete_contact).pack(side=tk.LEFT, padx=5)

# Create a listbox to display contacts
contact_list = tk.Listbox(root, width=50, height=15)
contact_list.pack(padx=10, pady=10)

# Load contacts and initialize the contact list
load_contacts()
update_contact_list()

# Start the Tkinter event loop
root.mainloop()

