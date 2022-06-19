from direct.showbase.ShowBase import ShowBase
from pandac.PandaModules import CollisionTraverser, CollisionHandlerPusher, CollisionHandlerQueue
from pandac.PandaModules import CollisionNode, CollisionSphere, CollisionCapsule
from pandac.PandaModules import Point3


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

		self.agent.set_traverser(self.traverser)

		for i,tube in enumerate(self.environment.get_tubes()):
			env_node = CollisionNode(f'tube_{i}')
			env_node.addSolid(tube)
			env_node_path = self.render.attachNewNode(env_node)
			#env_node_path.show()

		#self.traverser.showCollisions(self.render)

