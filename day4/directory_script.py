import os

# Get directory name from user
directory_name = input("Enter the name of the directory: ")

# Create the directory
os.makedirs(directory_name)
print(f"Directory '{directory_name}' created successfully.")
