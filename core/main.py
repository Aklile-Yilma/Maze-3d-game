from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import Point3, NodePath
from direct.interval.IntervalGlobal import Sequence, Func, Wait

import gltf

import os

from core.utils.keymapping import KeyMapping
from core import Config

from .agent import RhinoAgent, AgentManager
from .collisionHandler import CollisionHandler


class MazeRunnerGame(ShowBase):

	def __init__(self):
		super().__init__()
		
		gltf.patch_loader(self.loader)
		
		self.key_mapping = KeyMapping.load(Config.KEY_MAPPING_PATH)

		self.level = 0
		self.start_level(self.level)
		
	def start_level(self, level):
		scene = self.setup_scene(level)
		scene.reparentTo(self.render)

		agent = self.setup_agent("rhino")
		agent.reparentTo(scene)

		self.setup_camera(agent)

		collisionHandler= CollisionHandler(agent, scene)

	
	def setup_scene(self, level):

		scene = self.loader.loadModel(os.path.join(Config.RES_PATH,
		"models/mazes/00/maze0.bam"))
		scene.setScale(1, 1, 1)
		scene.setPos(0, 0, 0)
		return scene

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
		self.camera.setPos(-2/agent_scale, -30/agent_scale, 7/agent_scale)
		self.camera.lookAt(*agent.getPos())




