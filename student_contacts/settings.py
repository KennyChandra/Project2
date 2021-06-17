from json import load, dump


class Settings:

	def __init__(self):

		#App Conf
		self.title = "Students Information"


		#Window Conf
		base = 75
		ratio = (16, 9)
		self.width = base*ratio[0]
		self.height = base*ratio[1]
		self.screen = f"{self.width}x{self.height}+200+10"


		#Img Conf
		self.logo = "img/logo.jpeg"


		#Contacts Dummy
		self.contacts = None
		self.load_data_from_json()


	def load_data_from_json(self):
		with open("contacts.json", "r") as file_json:
			self.contacts = load(file_json)

	def save_data_to_json(self):
		with open("contacts.json", "w") as file_json:
			dump(self.contacts, file_json)