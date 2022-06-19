 

from direct.actor.Actor import Actor
from panda3d.core import Point3
from direct.interval.IntervalGlobal import Sequence, Func, Wait

import time
import math

from core import Config


class Agent(Actor):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


class MazeRunnerAgent(Agent):

	def __init__(
			self, 
			path, 
			walk_path=None, 
			step_size=1, 
			step_duration=1,
			rotation_size=1,
			rotation_duration=1
		):
		
		if walk_path is None:
			walk_path = path
		super().__init__(path, {'walk': walk_path})
	
		self.__traverser = None

		self.__step_size = step_size
		self.__step_duration = step_duration
		self.__rotation_size = rotation_size
		self.__rotation_duration = rotation_duration
	
		self._initial_setup()
		self._state = self._get_initial_state()

	def _get_initial_state(self):
		return {
				'forward': False,
				'left': False,
				'right': False
				}

	def _get_initial_hpr(self):
		return (0,0,0)
	
	def _get_initial_scale(self):
		return (1, 1, 1)

	def _initial_setup(self):
		self.setHpr(*self._get_initial_hpr())
		self.setScale(*self._get_initial_scale())

	def _get_forward_vector(self):
		h = self.getTrueH()
		return Point3(-math.sin(math.radians(h)), math.cos(math.radians(h)), 0)

	def set_traverser(self, traverser):
		if self.__traverse is None:
			return
		self.__traverser = traverser

	def setH(self, h):
		super().setH(self._get_initial_hpr()[0] + h)

	def getTrueH(self):
		return super().getH() - self._get_initial_hpr()[0]

	def walk(self):
		self._state["forward"] = True
		self.loop("walk")
		Sequence(
			Func(self.__keep_walking)
		).start()

	def stop_walking(self):
		self._state["forward"] = False
		self.stop()

	def __traverse(self):
		if self.parent is None:
			return
		self.__traverser.traverse(self.parent)

	def __keep_walking(self):
		
		if not self._state["forward"]:
			return

		Sequence(
				self.__walk_step(),
				Func(self.__traverse),
				Func(self.__keep_walking),
			).start()


	def __walk_step(self):
		final_position = (self._get_forward_vector() * self.__step_size) + self.getPos()
		#print("Final Position: %s" % (final_position,))
		pos_interval = self.posInterval(self.__step_duration, final_position, startPos=self.getPos())
		#print("Forward Vector: %s" % self._get_forward_vector())
	
		return pos_interval

	def turn_left(self):
		self._state["left"] = True
		self.__turn(1)
	
	def turn_right(self):
		self._state["right"] = True
		self.__turn(-1)

	def stop_turning(self):
		self._state["right"] = self._state["left"] = False

	def __turn(self, direction):
		
		key = "left"
		if direction == -1:
			key = "right"

		if not self._state[key]:
			return
	
		Sequence(
				self.hprInterval(
							self.__rotation_duration,
							self.__calc_turn_step(direction)
						),
				Func(self.__turn, direction)
			).start()
	
	def __calc_turn_step(self, direction):

		final_hpr = self.getHpr()
		print("Initial HPR: %s" % final_hpr)
		final_hpr[0] = final_hpr[0] + self.__rotation_size * direction
		print("Final HPR: %s" %final_hpr)
		return final_hpr




class RhinoAgent(MazeRunnerAgent):

	def __init__(self):
		super(RhinoAgent, self).__init__(
							Config.RHINO_AGENT_PATH,
							step_size = 0.3,
							step_duration = 0.0001,
							rotation_size = 5,
							rotation_duration = 0.1
						)
	

	def _get_initial_scale(self):
		return (0.0005, 0.0005, 0.0005)

	def _get_initial_hpr(self):
		return (90, -90, 0)

	def _initial_setup(self):
		super()._initial_setup()
		self.play("walk")
		self.stop()
