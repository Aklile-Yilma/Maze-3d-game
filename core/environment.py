from typing import *
from abc import ABC, abstractmethod

from panda3d.core import CollisionPolygon, Point3, CollisionSphere

class Environment(ABC):

	def __init__(self, loader, path):
		self.__node = loader.loadModel(path)

	def get_node(self):
		return self.__node

	@abstractmethod
	def get_tubes(self):
		pass



class Maze0Environment(Environment):

	def __init__(self, loader):
		super().__init__(loader, "res/models/mazes/01/maze.bam")

	def get_tubes(self):

		height = 30
		corners = [
					(100, 20), (100, 225), (57, 225), (57, 83),
					(7, 83), (7, 22), (100, 22), (100, -25), (-100, -25), 
					(-100, 22), (-7, 22), (-7, 100), (43, 100), (43, 225),
					(-100, 225), (-100, 20)
				]

		polygons = []

		for i in range(len(corners)-1):
			polygons.append(CollisionPolygon(
								Point3(*corners[i], 0), Point3(*corners[i+1], 0),
								Point3(*corners[i+1], height), Point3(*corners[i], height)
							))

		return polygons
