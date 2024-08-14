#Lisa Jacklin
#WordWeaver
#2024-08-14

import os
from datetime import datetime

class logger:
	def __init__(self):
		self.log_file = os.path.join("logs", "logins.log")
		self.log_login()
	
	def log_login(self):
		with open(self.log_file, "a") as log:
			log.write(f"Login at {datetime.now()}\n")


