#Lisa Jacklin
#WordWeaver
#2024-08-14

from tkinter import Frame, Text, Menu, PhotoImage, Label
from tkinter import filedialog
from word_counter import WordCounter
from logger import logger

class MainApp:
	def __init__(self, root):
		self.root = root
		self.root.title("WordWeaver")
		self.root.geometry("800x600")
