import random

class Jeu:
	
	def __init__(self, player, creature):
		self.player = player
		self.creature = creature	

	@staticmethod
	def FightCreature(player, creature):
		
		#Calcul des attaques
		AttP = player.strength + random.randint(1, 10)
		AttC = creature.strength + random.randint(1, 10)
			
		DifferentStrength = True
		while DifferentStrength:
		
			#Si l'attaque du perso est plus forte que celle du monstre
			if AttP > AttC:
				creature.hp-=(AttP - AttC)
				return creature
			
			#Si l'attaque du monstre est plus forte que celle du perso
			elif AttP < AttC:
				player.hp-=(AttC - AttP)
				return player

			#Si l'attaque est égal
			else:
				AttP = player.strength + random.randint(1, 10)
				AttC = creature.strength + random.randint(1, 10)