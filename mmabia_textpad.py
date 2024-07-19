import tkinter as tk
from tkinter import filedialog, colorchooser, font, messagebox
from tkinter.scrolledtext import ScrolledText
import os

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Mmabia Textpad")
root.geometry("800x600")

# Initialize the global filename variable
filename = None

# Function to create a new file
def new_file():
    global filename
    text_area.delete(1.0, tk.END)
    filename = None
    root.title("Mmabia Textpad")

# Function to open an existing file
def open_file():
    global filename
    filename = filedialog.askopenfilename(defaultextension=".txt",
                                          filetypes=[("All Files", "."), ("Text Documents", "*.txt")])
    if filename:
        with open(filename, 'r') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(1.0, file.read())
        root.title(f"Mmabia Textpad - {os.path.basename(filename)}")

# Function to save the current file
def save_file():
    global filename
    if filename:
        try:
            with open(filename, 'w') as file:
                file.write(text_area.get(1.0, tk.END))
            root.title(f"Mmabia Textpad - {os.path.basename(filename)}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        save_as_file()

# Function to save the current file with a new name
def save_as_file():
    global filename
    filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("All Files", "."), ("Text Documents", "*.txt")])
    if filename:
        with open(filename, 'w') as file:
            file.write(text_area.get(1.0, tk.END))
        root.title(f"Mmabia Textpad - {os.path.basename(filename)}")

# Function to choose and set the font
def choose_font():
    font_family = tk.simpledialog.askstring("Font", "Enter font family:")
    font_size = tk.simpledialog.askinteger("Font", "Enter font size:")
    if font_family and font_size:
        text_area.configure(font=(font_family, font_size))

# Function to choose and set the text color
def choose_color():
    color = colorchooser.askcolor()[1]
    if color:
        text_area.configure(fg=color)

# Function to change the theme
def change_theme(theme):
    if theme == "light":
        text_area.configure(bg="white", fg="black")
    elif theme == "dark":
        text_area.configure(bg="black", fg="white")

# Function to insert an image
def insert_image():
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", ".png;.jpg;.jpeg;.gif")])
    if filepath:
        try:
            image = tk.PhotoImage(file=filepath)
            text_area.image_create(tk.END, image=image)
            text_area.image = image  # Keep a reference to avoid garbage collection
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Function to insert a video (placeholder implementation)
def insert_video():
    filepath = filedialog.askopenfilename(filetypes=[("Video Files", ".mp4;.avi;*.mov")])
    if filepath:
        messagebox.showinfo("Info", "Video inserted. (This is a placeholder implementation.)")

# Function to create the menu
def create_menu():
    menu = tk.Menu(root)
    root.config(menu=menu)
    
    # File menu
    file_menu = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=new_file)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_command(label="Save As", command=save_as_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    
    # Edit menu
    edit_menu = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Undo", command=lambda: text_area.event_generate("<<Undo>>"))
    edit_menu.add_command(label="Redo", command=lambda: text_area.event_generate("<<Redo>>"))
    edit_menu.add_separator()
    edit_menu.add_command(label="Cut", command=lambda: text_area.event_generate("<<Cut>>"))
    edit_menu.add_command(label="Copy", command=lambda: text_area.event_generate("<<Copy>>"))
    edit_menu.add_command(label="Paste", command=lambda: text_area.event_generate("<<Paste>>"))
    edit_menu.add_command(label="Select All", command=lambda: text_area.event_generate("<<SelectAll>>"))
    
    # Format menu
    format_menu = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label="Format", menu=format_menu)
    format_menu.add_command(label="Font", command=choose_font)
    format_menu.add_command(label="Color", command=choose_color)
    
    # Theme menu
    theme_menu = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label="Theme", menu=theme_menu)
    theme_menu.add_command(label="Light", command=lambda: change_theme("light"))
    theme_menu.add_command(label="Dark", command=lambda: change_theme("dark"))
    
    # Insert menu
    insert_menu = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label="Insert", menu=insert_menu)
    insert_menu.add_command(label="Image", command=insert_image)
    insert_menu.add_command(label="Video", command=insert_video)

# Function to create the text area
def create_text_area():
    global text_area
    text_area = ScrolledText(root, wrap='word', undo=True)
    text_area.pack(fill='both', expand=1)
    text_area.focus_set()

# Create the menu and text area
create_menu()
create_text_area()

# Run the main event loop
root.mainloop()