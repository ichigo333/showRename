import os
import re
import argparse

def rename_files(path):
    # Get the list of files in the given path
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]

    # Loop through the files
    for file in files:
        # Parse the filename using regular expressions
        match = re.search(r'^(.+?)[sS](\d+)[eE](\d+).*?(\d+p)\.(.+)$', file)
        if match:
            # Build the new filename with the same extension
            file_extension = os.path.splitext(file)[1]
            new_filename = f"{match.group(1).replace('.', '_')}_s{match.group(2)}e{match.group(3)}_{match.group(4)}{file_extension}"
            old_path = os.path.join(path, file)
            new_path = os.path.join(path, new_filename)
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed {file} to {new_filename}")

# Parse command line arguments
parser = argparse.ArgumentParser(description='Rename files in folder')
parser.add_argument('-p', '--path', type=str, help='Path to folder')
args = parser.parse_args()

if args.path:
    path = args.path
else:
    path = input("Enter path to folder: ")

# Call the function with the provided or entered path
if os.path.isdir(path):
    rename_files(path)
else:
    print(f"{path} is not a valid directory")
