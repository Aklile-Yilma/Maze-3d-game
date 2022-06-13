 

from direct.actor.Actor import Actor
from panda3d.core import Point3
from direct.interval.IntervalGlobal import Sequence, Func, Wait

import time

class Agent(Actor):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


class MazeRunnerAgent(Agent):

	def __init__(self, path, walk_path=None, step_size=1, step_duration=1):
		if walk_path is None:
			walk_path = path
		self.__step_size = step_size
		self.__step_duration = step_duration
		self.__walking_state = False
		super().__init__(path, {'walk': walk_path})
	

	def get_orientation(self):
		return Point3(0, 1, 0)

	def walk(self):
		self.__walking_state = True
		self.loop("walk")
		sequence = Sequence(
				self.walk_step(),
				Func(self.__keep_walking)
			)
		sequence.start()
		#self.__keep_walking(sequence)
		#self.stop()
	
	def __keep_walking(self):
		
		if not self.__walking_state:
			sequence.append(Wait(self.__step_duration))
			sequence.append(Func(self.stop))
		print("Adding Step")
		Sequence(
				self.walk_step(),
				Func(self.__keep_walking)
			).start()


	def walk_step(self):
		final_position = (self.get_orientation() * self.__step_size) + self.getPos()
		print("Walking %s - %s in 10s" % (self.getPos(), final_position))
		pos_interval = self.posInterval(self.__step_duration, final_position, startPos=self.getPos())
		return pos_interval
