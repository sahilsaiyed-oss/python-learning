import os

# Specify the directory path (use '.' for the current directory)
directory = "."

# Get the list of files and directories
contents = os.listdir(directory)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)
