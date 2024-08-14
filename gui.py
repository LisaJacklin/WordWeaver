#Lisa Jacklin
#WordWeaver
#2024-08-14

from tkinter import Frame, Text, Menu, PhotoImage
from tkinter import filedialog
#from word_counter import WordCounter
#from logger import Logger

class MainApp:
	def __init__(self, root):
		self.root = root
		self.root.title("WordWeaver")
		self.root.geometry("800x600")

	#insert word counter and logger here when ready
	self.word_counter = WordCounter()
	self.logger = Logger()
	
	#now to setup the menu bar
	self.setup_menu()

	#text region
	self.text_area = Text(self.root, wrap = 'word')
	self.text_area.pack(expand=True, fill 'both')

	#bind keys
	#TODO: have the ability to change the keys here
	self.text_area.bind("<KeyRelease>", self.update_word_count)
	
	#background setup
	#TODO: need to add in more customization here if possible
	self.setup_background()

	#
	def setup_menu(self):
		menu_bar = Menu(self.root)
		self.root.config(menu=menu_bar)
		
		file_menu = Menu(menu_bar, tearoff=0)
		file_menu.add_command(label="New", command=self.new_file)
		file_menu.add_command(label="Open...", command=self.open_file)
		file_menu.add_command(label="Save As...", command=self.save_as)
		file_menu.add_command(label="File", menu=file_menu)
	
	def setup_background(self):
		background_image = PhotoImage(file= "assets/background.png")
		background_label = Label(self.root, image=background_image)
		background_label.place(relwidth=1, relheight=1)
		self.background_image = background_image #keeps in reference

	def update_word_count(self, event = None):
		text = self.text_area.get("1.0", "end-1c")
		self.word_counter.update_counter(text)

	def new_file(self):
		self.text_area.delete("1.0", "end")
	
	def open_file(self):
		file_path = filedialog.askopenfilename()
		with open(file_path, "r") as file:
			content = file.read()
			self.text_area.delete("1.0", "end")
			self.text_area.insert("1.0", content)

	def save_as(self):
		file_path = filedialog.asksaveasfilename(defaultextension=".txt")
		with open(file_path, "w") as file:
			content = self.text_area.get("1.0", "end-1c")
			file.write(content)
