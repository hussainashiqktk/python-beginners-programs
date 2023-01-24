"""
This script will add the string "new_string_" to the beginning of the name of all the files in the current directory. Be sure to change the string_to_add variable to the string you would like to add to the file names.

"""

import os

# Define the string to add to the file names
string_to_add = "new_string_"

# Get the current directory
current_dir = os.getcwd()

# Get all the files in the current directory
files = os.listdir(current_dir)

# Loop through all the files
for file in files:
    # Get the current file name
    current_file_name = file
    # Create the new file name by adding the string to the current file name
    new_file_name = string_to_add + current_file_name
    # Use the os.rename() function to rename the file
    os.rename(current_file_name, new_file_name)
    time.sleep(1)
