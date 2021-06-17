import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from settings import Settings
from appPage import AppPage


class Window(tk.Tk):

	def __init__(self, App):
		self.app = App
		self.settings = App.settings
		self.count = 0


		super().__init__()
		self.title(self.settings.title)
		self.geometry(self.settings.screen)
		self.resizable(0,0)

		self.create_admin()
		self.create_menu()
		self.create_container()

		self.pages = {}
		self.create_appPage()

	def create_menu(self):
		self.menu_bar = tk.Menu(self)
		self.configure(menu=self.menu_bar)

		self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
		self.file_menu.add_command(label="New Contact", command=self.app.open_file)
		self.file_menu.add_command(label="Exit", command=self.app.exit)

		self.help_menu = tk.Menu(self.menu_bar, tearoff=False)
		self.help_menu.add_command(label="About", command=self.app.about)

		self.menu_bar.add_cascade(label='File', menu=self.file_menu)
		self.menu_bar.add_cascade(label='Help', menu=self.help_menu)

	def create_admin(self):
		self.frameaaa = tk.Frame(self, bd = 350)
		self.frameaaa.pack(fill="both", expand = True)
		self.widgetss()


	def widgetss(self):

		self.userpassword = tk.Label(self.frameaaa, text="Password   : ", font=("Arial", 12))
		self.userpassword.grid(ipadx= 180, column=100)
 
		self.passEntry = tk.Entry(self.frameaaa, show="*")
		self.passEntry.grid(row=10, column = 100, pady = 20)
 	
		self.passbtn = tk.Button(self.frameaaa, text="LOGIN", command = self.clickedd)
		self.passbtn.grid(row = 14, column = 100)
		
	def clickedd(self):	

		if self.passEntry.get() == "cheese":
			self.frameaaa.destroy()

		else:
			self.count = self.count + 1
			if self.count == 3:
				sys.exit()


	def create_container(self):
		self.container = tk.Frame(self)
		self.container.pack(fill="both", expand=True)

	def create_appPage(self):
		self.pages["appPage"] = AppPage(self.container, self.app)




class ContactApp:

	def __init__(self):
		self.settings = Settings()
		self.window = Window(self)

	def about(self):
		a = tk.Toplevel()
		a.geometry("420x420")
		a.title("About this App")
		label = tk.Label(a, text="This App is made to save students information")
		label.pack()

	def open_file(self):
		print("Unavailable")

	def exit(self):
		respond = messagebox.askyesnocancel("Exit Program", "Are you sure to close the program ?")
		if respond:
			sys.exit()

	def run(self):
		self.window.mainloop()

if __name__ == '__main__':
	myContactApp = ContactApp()
	myContactApp.run()