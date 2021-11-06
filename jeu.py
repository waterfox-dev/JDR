from fabriquecreature import FabriqueCreature
import random

class Jeu:
	
	def __init__(self, user=None):
		self.player = user		

	def menu(self):

		try:
			choice = int(input("\nChoissisez une option :\n1 - Créer un personnage pour commencer une nouvelle partie\n2 - Combattre une créature\n3 - Afficher mon score\n4 - Exit\n--> "))
			assert choice >=1 and choice <=4
		except (AssertionError, ValueError):
			print("Veuillez choisir une valeur correcte.")
			Jeu.menu(self)

		if choice == 1:
			if self.player != None:
				print(f"Vous avez déjà un personnage : {self.player.name}")
			else:
				self.player = Jeu.CreatePlayer(self.player)
			Jeu.menu(self)
		
		elif choice == 2:
			if self.player == None:
				print("Vous ne pouvez pas combattre sans avoir créé un personnage au préalable ou avec un personnage décédé.")
			else:
				Jeu.FightCreature(self.player)
			Jeu.menu(self)

		elif choice == 3:
			if self.player == None:
				print("Vous n'avez pas créé de personnage.")
			else:
				print(f"Votre score est de {self.player.score}")
			Jeu.menu(self)
				
		elif choice == 4:
			exit()

	@staticmethod
	def CreatePlayer(player):
		name = input("Quel nom voulez vous donner à votre personnage ? ")
		player = FabriqueCreature.get_creature("perso", name)
		print(f"TADAAM !! {name} vient de naitre. Il a les caractéristiques suivantes : {player.strength} de force et {player.hp} points de vie")
		return player

	@staticmethod
	def FightCreature(player):
		
		#Determination du monstre à combattre
		monster_type = ["loup", "gobelin", "troll"]
		monster = FabriqueCreature.get_creature(monster_type[random.randint(0,2)])
		print(f"Vous affrontez un {monster.kind.capitalize()}, avec une force de {monster.strength}, et une vie égale à {monster.hp}pv.")
		
		#Calcul des attaques
		AttP = player.strength + random.randint(1, 10)
		AttC = monster.strength + random.randint(1, 10)
		
		#Combat seulement tant que la vie des deux est supérieur à 0
		while monster.hp > 0 and player.hp > 0:
			
			#Si l'attaque du perso est plus forte que celle du monstre
			if AttP > AttC:
				monster.hp-=(AttP - AttC)
				print(f"{player.name} est plus rapide. Il inflige {AttP - AttC} à {monster.kind}.\nIl lui reste {monster.hp} PV.")
			
			#Si l'attaque du monstre est plus forte que celle du perso
			elif AttC < AttP:
				player.hp-=(AttC - AttP)
				print(f"{monster.kind} est plus rapide. Il inflige {AttP - AttC} à {player.name}.\nIl lui reste {player.hp} PV.")

			#Si l'attaque est égal
			else:
				print("Aucun des deux n'a réussi à prendre l'avantage sur ce tour !")
				AttP = player.strength + random.randint(1, 10)
				AttC = monster.strength + random.randint(1, 10)
				
		
		#Si le joueur n'a plus de vie
		if player.hp <= 0:
			print(f"GAMER OVER :/ Votre brave héros a cédé sous les coups de l'ennemi. Il restait {monster.hp} PV à {monster.kind.capitalize()}")
			exit()
		
		#Si le monstre n'a plus de vie
		else:
			score = 1 if monster.kind == "loup" else 2 if monster.kind == "gobelin" else 3 if monster.kind == "troll" else None				
			player.score += score
			print(f"Point gagnés : {str(score)}\nVICTOIRE !!! Vous avez gagné le combat ! Votre score est maintenant de {player.score} point(s).")
			return
		