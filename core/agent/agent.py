 

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

	def __init__(self, path, walk_path=None, step_size=1, step_duration=1):
		
		if walk_path is None:
			walk_path = path
		super().__init__(path, {'walk': walk_path})
		
		self.__step_size = step_size
		self.__step_duration = step_duration
		
		self._initial_setup()
		self._state = self._get_initial_state()

	def _get_initial_state(self):
		return {
				'forward': False
				}

	def _get_initial_hpr(self):
		return (0,0,0)
	
	def _get_initial_scale(self):
		return (1, 1, 1)

	def _initial_setup(self):
		self.setHpr(*self._get_initial_hpr())
		self.setScale(*self._get_initial_scale())

	def _get_forward_vector(self):
		h = self.getH() - self._get_initial_hpr()[0]
		return Point3(math.sin(h), math.cos(h), 0)

	def walk(self):
		self._state["forward"] = True
		self.loop("walk")
		Sequence(
			Func(self.__keep_walking)
		).start()

	def stop_walking(self):
		self._state["forward"] = False
		self.stop()
	
	def __keep_walking(self):
		
		if not self._state["forward"]:
			return

		Sequence(
				self.__walk_step(),
				Func(self.__keep_walking)
			).start()


	def __walk_step(self):
		final_position = (self._get_forward_vector() * self.__step_size) + self.getPos()
		pos_interval = self.posInterval(self.__step_duration, final_position, startPos=self.getPos())
		return pos_interval
	

class RhinoAgent(MazeRunnerAgent):

	def __init__(self):
		super(RhinoAgent, self).__init__(
							Config.RHINO_AGENT_PATH,
							step_size = 1,
							step_duration = 0.4
						)
	

	def _get_initial_scale(self):
		return (0.0005, 0.0005, 0.0005)

	def _get_initial_hpr(self):
		return (90, 270, 0)

	def _initial_setup(self):
		super()._initial_setup()
		self.play("walk")
		self.stop()
