import os
import time

# Define the string to remove from the file names
string_to_remove = "new_string_"

# Get the current directory
current_dir = os.getcwd()

# Get all the files in the current directory
files = os.listdir(current_dir)

# Loop through all the files
for file in files:
    # Get the current file name
    current_file_name = file
    # Check if the string to remove is in the file name
    if current_file_name.startswith(string_to_remove):
        # Create the new file name by removing the string from the current file name
        new_file_name = current_file_name.replace(string_to_remove, "", 1)
        # Use the os.rename() function to rename the file
        os.rename(current_file_name, new_file_name)
        # Wait for 1 second before renaming the next file
        time.sleep(1)
