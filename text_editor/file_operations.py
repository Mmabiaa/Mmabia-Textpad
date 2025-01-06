from tkinter import filedialog, messagebox
import os

filename = None

def new_file(text_area):
    global filename
    text_area.delete(1.0, 'end')
    filename = None

def open_file(text_area):
    global filename
    filename = filedialog.askopenfilename(defaultextension=".txt",
                                          filetypes=[("All Files", "."), ("Text Documents", "*.txt")])
    
    if filename:
        with open(filename, 'r') as file:
            text_area.delete(1.0, 'end')
            text_area.insert(1.0, file.read())

def save_file(text_area):
    global filename
    
    if filename:
        try:
            with open(filename, 'w') as file:
                file.write(text_area.get(1.0, 'end'))
        except Exception as e:
            messagebox.showerror("Error", str(e))
        
def save_as_file(text_area):
    global filename
    
    filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("All Files", "."), ("Text Documents", "*.txt")])
    
    if filename:
        with open(filename, 'w') as file:
            file.write(text_area.get(1.0, 'end'))
    
def create_text_area(root):
    from tkinter.scrolledtext import ScrolledText
    
    global text_area
    text_area = ScrolledText(root, wrap='word', undo=True)