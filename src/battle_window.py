import random
import json
import pyglet
import time

from tkinter import * 
from tkinter.messagebox import *
from PIL import ImageTk, Image

from .utils.saver import save_character
from .utils.jeu import Jeu
from .utils.file_path import FilePath
import src.go_or_win as go_or_win
import src.menu as menu
import src.inventory_window as inventory_window

class BattleWindow:

    """
    Fonction qui permet d'ouvrir la page d'inventaire.
    """
    def open_inventory(self):
        player = self.player
        creature = self.creature
        self.screen.destroy()
        inventory_window.InventoryWindow(player, creature)

    """
    Fonction qui gère le bouton pour s'échapper, qui possède une réussite de 1 chance sur 3.
    Réussite augmenter à 100% si un portail est utilisé.
    """
    def to_escape(self):
        chance = [True, False, False]
        #Vérifie si un item est utilisé ou si le joueur réussit à fuir
        if self.item == "Portal" or random.choice(chance):
            player = self.player
            save_character(name=self.player.name, strength=self.player.strength, health=self.player.hp, character_sprite=self.player.sprite, score=self.player.score, coins=self.player.coins, items=self.player.items)
            self.screen.destroy()
            menu.MenuWindow(player)
        else:
            #Fait perdre un nombre de hp au joueur entre 1 et 3
            lost_hp = random.randint(1,3)
            #Affiche un texte dit par le monstre
            self.display_fail_escape(True, lost_hp)
            self.player.hp -= lost_hp
            player = self.player
            #Vérifie si le joueur à encore de la vie
            if self.player.hp > 0:
                self.CAN_Zone.itemconfigure(self.statsHp, text=f"Vie : {self.player.hp} Hp")
            else:
                self.screen.destroy()
                go_or_win.GameOverWindow(player, self.creature.kind)

    """
    Fonction qui permet au monstre de parler dans la cas d'une fuite échoué du joueur.
    """
    def display_fail_escape(self, state, lost_hp=None):
        if state:
            self.fail_escape_frame = self.CAN_Zone.create_rectangle(855, 260, 1095, 390, width=3, fill="#b4f3fa")
            self.fail_escape_text1 = self.CAN_Zone.create_text(975, 285, text="Tu as voulu fuir ?", font=("Letters for Learners", 23), fill="#6d1212")
            self.fail_escape_text2 = self.CAN_Zone.create_text(975, 340, text=f"Pour le peine tu\nvas perdre {lost_hp} Hp", font=("Letters for Learners", 23), fill="#6d1212")
        else:
            try:
                self.CAN_Zone.delete(self.fail_escape_frame, self.fail_escape_text1, self.fail_escape_text2)
            except AttributeError:
                pass

    """
    Fonction qui retourne le sprite qui correspond à l'utilisateur connecté.
    """
    def get_sprite(self):
        with open(FilePath.get("data", "registration.json"), "r") as r:
            data = json.load(r)
            for username in data :
                if username == self.player.name:
                    return data[username]["character_sprite"]

    """
    Fonction qui orchestre un combat entre le joueur et le monstre.
    Utilise le fichier jeu et la staticmethod FightCreature.
    """
    def fight(self):
        self.display_fail_escape(False)
        FightLoser = Jeu.FightCreature(self.player, self.creature)
        #Vérifie si le perdant est le joueur
        if FightLoser.kind == "character":
            self.player.hp = FightLoser.hp
            #Vérifie si le joueur à encore de la vie
            if self.player.hp <= 0:
                self.player.hp = 0
                player = self.player
                self.screen.destroy()
                #Envoie sur la page de GameOver
                go_or_win.GameOverWindow(player, self.creature.kind)
            #Sinon actualise les stats
            else:
                self.CAN_Zone.itemconfigure(self.statsHp, text=f"Vie : {self.player.hp} Hp")
        #Si c'est la créature qui perd
        else:
            self.creature.hp = FightLoser.hp
            #Vérifie si la créature à encore de la vie
            if self.creature.hp <= 0:
                player = self.player
                #self.CAN_Zone.itemconfigure(self.CAN_SpriteCreature_Image, image=self.imgExplosion)
                #self.CAN_Zone.delete(self.statsCreature, self.statsNameCreature, self.statsStrengthCreature, self.statsHpCreature)
                #time.sleep(4)
                self.screen.destroy()
                #Envoie sur la page de Victoire
                go_or_win.WinWindow(player, self.creature.kind, self.item)
            #Sinon actualise les stats
            else:
                self.CAN_Zone.itemconfigure(self.statsHpCreature, text=f"Vie : {self.creature.hp} Hp")


    def __init__(self, player, creature, item_for_fight=None) :
        
        """
		Paramètres de la page TKinter :
        - Titre
        - Taille
        - Couleur de fond
	    """
        self.screen = Tk() 
        self.screen.title("Combat ton adversaire !")
        self.screen.geometry("1536x800")
        self.screen.resizable(width=False, height=False)
        self.player = player
        self.creature = creature
       
        #Récupère un potentiel item utilisé
        self.item = item_for_fight

        """
		Ajout d'une police externe grâce au module pyglet
	    """
        pyglet.font.add_file(FilePath.get("assets", "fonts", "Letters for Learners.ttf"))

        """
        Création d'un canvas qui sert de fond de page.
        Avec ajout d'une image pixelisée comme décor.
        """
        self.CAN_Zone = Canvas(self.screen, height=845, width=1536)
        img = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "PixelBG3.png")))
        CAN_BG_Image = self.CAN_Zone.create_image(0, 0, image=img, anchor="nw")

        #Créer une image pour l'animation de la destruction d'une créature
        self.imgExplosion = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "explosion.png")))
        self.imgExplosion = self.imgExplosion._PhotoImage__photo.zoom(6)

        """
        Insertion du sprite que renvoie la fonction get_sprite.
        """
        sprite_player = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", self.get_sprite())))
        sprite_player = sprite_player._PhotoImage__photo.zoom(6)
        self.CAN_SpritePlayer_Image = self.CAN_Zone.create_image(400, 400, image=sprite_player, anchor="nw")

        """
        Modifie les coordonnées de placement de sprite du monstre si c'est un boss, du à la taille.
        """
        x = 850 if self.creature.kind != "Boss" else 780
        y = 420 if self.creature.kind != "Boss" else 195
            
        """
        Insertion du sprite du monstre.
        """
        sprite_creature = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", self.creature.sprite)))
        sprite_creature = sprite_creature._PhotoImage__photo.zoom(4)
        self.CAN_SpriteCreature_Image = self.CAN_Zone.create_image(x, y, image=sprite_creature, anchor="nw")

        """
        Création et placement des différents boutons : Attaquer; Inventaire; Fuir.
        """
        attack_button = Button(self.CAN_Zone, text = "Attaque", command= self.fight, height=1, width=9, bg="#59322d", fg="white", font=("Letters for Learners", 26))
        windowAttack = self.CAN_Zone.create_window(20, 710, anchor="nw", window=attack_button)

        item_button = Button(self.CAN_Zone, text = "Items", command = self.open_inventory, height=1, width=9, bg="#59322d", fg="white", font=("Letters for Learners", 26))
        windowItem = self.CAN_Zone.create_window(190, 710, anchor="nw", window=item_button)

        leak_button = Button(self.CAN_Zone, text = "Fuite", command = self.to_escape, height=1, width=9, bg="#59322d", fg="white", font=("Letters for Learners", 26))
        windowLeak = self.CAN_Zone.create_window(360, 710, anchor="nw", window=leak_button)
        
        """
        Insertion des cadres contenant les statistiques de force ainsi que de vie du joueur et du monstre.
        """
        self.stats = self.CAN_Zone.create_rectangle(340, 260, 580, 390, width=3, fill="#b4f3fa")
        self.statsName = self.CAN_Zone.create_text(460, 285, text=f"※ {self.player.name} ※", font=("Letters for Learners", 25), fill="#6d1212")
        self.statsStrength = self.CAN_Zone.create_text(460, 325, text=f"Force : {self.player.strength} Mana", font=("Letters for Learners", 23), fill="#6d1212")
        self.statsHp = self.CAN_Zone.create_text(460, 365, text=f"Vie : {self.player.hp} Hp", font=("Letters for Learners", 23), fill="#6d1212")
        
        #Montre le cadre si c'est le boss
        yRectangleG = 260 if self.creature.kind != "Boss" else 60
        yStats = 285 if self.creature.kind != "Boss" else 85

        self.statsCreature = self.CAN_Zone.create_rectangle(855, yRectangleG, 1095, yRectangleG+130, width=3, fill="#b4f3fa")
        
        self.statsNameCreature = self.CAN_Zone.create_text(975, yStats, text=f"☬ {self.creature.kind} ☬", font=("Letters for Learners", 25), fill="#6d1212")
        self.statsStrengthCreature = self.CAN_Zone.create_text(975, yStats+40, text=f"Force : {self.creature.strength} Mana", font=("Letters for Learners", 23), fill="#6d1212")
        self.statsHpCreature = self.CAN_Zone.create_text(975, yStats+80, text=f"Vie : {self.creature.hp} Hp", font=("Letters for Learners", 23), fill="#6d1212")

        #Initialisation du canvas dans la page avec tous ses composants
        self.CAN_Zone.pack()

        #Création de la page
        self.screen.mainloop()

