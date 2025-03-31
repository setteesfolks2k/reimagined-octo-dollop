import os
import shutil

DOWNLOADS_FOLDER = "C:/Users/YourUser/Downloads"  # Change this to your folder path
EXTENSIONS = {
    "Images": [".jpg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3", ".wav"]
}

for file in os.listdir(DOWNLOADS_FOLDER):
    file_path = os.path.join(DOWNLOADS_FOLDER, file)
    if os.path.isfile(file_path):
        for category, extensions in EXTENSIONS.items():
            if file.lower().endswith(tuple(extensions)):
                category_folder = os.path.join(DOWNLOADS_FOLDER, category)
                os.makedirs(category_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(category_folder, file))
                print(f"📂 Moved {file} to {category}/")
