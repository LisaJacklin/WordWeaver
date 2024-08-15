#Lisa Jacklin
#WordWeaver
#2024-08-14

class WordCounter:
	def __init__(self):
		self.word_count = 0
		
	def update_count(self, text):
		self.word_count = len(text.split())
		print(f"Current word count: {self.word_count}")


