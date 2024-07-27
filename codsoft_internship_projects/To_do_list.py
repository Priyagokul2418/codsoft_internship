import tkinter as tk
from tkinter import messagebox

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to remove the selected task
def remove_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to remove.")

# Function to clear all tasks
def clear_all_tasks():
    tasks_listbox.delete(0, tk.END)

# Create the main window
app = tk.Tk()
app.title("To-Do List App")

# Create and place widgets
frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

task_entry = tk.Entry(frame, width=40)
task_entry.pack(side=tk.LEFT, padx=(0, 10))

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

remove_button = tk.Button(frame, text="Remove Task", command=remove_task)
remove_button.pack(side=tk.LEFT)

clear_button = tk.Button(frame, text="Clear All", command=clear_all_tasks)
clear_button.pack(side=tk.LEFT)

tasks_listbox = tk.Listbox(app, width=50, height=15)
tasks_listbox.pack(padx=10, pady=(0, 10))

# Start the application
app.mainloop()
