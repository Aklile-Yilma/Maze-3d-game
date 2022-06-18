from direct.showbase import DirectObject
from panda3d.core import CollisionHandlerPusher, CollisionNode, CollisionSphere


class AgentManager(DirectObject.DirectObject):
	
	def __init__(self, agent, key_mapping):
		self.__agent = agent
		self.__setup_events(key_mapping)
		self.__setup_collision()

	def __setup_events(self, key_mapping):

		events = [
				("forward", self.__agent.walk, self.__agent.stop_walking),
				("left", self.__agent.turn_left, self.__agent.stop_turning),
				("right", self.__agent.turn_right, self.__agent.stop_turning),
			]

		for event, on_press, on_up in events:
			self.accept(key_mapping.get(event), on_press)
			self.accept(
					"%s-up" % (key_mapping.get(event)),
					on_up
					)	
	
	def __setup_collision(self):

		self.collision_handler = CollisionHandlerPusher()

		from_object	= self.__agent.attachNewNode(CollisionNode("collision_node"))
		from_object.node().addSolid(CollisionSphere(0, 0, 0, 0.3))

		self.collision_handler.addCollider(from_object, self.__agent)


