#Lisa Jacklin
#WordWeaver
#2024-08-14

from tkinter import Tk, Label, Menu, Text, PhotoImage, Frame
#from PIL import Image, ImageTk, ImageEnhance
import os

from logger import logger
from word_counter import WordCounter

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WordWeave")
        self.root.geometry("800x600")

		# Initialize Logger and WordCounter
        self.logger = logger()
        self.word_counter = WordCounter()
        
        # Set up menu bar
        self.setup_menu()

    # Set up background
        self.setup_background()

        # Set up text area on top of the overlay
        self.setup_text_area()
                
        # Set up text area
        #TOOD adjustments to a new function call
        # self.text_area = Text(self.root, wrap='word')
        # self.text_area.pack(expand=True, fill='both')

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

        #Customizations Commands
        custom_menu = Menu(menu_bar, tearoff=0)
        custom_menu.add_command(label="Background")
        custom_menu.add_command(label="more...") 
        menu_bar.add_cascade(label="Customize", menu=custom_menu)


    def setup_background(self):
        # Create a frame to cover the entire window
        background_frame = Frame(self.root, bg="lightblue")
        background_frame.place(relwidth=1, relheight=1)  # Fill the entire window

	
    def setup_text_area(self):
        # Place the text area on top of the semi-transparent overlay
        text_frame = Frame(self.root, bd=0)
        text_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        # Text area setup
        self.text_area = Text(text_frame, wrap='word', bg='white', font=('Arial', 12))
        self.text_area.pack(expand=True, fill='both')


