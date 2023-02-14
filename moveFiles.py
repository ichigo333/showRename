import os
import shutil
import argparse

def move_files_to_parent_folder(path):
    # Get the list of subdirectories in the given path
    subdirectories = [subdir for subdir in os.listdir(path) if os.path.isdir(os.path.join(path, subdir))]
    
    # Loop through the subdirectories
    for subdir in subdirectories:
        subdir_path = os.path.join(path, subdir)
        # Get the list of files in the subdirectory
        files = [file for file in os.listdir(subdir_path) if os.path.isfile(os.path.join(subdir_path, file))]
        # Move the files to the parent directory
        for file in files:
            src_path = os.path.join(subdir_path, file)
            dst_path = os.path.join(path, file)
            shutil.move(src_path, dst_path)
            print(f"Moved file {file} from {src_path} to {dst_path}")

# Parse command line arguments
parser = argparse.ArgumentParser(description='Move files from subfolders to parent folder')
parser.add_argument('path', type=str, help='Path to folder')
args = parser.parse_args()

# Call the function with the provided path
move_files_to_parent_folder(args.path)