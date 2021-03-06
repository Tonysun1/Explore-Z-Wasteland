from tkinter import Tk, Label, Button
from app.Game import init_game
import app.main_game


class IntroGUI:
	def __init__(self, master):
		self.master = master
		master.title("Welcome to Explore-Z-Wasteland")

		self.label = Label(master, text="Explore-Z-Wasteland")
		self.label.pack()

		self.start_game = Button(master, text='Sign in', command=self.start_game)
		self.start_game.pack()

		self.exit_game = Button(master, text='Sign up', command=self.exit_game)
		self.exit_game.pack()

	def start_game(self):
		init_game()

	def exit_game(self):
		# close the window
		pass


def init():
	# TODO: change to pygame intro page
	root = Tk()
	IntroGUI(root)
	root.mainloop()
