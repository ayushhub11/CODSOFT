import tkinter as tk
from tkinter import messagebox, simpledialog

# App Setup
root = tk.Tk()
root.title("My To-Do List")
root.geometry("400x500")
root.resizable(False, False)
root.config(bg="#fdf6fd")

# Global Task List
tasks = []

# Functions
def update_display():
    task_listbox.delete(0, tk.END)
    for i, t in enumerate(tasks):
        task_listbox.insert(tk.END, f"{i + 1}. {t}")

def add_task(event=None):
    task = task_entry.get().strip()
    if task:
        tasks.append(task)
        update_display()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Task", "Please type something to add.")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        for index in reversed(selected):
            tasks.pop(index)
        update_display()
    else:
        messagebox.showwarning("No Task", "Select one or more tasks to delete.")

def edit_task():
    selected = task_listbox.curselection()
    if selected:
        if len(selected) > 1:
            messagebox.showinfo("Multiple Selected", "Please select only one task to edit.")
            return
        index = selected[0]
        old_task = tasks[index]
        new_task = simpledialog.askstring("Edit Task", "Update your task:", initialvalue=old_task)
        if new_task and new_task.strip():
            tasks[index] = new_task.strip()
            update_display()
    else:
        messagebox.showinfo("No Selection", "Please select a task to edit.")

def clear_tasks():
    if tasks:
        if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
            tasks.clear()
            update_display()

# GUI Layout
tk.Label(root, text="To-Do List", font=("Segoe UI", 20, "bold"), bg="#fdf6fd", fg="#5c2e91").pack(pady=10)

task_entry = tk.Entry(root, font=("Segoe UI", 14), width=25, bd=2)
task_entry.pack(pady=10)
task_entry.bind("<Return>", add_task)

btn_frame = tk.Frame(root, bg="#fdf6fd")
btn_frame.pack()

tk.Button(btn_frame, text="Add", font=("Segoe UI", 12), width=10, bg="#b57edc", fg="white", command=add_task).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Edit", font=("Segoe UI", 12), width=10, bg="#dbb6ee", fg="black", command=edit_task).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", font=("Segoe UI", 12), width=10, bg="#f7ebfd", fg="black", command=delete_task).grid(row=1, column=0, padx=5)
tk.Button(btn_frame, text="Clear All", font=("Segoe UI", 12), width=10, bg="#ffe4f7", fg="black", command=clear_tasks).grid(row=1, column=1, padx=5)

# Task Listbox with Multi-Selection
task_listbox = tk.Listbox(root, font=("Segoe UI", 13), width=32, height=10, 
                          selectbackground="#e9d6f5", fg="black", bg="white", 
                          selectmode=tk.EXTENDED)  # <== MULTI SELECT ENABLED
task_listbox.pack(pady=15)

# Run App
root.mainloop()
