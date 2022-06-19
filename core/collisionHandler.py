<<<<<<< HEAD
from direct.showbase.ShowBase import ShowBase
from pandac.PandaModules import CollisionTraverser, CollisionHandlerPusher, CollisionHandlerQueue
=======
from direct.showbase.ShowBase import ShowBase, DirectObject
from pandac.PandaModules import CollisionTraverser, CollisionHandlerPusher, \
CollisionHandlerQueue,CollisionHandlerEvent 
>>>>>>> d8db92c (Final Touches)
from pandac.PandaModules import CollisionNode, CollisionSphere, CollisionCapsule
from pandac.PandaModules import Point3


<<<<<<< HEAD
class CollisionHandler:
	
	def __init__(self, agent, environment, render):
		self.environment= environment
		self.agent = agent
		self.render = render

		self.traverser = CollisionTraverser()
		self.pusher = CollisionHandlerPusher()
		self.pusher.setHorizontal(False)

	def handle(self):

		agent_node_path	= self.agent.attachNewNode(CollisionNode("agent_collision_node"))
		agent_node_path.setScale(1/self.agent.getScale()[0])
		agent_node_path.setHpr(-self.agent.getH(), 0, -self.agent.getP())
		agent_node_path.node().addSolid(CollisionSphere(-1, 0, 1,1))
		
		#agent_node_path.show()
		self.pusher.addCollider(agent_node_path, self.agent)
		self.traverser.addCollider(agent_node_path, self.pusher)
=======
class CollisionHandler(DirectObject.DirectObject):
	
	def __init__(self, agent, environment, render, on_finish):
		self.environment= environment
		self.agent = agent
		self.render = render
		self.on_finish = on_finish
		self.__setup()

	def __setup_agent_node(self, agent):
		agent_node_path	= self.agent.attachNewNode(CollisionNode('agent_collision_node'))
		agent_node_path.setScale(1/self.agent.getScale()[0])
		agent_node_path.setHpr(-self.agent.getH(), 0, -self.agent.getP())
		agent_node_path.node().addSolid(CollisionSphere(-1, 0, 1, 1))
		return agent_node_path

	def __setup_push_collision(self):

		for i,tube in enumerate(self.environment.get_tubes()):
			env_node = CollisionNode(f'tube_{i}')
			env_node.addSolid(tube)
			env_node_path = self.render.attachNewNode(env_node)
			#env_node_path.show()

	def __setup_finish_collision(self, handler):

		finish_node = CollisionNode("finish_line")
		finish_line = self.environment.get_finish_line()
		finish_line.setTangible(False)
		finish_node.addSolid(finish_line)
		finish_node_path = self.render.attachNewNode(finish_node)
		finish_node_path.show()
		
		handler.addInPattern('%fn-into-%in')
		self.accept("agent_collision_node-into-finish_line", self.on_finish)

	def __setup(self):

		traverser = CollisionTraverser()
		handler = CollisionHandlerPusher()
		handler.setHorizontal(False)
		
		agent_node_path = self.__setup_agent_node(self.agent)

		handler.addCollider(agent_node_path, self.agent)
		traverser.addCollider(agent_node_path, handler)
		self.agent.set_traverser(traverser)
>>>>>>> d8db92c (Final Touches)

		self.agent.set_traverser(self.traverser)

<<<<<<< HEAD
		for i,tube in enumerate(self.environment.get_tubes()):
			env_node = CollisionNode(f'tube_{i}')
			env_node.addSolid(tube)
			env_node_path = self.render.attachNewNode(env_node)
			#env_node_path.show()

		#self.traverser.showCollisions(self.render)
=======
		self.__setup_push_collision()
		self.__setup_finish_collision(handler)
	

		#traverser.showCollisions(self.render)
>>>>>>> d8db92c (Final Touches)

