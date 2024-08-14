#Lisa Jacklin
#WordWeaver
#2024-08-14

from tkinter import Tk, Frame, Text, Menu, PhotoImage, Label
from tkinter import filedialog

#imports from other files being built:
from word_counter import WordCounter
from logger import logger

class MainApp:
	def __init__(self, root):
		self.root = root
		self.root.title("WordWeaver")
		self.root.geometry("800x600") #basic window size

		#additional setup for the menu bar
		self.setup_menu()

		#now text area
		self.text_area = Text(self.root, wrap="word")
		self.text_area.pack(expand=True, fill="both")

		#basic labeling for Tkinter setup check
		self.label = Label(self.root, text="Welcome to WordWeaver!")
		self.label.pack(expand=True)
	
	#now to add in menu/setup bar items
	def setup_menu(self):
			menu_bar = Menu(self.root)
			self.root.config(menu=menu_bar)

			file_menu = Menu(menu_bar, tearoff = 0)
			file_menu.add_command(label = "Open...")
			file_menu.add_command(label = "Save...")
			file_menu.add_command(label="New")
			file_menu.add_cascade(label="File", menu=file_menu)

