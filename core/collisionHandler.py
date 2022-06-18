from direct.showbase.ShowBase import ShowBase
from pandac.PandaModules import CollisionTraverser, CollisionHandlerPusher
from pandac.PandaModules import CollisionNode, CollisionSphere
from pandac.PandaModules import Point3


class CollisionHandler():
    def __init__(self, agent, environmentModel):
        self.collisionNodes=[]
        self.environmentModel= environmentModel
        self.agent = agent

        self.traverser = CollisionTraverser()
        self.pusher = CollisionHandlerPusher()

    def handle():

        agentNode = CollisionNode('agent_collision_node')
        agentNode.reparentTo(self.agent)
        agentNode.addSolid(CollisionSphere())


        for i,tube in enumerate(self.environmentModel.getTubes()):
            env_node = CollisionNode(f'tube_{i}')
            env_node.addSolid(tube)
            env_node.reparentTo(self.environmentModel)
            self.collisionNodes.append(env_node)
            self.pusher.addCollider(env_node, self.environmentModel)
            self.traverser.addCollider(env_node, self.pusher)

        
        self.traverser.addCollider(agentNode, self.pusher)
        self.pusher.addCollider(agentNode, self.agent)
    


        











