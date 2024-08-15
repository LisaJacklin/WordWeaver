#Lisa Jacklin
#WordWeaver
#2024-08-14

from tkinter import Tk, Label, Menu, Text, PhotoImage, Frame


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WordWeave")
        self.root.geometry("800x600")

        # Set up menu bar
        self.setup_menu()

        # Set up background
        
        # Set up text area
        #TOOD adjustments to a new function call
        self.text_area = Text(self.root, wrap='word')
        self.text_area.pack(expand=True, fill='both')

		#labels
        self.label = Label(self.root, text="Welcome to WordWeaver")
        self.label.pack(expand=True)

    def setup_menu(self):
        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)

		#File Commands
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_command(label="Open...")
        file_menu.add_command(label="Save As...")
        
		#General Commands
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

		#File Editing Commands
        edit_menu = Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Undo")
        edit_menu.add_command(label="Redo")
        
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut")
        edit_menu.add_command(label="Copy")
        edit_menu.add_command(label="Paste")
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        

#this will allow me to run it without going through main.py
# if __name__ == "__main__":
#     root = Tk()
#     app = MainApp(root)
#     root.mainloop()
