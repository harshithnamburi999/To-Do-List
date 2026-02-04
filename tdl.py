import tkinter as tk
from tkinter import messagebox
tasks = []
status = []
root = tk.Tk()
root.title("To-Do List App")
root.geometry("800x600")   # BIG window size
def add_task():
    task = entry.get()
    if task == "":
        messagebox.showwarning("Warning", "Please enter a task")
    else:
        tasks.append(task)
        status.append("Pending")
        listbox.insert(tk.END, task + " - Pending")
        entry.delete(0, tk.END)
def mark_completed():
    try:
        index = listbox.curselection()[0]
        status[index] = "Completed"
        listbox.delete(index)
        listbox.insert(index, tasks[index] + " - Completed")
    except:
        messagebox.showwarning("Warning", "Please select a task")
def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        tasks.pop(index)
        status.pop(index)
    except:
        messagebox.showwarning("Warning", "Please select a task")
title_font = ("Arial", 26, "bold")
text_font = ("Arial", 16)
button_font = ("Arial", 14, "bold")
label = tk.Label(root, text="To-Do List", font=title_font)
label.pack(pady=20)
entry = tk.Entry(root, width=35, font=text_font)
entry.pack(pady=10)
entry.focus()
add_btn = tk.Button(root, text="Add Task", width=25, height=2,
                    font=button_font, command=add_task)
add_btn.pack(pady=8)
complete_btn = tk.Button(root, text="Mark as Completed", width=25, height=2,
                         font=button_font, command=mark_completed)
complete_btn.pack(pady=8)
delete_btn = tk.Button(root, text="Delete Task", width=25, height=2,
                       font=button_font, command=delete_task)
delete_btn.pack(pady=8)
listbox = tk.Listbox(root, width=50, height=10, font=text_font)
listbox.pack(pady=20)
root.mainloop()
