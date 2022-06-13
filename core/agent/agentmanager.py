from direct.showbase import DirectObject


class AgentManager(DirectObject.DirectObject):
	
	def __init__(self, agent):
		self.__agent = agent
		self.__setup_events()
		
	def __setup_events(self):
		self.accept("arrow_up", self.__agent.walk)
		#self.accept("arrow_up-up", self.__agent.stop_walking)
		self.accept("k", self.__test)

	def __test(self):
		print("Soemthing pressed")
