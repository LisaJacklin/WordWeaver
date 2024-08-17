#Lisa Jacklin
#WordWeaver
#2024-08-16

import os

class FileManager:
    def __init__(self):
        self.current_file = None    
        self.file_content = ""
    
    def create_new_file(self, fiename):
        """Creates a new file and sets it as the current file."""
        if os.path.exists(filename):
            print(f"File '{filename}' already exists. Try opening it instead.")
        else:
            with open(filename, 'w') as file:
                self.current_file = filename
                self.file_content = ""
                print(f"New file '{filename}' created.")

    def open_existing_file(self, filename):
        """Opens an existing file and loads its content."""
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                self.current_file = filename
                self.file_content = file.read()
                print(f"File '{filename}' opened.")
                print(f"Content:\n{self.file_content}")
        else:
            print(f"File '{filename}' does not exist. Try creating it first.")


    def save_file_as(self, filename):
        """Saves the current content to a new file."""
        with open(filename, 'w') as file:
            file.write(self.file_content)
            self.current_file = filename
            print(f"File saved as '{filename}'.")
    
    def edit_content(self, new_content):
        """Allows user to edit the current file content."""
        if self.current_file:
            self.file_content = new_content
            print(f"Content updated in '{self.current_file}'.")
        else:
            print("No file is currently open. Please create or open a file first.")
