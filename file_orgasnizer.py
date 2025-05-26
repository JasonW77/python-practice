import os
import shutil

# set the directory you want to organize
DIRECTORY = os.path.expanduser(r"C:\Users\JasonW\OneDrive\Desktop\New folder") # Change to your target folder

# Define categories and extensions
CATEGORIES = {
     "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Others": []   
}

def get_category(file_extension):
    if not file_extension:
        return "Others"  # Catch files without extensions
    for category, extensions in CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category
    return "Others"  # Ensure fallback
        
def organize(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath):
            _, ext = os.path.splitext(filename)
            category = get_category(ext)
            category_folder = os.path.join(directory, category)

            if not os.path.exists(category_folder):
                os.makedirs(category_folder)

            dest_path = os.path.join(category_folder, filename)
            shutil.move(filepath, dest_path)
            print(f"Moved: {filename}->{category}/")

if __name__ == "__main__":
    print(f"Organizing files in: {DIRECTORY}")
    organize(DIRECTORY)