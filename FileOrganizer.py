import os
import shutil

#Set the folder you want to organise
source_folder = r"C:\Users\YourName\Downloads" # Change this to your folder path

# Define categories and extensions
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', ',tar', '.gz'],
    'Code': ['.py', '.js', '.html', '.css', '.cpp', '.java'],
}

def create_and_move(file, folder_name):
    folder_path = os.path.join(source_folder, folder_name)
    os.makedir(folder_path, exist_ok = True)
    shutil.mave(os.path.join(source_folder, file), os.path.join(folder_path, file))

def organize_files():
    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)

        if os.path.isfile(file.path):
            file_ext = os.path.splitext(file)[1].lower()
            moved = False
            for category, extensions in file_types.items():
                if file_ext in extensions:
                    create_and_move(file, category)
                    moved = True
                    break
            if not moved:
                create_and_move(file, "Others")
    
    print(" Files have been organized!")

organize_files()

