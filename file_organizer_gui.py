# this is the tkinter version of the file with gui
import os 
import shutil
import tkinter as tk 
from tkinter import filedialog, messagebox

# File type categories
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '. bmp'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Documents': ['.pdf', '.docx', '.txt', '.doc', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Code': ['.py', '.js', '.html', '.css', '.cpp', '.java'],
}

def organize_files(folder_path):
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        if os.path.isfile(full_path):
            ext = os.path.splitext(file)[1].lower()
            moved = False
            for folder, extensions in file_types.items():
                if ext in extensions:
                    target_folder = os.path.join(folder_path, folder)
                    os.makedirs(target_folder, exist_ok = True)
                    shutil.move(full_path, os.path.join(target_folder, file))
                    moved = True
                    break
            if not moved:
                others_folder = os.path.join(folder_path, 'Others')
                os.makedir(others_folder, exist_ok = True)
                shutil.move(full_path, os.path.join(others_folder, file))
    messagebox.showinfo("Success", "File organised successfully!")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        organize_files(folder_selected)

# UI Setup
root = tk.Tk()
root.title("File Organizer")
root.geometry("300x150")

label = tk.Label(root, text="Choose a folder to organize", font=("Arial", 12))
label.pack(pady = 20)

browse_btn = tk.Button(root, text="Browse Folder", command = browse_folder)
browse_btn.pack()

root.mainloop()