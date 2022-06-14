


class KeyMapping(dict):

	def save(self, path):
		file = open(path, "w")
		for value, key in self.items():
			print("%s %s" % (value, key), end="\n", file=file)
		file.close()

	@staticmethod
	def load(path) -> 'KeyMapping':
		content = open(path).read()
		mapping = KeyMapping()
		for key_map in content.split("\n")[:-1]:
			value, key = key_map.split(" ")
			mapping[value] = key
		return mapping



