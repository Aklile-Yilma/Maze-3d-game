from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import Point3, NodePath
from direct.interval.IntervalGlobal import Sequence, Func, Wait

import gltf

import os

from core.utils.keymapping import KeyMapping
from core import Config

from .agent import RhinoAgent, AgentManager
from .environment import Maze0Environment, Maze1Environment, LoadedMazeEnvironment
from .collisionHandler import CollisionHandler


class MazeRunnerGame(ShowBase):

	def __init__(self):
		super().__init__()
		
		gltf.patch_loader(self.loader)
		
		self.key_mapping = KeyMapping.load(Config.KEY_MAPPING_PATH)

		self.levels = Config.LEVELS 
		self.level = 0
		self.start_level(self.level)
	

	def increment_level(self):
		print("Cleaning Render")
		self.render.node().removeAllChildren()
		self.level = (self.level+1)%len(self.levels)
		print(self.level)
		self.start_level(self.level)

	def start_level(self, level):
		print("Starting Level %s" % (level,))
		scene = self.setup_scene(level)
		scene.get_node().reparentTo(self.render)
		
		agent = self.setup_agent("rhino")
		agent.reparentTo(self.render)
		
		self.setup_camera(agent)

		collisionHandler= CollisionHandler(agent, scene, self.render,
				self.on_finish)

	
	def setup_scene(self, level):

		config = self.levels[level]

		scene = LoadedMazeEnvironment(self.loader, config.scene, config.collision)

		return scene

		#scene = self.loader.loadModel(os.path.join(Config.RES_PATH,
		#"models/mazes/00/maze0.bam"))
		#scene.setScale(1, 1, 1)
		#scene.setPos(0, 0, 0)
		#return scene

	def setup_agent(self, agent):

		agent = RhinoAgent()
		agent_manager = AgentManager(agent, self.key_mapping)
		return agent

	def setup_camera(self, agent):
		self.disableMouse()
		
		agent_scale = agent.getScale()[0]
		
		camera_parent = NodePath("Camera Parent")
		camera_parent.reparentTo(agent)
		camera_parent.setHpr(-agent.getH(), 0, -agent.getP())

		self.camera.reparentTo(camera_parent)
		self.camera.setScale(1/agent_scale)
		self.camera.setPos(-2/agent_scale, -25/agent_scale, 6/agent_scale)
		self.camera.lookAt(*agent.getPos())

	def on_finish(self, entry):
		self.increment_level()
		print("Done: %s"%(entry,))



