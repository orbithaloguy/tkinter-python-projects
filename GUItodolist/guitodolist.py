import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task != '':
        tasks.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please Enter a Task.")


def clear_tasks():
    if tasks.size() != 0:
        tasks.delete(0, tk.END)
    else:
        messagebox.showwarning("Inpuy Error", "Please Enter a Task.")

def delete_task():
    try:
        task = tasks.curselection()
        tasks.delete(task)
    except:
        messagebox.showwarning("Input Error", "Please Select a Task To Delete")

main = tk.Tk()
main.resizable(False, False)
main.title("To Do List")

intro = tk.Label(main, text="TO-DO LIST", font=("Helvetica", 16))
intro.pack(pady=10)

entry = tk.Entry(main, font=("Helvetica", 16))
entry.pack()

btn_frame = tk.Frame(main, width=250, height=25, bd=2, relief="groove")
btn_frame.pack()

btn_add = tk.Button(btn_frame, text="Add", width=10, command=add_task)
btn_add.pack(side="left")
btn_clear = tk.Button(btn_frame, text="Clear All", width=10, command=clear_tasks)
btn_clear.pack(side="left")

tasks = tk.Listbox(main, width=50, height=10)
tasks.pack()

btn_delete = tk.Button(main, text="Delete", width=10, command=delete_task)
btn_delete.pack()

main.mainloop()