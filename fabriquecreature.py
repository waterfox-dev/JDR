import random
from creature import Creature

class FabriqueCreature:

	@staticmethod
	def get_creature(kind, name=None):
			if kind == "loup":
				return Creature(kind, random.randint(3, 8), random.randint(5, 10))
			elif kind == "gobelin":
				return Creature(kind, random.randint(5, 10), random.randint(10, 15))
			elif kind == "troll":
				return Creature(kind, random.randint(10, 15), random.randint(20, 30))
			elif kind == "perso":
				return Creature(kind, random.randint(12, 18), random.randint(20, 50), name, 0)