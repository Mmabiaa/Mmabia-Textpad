from tkinter import Menu
from file_operations import *
from text_formatting import *
from insertions import *
from tkinter import messagebox


def create_menu(root):
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
    
def about():
    messagebox.showinfo("About", "Mmabiaa Text Editor\nVersion 1.0\n\n Created by Boateng Agyenim Prince\n\n A simple text editor built using python and tkinter")
