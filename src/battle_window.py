import random
import json
import pyglet

from tkinter import * 
from tkinter.messagebox import *
from PIL import ImageTk, Image

from .utils.jeu import Jeu
from .utils.file_path import FilePath
import src.go_or_win as go_or_win
import src.menu as menu

class BattleWindow:

    def display_item(self):
        return "Hello World"

    def get_sprite(self):
        with open(FilePath.get("data", "registration.json"), "r") as r:
            data = json.load(r)
            for username in data :
                if username == self.player.name:
                    return data[username]["character_sprite"]

    def fight(self, CAN_Zone, statsHp, statsHpCreature):
        FightLoser = Jeu.FightCreature(self.player, self.creature)
        if FightLoser.kind == "character":
            self.player.hp = FightLoser.hp
            if self.player.hp <= 0:
                self.player.hp = 0
                player = self.player
                self.screen.destroy()
                go_or_win.GameOverWindow(player, self.creature.kind)
            else:
                CAN_Zone.itemconfigure(statsHp, text=f"Vie : {self.player.hp} Hp")
        else:
            self.creature.hp = FightLoser.hp
            if self.creature.hp <= 0:
                player = self.player
                self.screen.destroy()
                go_or_win.WinWindow(player, self.creature.kind)
            else:
                CAN_Zone.itemconfigure(statsHpCreature, text=f"Vie : {self.creature.hp} Hp")


    def __init__(self, player, creature) :
        
        self.screen = Tk() 
        self.screen.title("Combat ton adversaire !")
        self.screen.geometry("1536x845")
        self.player = player
        self.creature = creature

        pyglet.font.add_file(FilePath.get("assets", "fonts", "Letters for Learners.ttf"))

        CAN_Zone = Canvas(self.screen, height=845, width=1536)
        img = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "PixelBG3.png")))
        CAN_BG_Image = CAN_Zone.create_image(0, 0, image=img, anchor="nw")

        sprite_player = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", self.get_sprite())))
        sprite_player = sprite_player._PhotoImage__photo.zoom(6)
        CAN_SpritePlayer_Image = CAN_Zone.create_image(400, 400, image=sprite_player, anchor="nw")

        sprite_creature = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", self.creature.sprite)))
        sprite_creature = sprite_creature._PhotoImage__photo.zoom(4)
        CAN_SpriteCreature_Image = CAN_Zone.create_image(850, 420, image=sprite_creature, anchor="nw")

        attack_button = Button(CAN_Zone, text = "Attaque", command=lambda: self.fight(CAN_Zone, statsHp, statsHpCreature), height=1, width=9, bg="#59322d", fg="white", font=("Letters for Learners", 26))
        windowAttack = CAN_Zone.create_window(20, 710, anchor="nw", window=attack_button)

        item_button = Button(CAN_Zone, text = "Items", command = lambda : self.display_item(), height=1, width=9, bg="#59322d", fg="white", font=("Letters for Learners", 26))
        windowItem = CAN_Zone.create_window(190, 710, anchor="nw", window=item_button)

        leak_button = Button(CAN_Zone, text = "Fuite", command = lambda :print("Vous prenez la fuite"), height=1, width=9, bg="#59322d", fg="white", font=("Letters for Learners", 26))
        windowLeak = CAN_Zone.create_window(360, 710, anchor="nw", window=leak_button)
        
        stats = CAN_Zone.create_rectangle(340, 260, 580, 390, width=3, fill="#b4f3fa")
        statsName = CAN_Zone.create_text(460, 285, text=f"※ {self.player.name} ※", font=("Letters for Learners", 25), fill="#6d1212")
        statsStrength = CAN_Zone.create_text(460, 325, text=f"Force : {self.player.strength} Mana", font=("Letters for Learners", 23), fill="#6d1212")
        statsHp = CAN_Zone.create_text(460, 365, text=f"Vie : {self.player.hp} Hp", font=("Letters for Learners", 23), fill="#6d1212")
        
        statsCreature = CAN_Zone.create_rectangle(855, 260, 1095, 390, width=3, fill="#b4f3fa")
        statsNameCreature = CAN_Zone.create_text(975, 285, text=f"☬ {self.creature.kind} ☬", font=("Letters for Learners", 25), fill="#6d1212")
        statsStrengthCreature = CAN_Zone.create_text(975, 325, text=f"Force : {self.creature.strength} Mana", font=("Letters for Learners", 23), fill="#6d1212")
        statsHpCreature = CAN_Zone.create_text(975, 365, text=f"Vie : {self.creature.hp} Hp", font=("Letters for Learners", 23), fill="#6d1212")
        
        CAN_Zone.pack()

        self.screen.mainloop()

class NoLifeToFight:

    def GiveRandomLife(self):

        self.player.hp = random.randint(10, 20)
        self.player.strength -= 3
        player = self.player
        self.screen.destroy()
        menu.MenuWindow(player)

    def __init__(self, player):

        self.screen = Tk()
        self.screen.geometry("1536x845")
        self.player = player       

        pyglet.font.add_file(FilePath.get("assets", "fonts", "Letters for Learners.ttf"))

        CAN_Zone = Canvas(self.screen, height=845, width=1536)
        img = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "NoLifeBG.png")))
        CAN_BG_Image = CAN_Zone.create_image(0, 0, image=img, anchor="nw")

        RectangleInfo = CAN_Zone.create_rectangle(725, 100, 1450, 450, width=2)
        InformationText = CAN_Zone.create_text(750, 120, text="Vous possèdez actuellement 0 Hp.\nOr combattre avec 0 Hp est impossible.\nDeux choix s'offrent à vous :\n➜ Acheter un régénérateur\n➜ Obtenir une vie aléatoire entre 10 et 20,\n     mais en contrepartie perdre 3 Mana", anchor="nw", font=("Letters for Learners", 35))

        FrameButtons = Frame(CAN_Zone, height=120, width=300, bg="#8601af")
        
        ButtonShop = Button(FrameButtons, text = "Magasin", command = lambda :print("Magasin"), height=2, width=15, bg="#808080", fg="black", font=("Letters for Learners", 30))
        ButtonShop.grid(column=0, row=0, padx=40)
        
        ButtonRandomLife = Button(FrameButtons, text = "Vie Aléatoire", command = lambda: self.GiveRandomLife(), height=2, width=15, bg="#808080", fg="black", font=("Letters for Learners", 30))       
        ButtonRandomLife.grid(column=1, row=0, padx=40)

        WindowButtons = CAN_Zone.create_window(760, 530, anchor="nw", window=FrameButtons)

        CAN_Zone.pack()

        self.screen.mainloop()