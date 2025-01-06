from tkinter import filedialog, messagebox, END
import os
from text_formatting import *

filename = None

def new_file(root):
    #new_file : clears the text area and resets the filename
    global filename
    text_area.delete(1.0, END) 
    filename = None
    root.title("Mmabia Text Pad- Untitled File")

def open_file(root):
    #open_file : opens a file dialog,reads the selected file and displays it contents in the text area
    global filename
    filename = filedialog.askopenfilename(defaultextension=".txt",
                                          filetypes=[("All Files", "."), ("Text Documents", "*.txt")])
    if filename:
        with open(filename, 'r') as file:
            text_area.delete(1.0, END)
            text_area.insert(1.0, file.read())
        root.title(f"Mmabia Textpad - {os.path.basename(filename)}")


def save_file(root):
    #save_file : saves the current file 
    global filename
    if filename:
        try:
            with open(filename, 'w') as file:
                file.write(text_area.get(1.0, END))
            root.title(f"Mmabia Textpad - {os.path.basename(filename)}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        save_as_file()


def save_as_file(root):
    #save_as_file : opens a save dialog and saves the file with a name
    global filename
    filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("All Files", "."), ("Text Documents", "*.txt")])
    if filename:
        with open(filename, 'w') as file:
            file.write(text_area.get(1.0, END))
        root.title(f"Mmabiaa Textpad - {os.path.basename(filename)}")


