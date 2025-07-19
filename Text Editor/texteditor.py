import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter import ttk
import os

saved = False
light_mode = True
font_size = 10

def new_file():
    content = text.get(1.0, tk.END)
    if not saved and len(content) > 1:
        result=messagebox.askyesnocancel("Unsaved Changes", "Do you want to save before opening a new file?")
        if result:
            save_file()
    text.delete(1.0, tk.END)


def open_file():
    global saved
    saved = False
    initial_directory = os.path.expanduser("~")
    print(initial_directory)
    file_path = fd.askopenfilename(
        title = "Select a File",
        initialdir = initial_directory,
        filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text.delete(1.0, tk.END)
            text.insert(1.0, content)

def save_file():
    global saved
    saved=True
    file_path = fd.asksaveasfilename(
        title="Save File",
        defaultextension = ".txt",
        filetypes = [("Text File", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, 'w') as file:
                content = text.get(1.0, tk.END)
                file.write(content)
            print("File Saved Successfully")
        except Exception as e:
            print("Error Saving The File:", e)

def exit_program():
    content = text.get(1.0, tk.END)
    if not saved and len(content) > 1:
        result = messagebox.askyesnocancel("Unsaved Changes", "Do you want to save before exiting?")
        if result:
            save_file()
            main.destroy()
        elif result is False:
            main.destroy()
    else:
        main.destroy()

def change_state(event):
    global saved
    saved = False

def zoom_in():
    global font_size
    font_size += 5
    text.config(font=("Arial", font_size))

def zoom_out():
    global font_size
    if font_size > 5:
        font_size -= 5
        text.config(font=("Arial", font_size))

def switch_mode():
    global light_mode
    if light_mode:
        text.config(background='black', foreground='white', insertbackground='white')
        light_mode = False
    else:
        text.config(background='white', foreground='black', insertbackground='black')
        light_mode = True

main = tk.Tk()
main.title("Text Editor")
main.geometry("800x400")

menu_bar = tk.Menu(main)
main.config(menu=menu_bar)

menu_file = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=menu_file)
menu_view = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="View", menu=menu_view)

menu_file.add_command(label="New", command=new_file)
menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=exit_program)

menu_view.add_command(label="Zoom In", command=zoom_in)
menu_view.add_command(label="Zoom Out", command=zoom_out)
menu_view.add_separator()
menu_view.add_command(label="Switch Mode", command=switch_mode)

text = tk.Text(main, font=("Helvetica", 10), background='white', foreground='black', insertbackground='black')
text.pack(fill="both", expand=True)
text.bind('<Key>', change_state)

main.protocol('WM_DELETE_WINDOW', exit_program)

main.mainloop()