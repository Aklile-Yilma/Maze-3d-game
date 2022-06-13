
import os
import sys



class MazeRunnerApp:


	def setup(self):
		from .Config import BASE_PATH
		sys.path.append(BASE_PATH)

	def run(self):
		
		from core.main import MazeRunnerGame
		game = MazeRunnerGame()
		game.run()

	def start(self):
		self.setup()
		self.run()

