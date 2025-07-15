import tkinter as tk
from tkinter import messagebox, filedialog

# Initialize main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("500x700")
root.configure(bg="#f0f0f0")

# Task List
tasks = []

# Functions
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete")

def save_tasks():
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file:
        with open(file, "w") as f:
            for task in tasks:
                f.write(task + "\n")
        messagebox.showinfo("Saved", "Tasks saved successfully!")

def load_tasks():
    file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file:
        with open(file, "r") as f:
            loaded_tasks = f.readlines()
        for task in loaded_tasks:
            cleaned = task.strip()
            if cleaned:
                tasks.append(cleaned)
                listbox.insert(tk.END, cleaned)

# Widgets
title = tk.Label(root, text="To-Do List", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack(pady=10, padx=22, fill=tk.X)

add_btn = tk.Button(root, text="Add Task", command=add_task, font=("Helvetica", 12), bg="#a4d4ae")
add_btn.pack(pady=5)

listbox = tk.Listbox(root, font=("Helvetica", 12), height=8)
listbox.pack(padx=20, pady=8, fill=tk.BOTH, expand=True)

delete_btn = tk.Button(root, text="Delete Task", command=delete_task, font=("Helvetica", 11), bg="#f77c7c")
delete_btn.pack(pady=5)

save_btn = tk.Button(root, text="Save Tasks", command=save_tasks, font=("Helvetica", 11), bg="#c2c2f0")
save_btn.pack(pady=5)

load_btn = tk.Button(root, text="Load Tasks", command=load_tasks, font=("Helvetica", 12), bg="#ffe599")
load_btn.pack(pady=5)

# Run the main event loop
root.mainloop()
