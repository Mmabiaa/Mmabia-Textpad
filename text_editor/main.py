from tkinter import Tk
from commands import create_menu
from file_operations import create_text_area
from text_formatting import create_text_area
# Initialize the main Tkinter window
root = Tk()
root.title("Mmabiaa Textpad")
root.geometry("800x600")

# Create the menu and text area
create_menu(root)
create_text_area(root)

# Run the main event loop
root.mainloop()
