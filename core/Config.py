import os


BASE_PATH = os.path.abspath(
					os.path.dirname(
						os.path.dirname(__file__)
					)
				)

RES_PATH = os.path.join(BASE_PATH, "res")

RHINO_AGENT_PATH = os.path.join(RES_PATH, "models/agents/rhino/scene.gltf") 


KEY_MAPPING_PATH = os.path.join(RES_PATH, "utils/key_mapping.txt")





