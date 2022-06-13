from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import Point3

import gltf

import os

from core import Config

from .agent import MazeRunnerAgent, AgentManager

class MazeRunnerGame(ShowBase):

	def __init__(self):
		super().__init__()
		
		gltf.patch_loader(self.loader)

		self.level = 0
		self.start_level(self.level)

	def start_level(self, level):
		scene = self.setup_scene(level)
		scene.reparentTo(self.render)

		agent = self.setup_agent("rhino")
		agent.reparentTo(self.render)
	
	def setup_scene(self, level):
		scene = self.loader.loadModel(os.path.join(Config.RES_PATH,
		"models/mazes/00/maze0.bam"))
		scene.setScale(1, 1, 1)
		scene.setPos(0, 0, 0)
		return scene

	def setup_agent(self, agent):

		agent = MazeRunnerAgent(
					os.path.join(Config.RES_PATH,"models/agents/rhino/scene.gltf"),
					step_size = 30,
					step_duration = 10
				)
		agent.setScale(0.0003, 0.0003, 0.0003)
		agent.setPos(1, 5, -1)
		agent.setHpr(90, 270, 0)
		
		#agent.posInterval(5, Point3(1, 100, -1), startPos=(1, 0, -1))
		#agent.loop("walk")
		agent_manager = AgentManager(agent)

		return agent


