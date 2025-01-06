import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_info(message):
    """Log an informational message."""
    logging.info(message)

def log_error(message):
    """Log an error message."""
    logging.error(message)

def get_file_extension(filename):
    """Return the file extension for a given filename."""
    return os.path.splitext(filename)[1]

def is_valid_text_file(filename):
    """Check if the given filename has a valid text file extension."""
    valid_extensions = ['.txt', '.md', '.rtf']
    return get_file_extension(filename) in valid_extensions

def show_message(title, message):
    """Display a message box with the given title and message."""
    from tkinter import messagebox
    messagebox.showinfo(title, message)

def confirm_exit():
    """Confirm if the user wants to exit the application."""
    from tkinter import messagebox
    return messagebox.askokcancel("Quit", "Do you really want to quit?")

def clear_text_area(text_area):
    """Clear the content of the text area."""
    text_area.delete(1.0, 'end')
