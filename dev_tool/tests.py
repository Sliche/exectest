import os

# Specify the path to the folder you want to list directories from
folder_path = "/home/borislav/Desktop/ferris/exectest"

# Get a list of directories within the specified folder
directories = [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]

# Print the list of directories
for directory in directories:
    print(directory)
