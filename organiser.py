import os
import shutil

folder_path = "C:/Users/your_user_here/Downloads"

file_categories = {
    ".pdf": "pdf",
    ".jpg": "img",
    ".jpeg": "img",
    ".png": "img",
    ".mp4": "vid",
    ".mp3": "audio",
    ".zip": "compressed",
    ".rar": "compressed",
    ".exe": "exec",
    ".docx": "docs",
    ".txt": "docs",
}

files = os.listdir(folder_path)

for file in files:
    name, extension = os.path.splitext(file)
    extension = extension.lower()

    if extension in file_categories:
        category = file_categories[extension]
        category_path = os.path.join(folder_path, category)

        if not os.path.exists(category_path):
            os.makedirs(category_path)

        source = os.path.join(folder_path, file)
        destination = os.path.join(category_path, file)
        shutil.move(source, destination)
        print(f"Moved {file} to {category}/")