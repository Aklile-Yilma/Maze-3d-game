import os

from dataclasses import dataclass


@dataclass
class LevelConfig:
	
	scene: str
	collision: str
	agent: str


BASE_PATH = os.path.abspath(
					os.path.dirname(
						os.path.dirname(__file__)
					)
				)

RES_PATH = os.path.join(BASE_PATH, "res")

RHINO_AGENT_PATH = os.path.join(RES_PATH, "models/agents/rhino/scene.gltf") 


KEY_MAPPING_PATH = os.path.join(RES_PATH, "utils/key_mapping.txt")


LEVELS = [
		LevelConfig(
			os.path.join(RES_PATH, "models/mazes/01/maze.bam"),
			os.path.join(RES_PATH, "models/mazes/01/collision_nodes.txt"),
			RHINO_AGENT_PATH
		),
		LevelConfig(
			os.path.join(RES_PATH, "models/mazes/02/maze.bam"),
			os.path.join(RES_PATH, "models/mazes/02/collision_nodes.txt"),
			RHINO_AGENT_PATH
		)
	]


