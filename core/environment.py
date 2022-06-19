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

<<<<<<< HEAD
=======
	@abstractmethod
	def get_finish_line(self):
		pass

>>>>>>> d8db92c (Final Touches)


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
<<<<<<< HEAD
=======
	
	def get_finish_line(self):
		return CollisionPolygon(
				Point3(45, 225, 0), Point3(53, 225, 0),
				Point3(53, 225, 30), Point3(45, 225, 30)
			)
	
class Maze1Environment(Maze0Environment):
	pass


class LoadedMazeEnvironment(Environment):
	
	def __init__(self, loader, scene_path, collision_path):
		super().__init__(loader, scene_path)
		self.push_corners, self.height, self.finish	= self.__load_collision(collision_path)
		print(self.push_corners, self.height, self.finish, sep="-------")

	def __parse_corners(self, content):
		corners = []
		for corner_str in content.split("|"):
			corners.append(tuple([float(c) for c in corner_str.split(",")]))
		print(corners)
		return corners

	def __load_collision(self,path):
		content = open(path).read()
		pusher, height, finish = content.split("\n")[:-1]
		return self.__parse_corners(pusher), float(height) ,self.__parse_corners(finish)

	def __create_polygons(self, corners, height):
		polygons = []

		for i in range(len(corners)-1):
			polygons.append(CollisionPolygon(
								Point3(*corners[i], 0), Point3(*corners[i+1], 0),
								Point3(*corners[i+1], height), Point3(*corners[i], height)
							))

		return polygons

	def get_tubes(self):
		return self.__create_polygons(self.push_corners, self.height)

	def get_finish_line(self):
		return self.__create_polygons(self.finish, self.height)[0]



>>>>>>> d8db92c (Final Touches)
