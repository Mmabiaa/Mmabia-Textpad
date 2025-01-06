from tkinter import simpledialog, font, TclError, colorchooser
from tkinter.scrolledtext import ScrolledText


current_font_family = "Times New Roman"
current_font_size = 18


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



# Function to choose and set the text color
def choose_color():
    #A Function that allows users to choose font color
    color = colorchooser.askcolor()[1]
    if color:
        text_area.configure(fg=color)


def create_text_area(root):
    global text_area
    text_area = ScrolledText(root, wrap='word', undo=True, font=(current_font_family, current_font_size))
    text_area.pack(fill='both', expand=1)
    text_area.focus_set()

def choose_font():
    #choose_font : opens a font dialog and sets the font
    global current_font_family, current_font_size
    font_family = simpledialog.askstring("Font", "Enter font family:")
    font_size = simpledialog.askinteger("Font", "Enter font size:")
    if font_family and font_size:
        current_font_family = font_family
        current_font_size = font_size
        text_area.configure(font=(current_font_family, current_font_size))


def increase_font_size(text_area):
    """Increase the font size by 5."""
    global current_font_size
    current_font_size += 5
    text_area.configure(font=(current_font_family, current_font_size))

def decrease_font_size(text_area):
    """Decrease the font size by 5, ensuring it doesn't go below 2."""
    global current_font_size
    if current_font_size > 2:
        current_font_size -= 5
        text_area.configure(font=(current_font_family, current_font_size))

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
