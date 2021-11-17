import random
from .creature import Creature

class FabriqueCreature:

	@staticmethod
	def get_creature(kind, name=None):
			if kind == "Loup":
				return Creature(kind, random.randint(3, 8), random.randint(5, 10), "wolf.png")
			elif kind == "Gobelin":
				return Creature(kind, random.randint(5, 10), random.randint(10, 15), "goblin.png")
			elif kind == "Troll":
				return Creature(kind, random.randint(10, 15), random.randint(20, 30), "troll.png")
			elif kind == "Boss":
				return Creature(kind, random.randint(25, 40), random.randint(80, 100), "boss.png")
			elif kind == "character":
				return Creature(kind, random.randint(12, 18), random.randint(20, 50), random.choice(['wizard1-final.png','wizard2-final.png']), name, 0, 0, [])
		