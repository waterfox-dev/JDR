import json
import pyglet

from tkinter import * 
from tkinter.messagebox import *
from PIL import ImageTk, Image

from .utils.file_path import FilePath
from .menu import MenuWindow

class NewPerso:

    """
    Fonction qui renvoie à la page du Menu.
    """
    def change_window(self):
        self.screen.destroy()
        MenuWindow(self.player)

    """
    Fonction qui retourne le sprite qui correspond à l'utilisateur connecté.
    """
    def get_sprite(self):
        with open(FilePath.get("data", "registration.json"), "r") as r:
            data = json.load(r)
            for username in data :
                if username == self.player.name:
                    return data[username]["character_sprite"]

    
    def __init__(self, player):

        """
		Paramètres de la page TKinter :
        - Titre
        - Taille
        - Couleur de fond
	    """
        self.screen = Tk()
        self.screen.title("Création d'un nouveau personnage")
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
        IMG_Image = PhotoImage(file=FilePath.get("assets", "images", "PixelBG.png"))
        CAN_Zone = Canvas(self.screen, height=845, width=1536)
        CAN_Zone_Image = CAN_Zone.create_image(0, 0, image=IMG_Image, anchor="nw")
        
        """
        Insertion du sprite que renvoie la fonction get_sprite.
        """
        sprite_player = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", self.get_sprite())))
        sprite_player = sprite_player._PhotoImage__photo.zoom(12)
        CAN_Sprite_Image = CAN_Zone.create_image(768, 200, image=sprite_player, anchor="n")
        
        #Texte complémentaire
        congratulation = CAN_Zone.create_text(750, 60, text="Bravo ! Tu viens de creer ton personnage.", font=("Roman", 40), fill="#6d1212")
        charaName = CAN_Zone.create_text(750, 130, text=f"Bienvenue {self.player.name}", font=("Roman", 40), fill="#6d1212")
        
        """
        Insertion d'un cadre contenant les statistiques de force ainsi que de vie.
        """
        stats = CAN_Zone.create_rectangle(145, 300, 445, 446, width=2)
        statsStrength = CAN_Zone.create_text(295, 340, text=f"Force : {self.player.strength} Mana", font=("Roman", 30), fill="#6d1212")
        statsHp = CAN_Zone.create_text(295, 400, text=f"Vie : {self.player.hp} Hp", font=("Roman", 30), fill="#6d1212")

        #Création du bouton pour retourner au menu
        ContinueButton = Button(CAN_Zone, text="Continuer", fg="white", font=("Letters for Learners", 25), command=self.change_window, height=1, width=10, bg="#8601af")
        window = CAN_Zone.create_window(20, 20, anchor="nw", window=ContinueButton)

        #Initialisation du canvas dans la page avec tous ses composants
        CAN_Zone.pack()

        #Création de la page
        self.screen.mainloop()