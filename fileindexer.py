import os

# Define the directory path
directory_path = "your/path"

# Files and folders to be ignored
ignore_list = ["ignore_file_or_folder"]

# List file and folder names including subfolders
with open("file_list.txt", "w", encoding="utf-8") as file:
    for root_dir, sub_dirs, files in os.walk(directory_path):
        # Remove folders in the ignore list from the sub_dirs list
        sub_dirs[:] = [d for d in sub_dirs if d not in ignore_list]

        # Print the current directory
        file.write(f"Folder: {root_dir}\n")

        # Print subfolders (after ignore check)
        for sub_dir in sub_dirs:
            file.write(f"  Sub Folder: {sub_dir}\n")

        # Print files (with ignore check)
        for filename in files:
            if filename not in ignore_list:
                file.write(f"  File: {filename}\n")

        file.write("\n")

print("All directory and file names (with ignore list applied) have been written to 'file_list.txt'.")