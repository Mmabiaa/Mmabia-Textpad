from tkinter import filedialog, messagebox, PhotoImage, END
from text_formatting import*



def insert_image():
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", ".png;.jpg;.jpeg;.gif")])
    if filepath:
        try:
            image = PhotoImage(file=filepath)
            text_area.image_create(END, image=image)
            text_area.image = image  # Keep a reference to avoid garbage collection
        except Exception as e:
            messagebox.showerror("Error", str(e))

def insert_video():
    filepath = filedialog.askopenfilename(filetypes=[("Video Files", ".mp4;.avi;*.mov")])
    if filepath:
        messagebox.showinfo("Info", "Video inserted. (This is a placeholder implementation.)")
