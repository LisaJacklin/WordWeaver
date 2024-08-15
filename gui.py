#Lisa Jacklin
#WordWeaver
#2024-08-14

from tkinter import Tk, Label, Menu, Text, PhotoImage, Frame
import os

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WordWeave")
        self.root.geometry("800x600")

        # Set up menu bar
        self.setup_menu()

        # Set up background
       	#self.setup_background()

        # Set up text area
        #TOOD adjustments to a new function call
        self.text_area = Text(self.root, wrap='word')
        self.text_area.pack(expand=True, fill='both')
        #self.setup_text_area()

		#labels
        self.label = Label(self.root, text="Welcome to WordWeaver")
        self.label.pack(expand=True)

    def setup_menu(self):
        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_command(label="Open...")
        file_menu.add_command(label="Save As...")
        
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        edit_menu = Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Undo")
        edit_menu.add_command(label="Redo")
        
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut")
        edit_menu.add_command(label="Copy")
        edit_menu.add_command(label="Paste")
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

#TODO Adjust the following items
    def setup_background(self):
        try:
            image_path = "assets/default_background.png"
            if os.path.exists(image_path):
                background_image = PhotoImage(file=image_path)
                background_label = Label(self.root, image=background_image)
                background_label.place(relwidth=1, relheight=1)
                self.background_image = background_image  # Keep a reference to avoid garbage collection
            else:
                print(f"Error: File {image_path} does not exist.")
        except Exception as e:
            print(f"Error setting up background: {e}")

    def setup_text_area(self):
        # Create a Frame to hold the text area (this will be useful for layering with the background)
        text_frame = Frame(self.root, bg='white', bd=5)
        text_frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.8, anchor='center')

        # Text area setup
        self.text_area = Text(text_frame, wrap='word')
        self.text_area.pack(expand=True, fill='both')


#this will allow me to run it without going through main.py
if __name__ == "__main__":
    root = Tk()
    app = MainApp(root)
    root.mainloop()
