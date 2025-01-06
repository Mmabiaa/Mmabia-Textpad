from tkinter import simpledialog, font, TclError

current_font_family = "Times New Roman"
current_font_size = 18

def choose_font(text_area):
    """Open a dialog to choose a font family and size."""
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

def apply_bold(text_area):
    """Toggle bold formatting on the selected text."""
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

def apply_italic(text_area):
    """Toggle italic formatting on the selected text."""
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

def apply_underline(text_area):
    """Toggle underline formatting on the selected text."""
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

def apply_strikethrough(text_area):
    """Toggle strikethrough formatting on the selected text."""
    try:
        current_tags = text_area.tag_names("sel.first")
        if "strikethrough" in current_tags:
            text_area.tag_remove("strikethrough", "sel.first", "sel.last")
        else:
            text_area.tag_add("strikethrough", "sel.first", "sel.last")
            strikethrough_font = font.Font(text_area, text_area.cget("font"))
            strikethrough_font.configure(overstrike=True)
            text_area.tag_configure("strikethrough", font=strikethrough_font)
    except TclError:
        pass