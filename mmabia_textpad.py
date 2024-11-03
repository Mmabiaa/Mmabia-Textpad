#Importing required modules
from tkinter import *
from tkinter import filedialog, colorchooser, font, messagebox, simpledialog
from tkinter.scrolledtext import ScrolledText
import os
'''
    tkinter for GUI
    filedialog for opening and saving files
    colorchooser for choosing color
    font for choosing font
    messagebox for displaying messages
    simpledialog for displaying input boxes
    ScrolledText for scrolling text
    os for file operations
'''



# Initialize the main Tkinter window
root = Tk()
root.title("Mmabiaa Textpad")
root.geometry("800x600")
'''
    root: the main window object
    title: sets the title of the window
    geometry: sets the size of the window
'''


# Initialize the global filename and font variables
filename = None
current_font_family = "Times New Roman"
current_font_size = 18

'''
    filename: stores the name of the file
    current_font_family: stores the current font family
    current_font_size: stores the current font size
'''

# Function to create a new file
def new_file():
    #new_file : clears the text area and resets the filename
    global filename
    text_area.delete(1.0, END) 
    filename = None
    root.title("Mmabia Text Pad- Untitled File") #Sets the title as Mmabia Textpad
    

# Function to open an existing file
def open_file():
    #open_file : opens a file dialog,reads the selected file and displays it contents in the text area
    global filename
    filename = filedialog.askopenfilename(defaultextension=".txt",
                                          filetypes=[("All Files", "."), ("Text Documents", "*.txt")])
    if filename:
        with open(filename, 'r') as file:
            text_area.delete(1.0, END)
            text_area.insert(1.0, file.read())
        root.title(f"Mmabia Textpad - {os.path.basename(filename)}")

# Function to save the current file
def save_file():
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

# Function to save the current file with a new name
def save_as_file():
    #save_as_file : opens a save dialog and saves the file with a name
    global filename
    filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("All Files", "."), ("Text Documents", "*.txt")])
    if filename:
        with open(filename, 'w') as file:
            file.write(text_area.get(1.0, END))
        root.title(f"Mmabia Textpad - {os.path.basename(filename)}")

# Function to choose and set the font
def choose_font():
    #choose_font : opens a font dialog and sets the font
    global current_font_family, current_font_size
    font_family = simpledialog.askstring("Font", "Enter font family:")
    font_size = simpledialog.askinteger("Font", "Enter font size:")
    if font_family and font_size:
        current_font_family = font_family
        current_font_size = font_size
        text_area.configure(font=(current_font_family, current_font_size))

# Function to increase the font size
def increase_font_size():
    #This function helps to increase the font size of a font by 5
    global current_font_size
    current_font_size += 5
    text_area.configure(font=(current_font_family, current_font_size))

# Function to decrease the font size
def decrease_font_size():
    #This function helps to decrease the font size of a font by 5
    global current_font_size
    if current_font_size > 2:
        current_font_size -= 5
        text_area.configure(font=(current_font_family, current_font_size))

# Function to choose and set the text color
def choose_color():
    #A Function that allows users to choose font color
    color = colorchooser.askcolor()[1]
    if color:
        text_area.configure(fg=color)

# Function to change the theme
def change_theme(theme):
    if theme == "light":
        text_area.configure(bg="white", fg="black")
    elif theme == "dark":
        text_area.configure(bg="black", fg="white")
    elif theme == "gray":
        text_area.configure(bg="grey", fg="white")
    elif theme == "green":
        text_area.configure(bg="green", fg="black")
    elif theme == "blue":
        text_area.configure(bg="blue", fg="white")
    elif theme == "purple":
        text_area.configure(bg="purple", fg="white")
    elif theme == "orange":
        text_area.configure(bg="orange", fg="black")
    elif theme == "yellow":
        text_area.configure(bg="yellow", fg="black")
    elif theme == "pink":
        text_area.configure(bg="pink", fg="black")
    elif theme == "brown":
        text_area.configure(bg="brown", fg="white")
    elif theme == "cyan":
        text_area.configure(bg="cyan", fg="black")
    elif theme == "magenta":
        text_area.configure(bg="magenta", fg="white")
    elif theme == "custom":
        text_area.configure(bg="aqua", fg="white")

# Function to insert an image
def insert_image():
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", ".png;.jpg;.jpeg;.gif")])
    if filepath:
        try:
            image = PhotoImage(file=filepath)
            text_area.image_create(END, image=image)
            text_area.image = image  # Keep a reference to avoid garbage collection
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Function to insert a video (placeholder implementation)
def insert_video():
    filepath = filedialog.askopenfilename(filetypes=[("Video Files", ".mp4;.avi;*.mov")])
    if filepath:
        messagebox.showinfo("Info", "Video inserted. (This is a placeholder implementation.)")

# Function to apply bold formatting
def apply_bold():
    try:
        current_tags = text_area.tag_names("sel.first")
        if "bold" in current_tags:
            text_area.tag_remove("bold", "sel.first", "sel.last")
        else:
            text_area.tag_add("bold", "sel.first", "sel.last")
            bold_font = font.Font(text_area, text_area.cget("font"))
            bold_font.configure(weight="bold")
            text_area.tag_configure("bold", font=bold_font)
    except TclError:
        pass

