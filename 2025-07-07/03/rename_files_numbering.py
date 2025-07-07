import os
import argparse

def rename_files_numbering(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    files.sort()  # Sort files to ensure consistent ordering

    for index, filename in enumerate(files, start=1):
        new_name = f"{index:02d}_{filename}"
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed '{filename}' to '{new_name}'")
def main(): 
    parser = argparse.ArgumentParser(description="Rename files in a directory with numbering.")
    parser.add_argument("directory", type=str, help="The directory containing the files to rename.")
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: The directory '{args.directory}' does not exist.")
        return

    rename_files_numbering(args.directory)  
if __name__ == "__main__":
    main()
# This script renames files in a specified directory by adding a two-digit number prefix to each file name.
# The files are sorted alphabetically before renaming to ensure consistent numbering.
# Usage: python rename_files_numbering.py /path/to/directory