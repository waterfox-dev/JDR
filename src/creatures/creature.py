
class Creature:

	"""
	Créer un objet qui a comme attributs tous les composants d'une créature ou d'un personnage.
	"""
	def __init__(self, kind, strength, health, sprite, name=None, score=None, coins=None, items=None):
		self.kind = kind
		self.name = name
		self.strength = strength
		self.hp = health
		self.sprite = sprite
		self.score = score
		self.coins = coins
		self.items = items