class NoLifeToFight:

    """
    Fonction qui renvoie à la page du Menu.
    """
    def return_to_menu(self):
        self.screen.destroy()
        menu.MenuWindow(self.player)

    """
    Fonction qui permet d'ouvrir la page d'inventaire.
    """
    def open_inventory(self):
        player = self.player
        self.screen.destroy()
        inventory_window.InventoryWindow(player, None)

    """
    Fonction qui ajoute un nombre de points de vie au joueur entre 10 et 20.
    Et retire 3 de mana, mais s'il n'y a plus de mana, baisse le score, mais augment le mana et la vie.
    """
    def GiveRandomLife(self):

        self.player.hp = random.randint(10, 20)
        self.player.strength -= 3
        if self.player.strength <= 0:
            showerror("Erreur", f"Vous avez épuisé toute votre magie {self.player.name}, votre faiblesse vous déshonore, et vous perdez alors 20 de score. Mais si nous voulons gagner cette revanche, il me faut vous aider. Je vous donnerai donc 15 Mana")
            self.player.strength = 15
            self.player.score -= 20
            save_character(name=self.player.name, strength=self.player.strength, health=self.player.hp, character_sprite=self.player.sprite, score=self.player.score, coins=self.player.coins, items=self.player.items)
        player = self.player
        self.screen.destroy()
        menu.MenuWindow(player)

    def __init__(self, player):

        """
		Paramètres de la page TKinter :
        - Titre
        - Taille
        - Couleur de fond
	    """
        self.screen = Tk()
        self.screen.geometry("1536x845")
        self.screen.title("Tu n'as plus de vie !")
        self.player = player       

        """
		Ajout d'une police externe grâce au module pyglet
	    """
        pyglet.font.add_file(FilePath.get("assets", "fonts", "Letters for Learners.ttf"))

        """
        Création d'un canvas qui sert de fond de page.
        Avec ajout d'une image pixelisée comme décor.
        """
        self.CAN_Zone = Canvas(self.screen, height=845, width=1536)
        img = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "NoLifeBG.png")))
        CAN_BG_Image = self.CAN_Zone.create_image(0, 0, image=img, anchor="nw")

        """
        Insertion d'un cadre informatif.
        """
        RectangleInfo = self.CAN_Zone.create_rectangle(725, 100, 1450, 450, width=2)
        InformationText = self.CAN_Zone.create_text(750, 120, text="Vous possèdez actuellement 0 Hp.\nOr combattre avec 0 Hp est impossible.\nDeux choix s'offrent à vous :\n➜ Utiliser une Potion de Vie\n➜ Obtenir une vie aléatoire entre 10 et 20,\n     mais en contrepartie perdre 3 Mana", anchor="nw", font=("Letters for Learners", 35))

        """
        Création et placement de bouton pour choisir entre l'inventaire, le menu et la vie aléatoire
        """
        FrameButtons = Frame(self.CAN_Zone, height=120, width=300, bg="#8601af")
        
        ButtonShop = Button(FrameButtons, text = "Inventaire", command = self.open_inventory, height=2, width=15, bg="#808080", fg="black", font=("Letters for Learners", 30))
        ButtonShop.grid(column=0, row=0, padx=40)
        
        ButtonRandomLife = Button(FrameButtons, text = "Vie Aléatoire", command = self.GiveRandomLife, height=2, width=15, bg="#808080", fg="black", font=("Letters for Learners", 30))       
        ButtonRandomLife.grid(column=1, row=0, padx=40)

        WindowButtons = self.CAN_Zone.create_window(760, 490, anchor="nw", window=FrameButtons)

        MenuButton = Button(self.CAN_Zone, text="Menu", fg="#8601af", font=("Letters for Learners", 30), command = self.return_to_menu, height=2, width=15, bg="#808080")
        window = self.CAN_Zone.create_window(965, 650, anchor="nw", window=MenuButton)

        #Initialisation du canvas dans la page avec tous ses composants
        self.CAN_Zone.pack()

        #Création de la page
        self.screen.mainloop()