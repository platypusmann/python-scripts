import os
import shutil

# Ask user for target directory
target_dir = os.path.expanduser(input("Enter the folder path to organize: ").strip())

# Define folder mapping based on file extension
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Text': ['.txt', '.md'],
    'PDFs': ['.pdf'],
    'Python': ['.py'],
    'Others': []
}

# Make sure the target folder exists
if not os.path.isdir(target_dir):
    print("Folder does not exist.")
    exit()

print(f"\nOrganizing files in: {target_dir}")

for file in os.listdir(target_dir):
    file_path = os.path.join(target_dir, file)

    # Skip if it's a folder
    if os.path.isdir(file_path):
        continue

    # Get file extension
    _, ext = os.path.splitext(file)

    # Determine category folder
    moved = False
    for category, extensions in file_types.items():
        if ext.lower() in extensions:
            dest_folder = os.path.join(target_dir, category)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(dest_folder, file))
            print(f"Moved {file} to {category}/")
            moved = True
            break

    # If not matched, put in 'Others'
    if not moved:
        dest_folder = os.path.join(target_dir, "Others")
        os.makedirs(dest_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(dest_folder, file))
        print(f"Moved {file} to Others/")
