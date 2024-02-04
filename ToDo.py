import tkinter as tk
from tkinter import messagebox
import random

def add_task():
    task = e1.get()
    if task:
        listbox.insert(tk.END, task)
        e1.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def rem_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def delete():
    listbox.delete(0, tk.END)

def select_random():
    if listbox.size() > 0:
        select_task = random.choice(listbox.get(0, tk.END))
        messagebox.showinfo("Random Task", f"Random Task: {select_task}")
    else:
        messagebox.showwarning("Warning", "No tasks to select.")

root=tk.Tk()
root.geometry("360x460")

root.title("TO DO LIST")
root.configure(bg="#2E2E2E")

label=tk.Label(root,text="TO-DO",font=('Georgia',20),bg="#2E2E2E",fg='white')
label.grid(padx=20,pady=20)

l1=tk.Label(root,text="Task :",font=('Georgia',20),bg="#2E2E2E",fg='white')
l1.grid(row=1,column=0,pady=10)
e1=tk.Entry(root, width=30, bg="#2E2E2E", fg="white")
e1.grid(row=1,column=1)

add_button=tk.Button(root, text="Add Task", command=add_task, bg="#404040", fg="white")
add_button.grid(column=1)

l2=tk.Label(root,text="LIST",font=('Georgia',20),bg="#2E2E2E",fg='white')
l2.grid(row=3,column=1,pady=10)
listbox=tk.Listbox(root, selectmode=tk.SINGLE, width=30, height=10, bg="#2E2E2E", fg="white")
listbox.grid(column=1,pady=10)

remove_button=tk.Button(root, text="Remove Task", command=rem_task, bg="#404040", fg="white")
remove_button.grid(row=4)

delete_button=tk.Button(root, text="Delete All", command=delete, bg="#404040", fg="white")
delete_button.grid(row=5,column=1)

random_button=tk.Button(root, text="Random Task", command=select_random, bg="#404040", fg="white")
random_button.grid(row=6,column=1)

root.mainloop()