# Function to apply strikethrough formatting
def apply_strikethrough():
    try:
        current_tags = text_area.tag_names("sel.first")
        if "strikethrough" in current_tags:
            text_area.tag_remove("strikethrough", "sel.first", "sel.last")
        else:
            text_area.tag_add("strikethrough", "sel.first", "sel.last")
            strikethrough_font = font.Font(text_area, text_area.cget("font"))
            strikethrough_font.configure(slant="italic")
            text_area.tag_configure("strikethrough", font=strikethrough_font)
    except TclError:
        pass

# Function to apply italic formatting
def apply_italic():
    try:
        current_tags = text_area.tag_names("sel.first")
        if "italic" in current_tags:
            text_area.tag_remove("italic", "sel.first", "sel.last")
        else:
            text_area.tag_add("italic", "sel.first", "sel.last")
            italic_font = font.Font(text_area, text_area.cget("font"))
            italic_font.configure(slant="italic")
            text_area.tag_configure("italic", font=italic_font)
    except TclError:
        pass

# Function to apply underline formatting
def apply_underline():
    try:
        current_tags = text_area.tag_names("sel.first")
        if "underline" in current_tags:
            text_area.tag_remove("underline", "sel.first", "sel.last")
        else:
            text_area.tag_add("underline", "sel.first", "sel.last")
            underline_font = font.Font(text_area, text_area.cget("font"))
            underline_font.configure(underline=True)
            text_area.tag_configure("underline", font=underline_font)
    except TclError:
        pass

# Function for about
def about():
    messagebox.showinfo("About", "Mmabia Text Editor\nVersion 1.0\n\n Created by Boateng Agyenim Prince\n\n A simple text editor built using python and tkinter")

# Function to create the menu
def create_menu():
    menu = Menu(root)
    root.config(menu=menu)
    
    # File menu
    file_menu = Menu(menu, tearoff=False)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=new_file)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_command(label="Save As", command=save_as_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    
    # Edit menu
    edit_menu = Menu(menu, tearoff=False)
    menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Undo", command=lambda: text_area.event_generate("<<Undo>>"))
    edit_menu.add_command(label="Redo", command=lambda: text_area.event_generate("<<Redo>>"))
    edit_menu.add_separator()
    edit_menu.add_command(label="Cut", command=lambda: text_area.event_generate("<<Cut>>"))
    edit_menu.add_command(label="Copy", command=lambda: text_area.event_generate("<<Copy>>"))
    edit_menu.add_command(label="Paste", command=lambda: text_area.event_generate("<<Paste>>"))
    edit_menu.add_command(label="Select All", command=lambda: text_area.event_generate("<<SelectAll>>"))
    edit_menu.add_separator()
    
    # Format menu
    format_menu = Menu(menu, tearoff=False)
    menu.add_cascade(label="Format", menu=format_menu)
    format_menu.add_command(label="Font", command=choose_font)
    format_menu.add_command(label="Increase Font Size", command=increase_font_size)
    format_menu.add_command(label="Decrease Font Size", command=decrease_font_size)
    format_menu.add_command(label="Color", command=choose_color)
    format_menu.add_separator()
    format_menu.add_command(label="Bold", command=apply_bold)
    format_menu.add_command(label="Italic", command=apply_italic)
    format_menu.add_command(label="Underline", command=apply_underline)
    format_menu.add_command(label="Strikethrough", command=apply_strikethrough)
    
    # Theme menu
    theme_menu = Menu(menu, tearoff=False)
    menu.add_cascade(label="Theme", menu=theme_menu)
    theme_menu.add_command(label="Light", command=lambda: change_theme("light"))
    theme_menu.add_command(label="Dark", command=lambda: change_theme("dark"))
    theme_menu.add_command(label="Gray", command=lambda: change_theme("gray"))
    theme_menu.add_command(label="Green", command=lambda: change_theme("green"))
    theme_menu.add_command(label="Blue", command=lambda: change_theme("blue"))
    theme_menu.add_command(label="Purple", command=lambda: change_theme("purple"))
    theme_menu.add_command(label="Red", command=lambda: change_theme("red"))
    theme_menu.add_command(label="Orange", command=lambda: change_theme("orange"))
    theme_menu.add_command(label="Yellow", command=lambda: change_theme("yellow"))
    theme_menu.add_command(label="Brown", command=lambda: change_theme("brown"))
    theme_menu.add_command(label="Pink", command=lambda: change_theme("pink"))
    theme_menu.add_command(label="Cyan", command=lambda: change_theme("cyan"))
    theme_menu.add_command(label="Custom", command=lambda: change_theme("custom"))

    
    # Help menu
    help_menu = Menu(menu, tearoff=False)
    menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=about)
    
    # Insert menu
    insert_menu = Menu(menu, tearoff=False)
    menu.add_cascade(label="Insert", menu=insert_menu)
    insert_menu.add_command(label="Image", command=insert_image)
    insert_menu.add_command(label="Video", command=insert_video)

# Function to create the text area
def create_text_area():
    global text_area
    text_area = ScrolledText(root, wrap='word', undo=True, font=(current_font_family, current_font_size))
    text_area.pack(fill='both', expand=1)
    text_area.focus_set()

# Create the menu and text area
create_menu()
create_text_area()

# Run the main event loop
root.mainloop()
