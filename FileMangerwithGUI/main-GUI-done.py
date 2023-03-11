import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organize_files():
    if path := filedialog.askdirectory():
        files = os.listdir(path)

        for i in files:
            filename, extension = os.path.splitext(i)
            extension_1 = extension[1:]
            folder_path = os.path.join(path, extension_1)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(os.path.join(path, i), os.path.join(folder_path, i))
        messagebox.showinfo("Success", "Files have been organized successfully!")
    else:
        messagebox.showwarning("Error", "Please select a directory.")

root = tk.Tk()
root.title("File Organizer")

canvas = tk.Canvas(root, height=200, width=400)
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

button = tk.Button(frame, text="Select Directory", command=organize_files)
button.pack()

root.mainloop()
