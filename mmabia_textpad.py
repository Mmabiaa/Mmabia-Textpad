from tkinter import *
from tkinter import filedialog, colorchooser, font, messagebox, simpledialog
from tkinter.scrolledtext import ScrolledText
import os

# Initialize the main Tkinter window
root = Tk()
root.title("Mmabia Textpad")
root.geometry("800x600")
root.configure(bg="#f0f0f0")  # Set a light background color

# Initialize global variables
filename = None
current_font_family = "Arial"  # Changed font family for aesthetics
current_font_size = 12

# Status bar to show file information
status_bar = Label(root, text="Welcome to Mmabia Textpad", bd=1, relief=SUNKEN, anchor=W)
status_bar.pack(side=BOTTOM, fill=X)

# Function to create a new file
def new_file():
    global filename
    text_area.delete(1.0, END)
    filename = None
    root.title("Mmabia Textpad - Untitled File")
    status_bar.config(text="New file created")

# Function to open an existing file
def open_file():
    global filename
    filename = filedialog.askopenfilename(defaultextension=".txt",
                                          filetypes=[("All Files", "."), ("Text Documents", "*.txt")])
    if filename:
        with open(filename, 'r') as file:
            text_area.delete(1.0, END)
            text_area.insert(1.0, file.read())
        root.title(f"Mmabia Textpad - {os.path.basename(filename)}")
        status_bar.config(text=f"Opened: {os.path.basename(filename)}")

# Function to save the current file
def save_file():
    global filename
    if filename:
        try:
            with open(filename, 'w') as file:
                file.write(text_area.get(1.0, END))
            root.title(f"Mmabia Textpad - {os.path.basename(filename)}")
            status_bar.config(text=f"Saved: {os.path.basename(filename)}")
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
            file.write(text_area.get(1.0, END))
        root.title(f"Mmabia Textpad - {os.path.basename(filename)}")
        status_bar.config(text=f"Saved as: {os.path.basename(filename)}")

# Function to create the menu with icons (update paths to your icons)
def create_menu():
    menu = Menu(root)
    root.config(menu=menu)
    
    # File menu
    file_menu = Menu(menu, tearoff=False)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=new_file)  # Add icon here if needed
    file_menu.add_command(label="Open", command=open_file)  # Add icon here if needed
    file_menu.add_command(label="Save", command=save_file)  # Add icon here if needed
    file_menu.add_command(label="Save As", command=save_as_file)  # Add icon here if needed
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    # Edit menu (add icons similarly)
    edit_menu = Menu(menu, tearoff=False)
    menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Undo", command=lambda: text_area.event_generate("<<Undo>>"))
    edit_menu.add_command(label="Redo", command=lambda: text_area.event_generate("<<Redo>>"))
    
    # Format menu (add icons similarly)
    format_menu = Menu(menu, tearoff=False)
    menu.add_cascade(label="Format", menu=format_menu)

    # Theme menu (add icons similarly)

    # Help menu (add icons similarly)

# Function to create the text area with padding and styling
def create_text_area():
    global text_area
    text_area = ScrolledText(root, wrap='word', undo=True,
                              font=(current_font_family, current_font_size),
                              bg="#ffffff", fg="#000000",
                              bd=2, relief=SUNKEN,
                              padx=10, pady=10)  # Added padding and border style

    text_area.pack(fill='both', expand=1)
    text_area.focus_set()

# Create the menu and text area
create_menu()
create_text_area()

# Run the main event loop
root.mainloop()