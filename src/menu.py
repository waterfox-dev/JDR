import pyglet
import random

from tkinter import * 
from tkinter.messagebox import *
from PIL import ImageTk, Image

from .utils.file_path import FilePath
from .utils.saver import save_character
from .creatures.fabriquecreature import FabriqueCreature
from .score_window import ScoreWindow
import src.battle_window as battle_window
import src.shop_window as shop_window

class MenuWindow:

    """
    Fonction qui, au moment de quitter le jeu, enregistre toutes les données du joueur dans la base de données.
    """
    def QuitGame(self):
        save_character(name=self.player.name, strength=self.player.strength, health=self.player.hp, character_sprite=self.player.sprite, score=self.player.score, coins=self.player.coins, items=self.player.items)
        self.screen.destroy()

    """
    Fonction qui permet de lancer la page de combat. En créant un créature aléatoire.
    Vérifie qu'il reste de la vie au joueur, dans le cas contraire, lui renvoie une page qui lui explique ce qu'il peut faire.
    """
    def GoToFight(self):
        player = self.player
        self.screen.destroy()
        if player.hp > 0:
            creature = FabriqueCreature.get_creature(random.choice(["Loup", "Gobelin", "Troll"]))
            battle_window.BattleWindow(player, creature)
        else:
            battle_window.NoLifeToFight(player)

    """
    Fonction qui ouvre la page de magasin.
    """
    def GoToShop(self):
        player = self.player
        self.screen.destroy()
        shop_window.ShopWindow(player)

    """
    Fonction qui ouvre la page de score.
    """
    def GoToScore(self):
        player = self.player
        self.screen.destroy()
        ScoreWindow(player)

    def __init__(self, player):

        """
		Paramètres de la page TKinter :
        - Titre
        - Icône
        - Taille
        - Couleur de fond
	    """
        self.screen = Tk()
        self.screen.title("Menu de WizardsRevenge")
        #self.screen.iconbitmap(FilePath.get("assets", "icon", "grimoire.ico"))
        self.screen.geometry("1536x845")
        self.player = player
        
        """
		Ajout d'une police externe grâce au module pyglet
	    """
        pyglet.font.add_file(FilePath.get("assets", "fonts", "Letters for Learners.ttf"))

        """
        Création d'un canvas qui sert de fond de page.
        Avec ajout d'une image pixelisée comme décor.
        """
        CAN_Zone = Canvas(self.screen, height=845, width=1536)
        img = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "PixelBG2.png")))
        CAN_Sprite_Image = CAN_Zone.create_image(0, 0, image=img, anchor="nw")
        
        #Création d'un cadre
        Frame1 = Frame(CAN_Zone, height=120, width=300, bg="#333399")
        
        """
		Création et placement des différents boutons qui se trouvent sur la page de Menu : Combattre; Magasin; Score; Quitter.
	    """
        ButtonFight = Button(Frame1, text="Combattre !", font=("Letters for Learners", 20), height=2, width=15, bg="#4e5180", fg="white", command=self.GoToFight)
        ButtonFight.grid(column=0, row=0, padx=30, pady=50)
        
        ButtonShop = Button(Frame1, text="Magasin", font=("Letters for Learners", 20), height=2, width=15, bg="#4e5180", fg="white", command=self.GoToShop)
        ButtonShop.grid(column=1, row=1, padx=30, pady=50)
        
        ButtonScore = Button(Frame1, text="Score", font=("Letters for Learners", 20), height=2, width=15, bg="#4e5180", fg="white", command=self.GoToScore)
        ButtonScore.grid(column=2, row=0, padx=30, pady=50)
        
        ButtonQuit = Button(CAN_Zone, text="Quitter", font=("Letters for Learners", 20), height=2, width=15, bg="#313350", fg="white", command=self.QuitGame)

        """
		Placement des boutons.
	    """
        ButtonWindowQuit = CAN_Zone.create_window(1450, 90, anchor="ne", window=ButtonQuit)
        ButtonsWindow = CAN_Zone.create_window(130, 280, anchor="nw", window=Frame1)

        """
		Création d'un cadre de titre pour annoncer le menu.
	    """
        MessageRectangle = CAN_Zone.create_rectangle(120, 70, 1035, 190, width=8, fill="#7d4e80", outline="#313350")
        MessageText = CAN_Zone.create_text(580, 130, text=f"Menu de WizardsRevenge", font=("Letters for Learners", 75, "bold"), fill="white")

        #Initialisation du canvas dans la page avec tous ses composants
        CAN_Zone.pack()

        #Création de la page
        self.screen.mainloop()