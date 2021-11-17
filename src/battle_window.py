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

class BattleWindow:

    def to_escape(self):
        chance = [True, False, False]
        if random.choice(chance):
            player = self.player
            save_character(name=self.player.name, strength=self.player.strength, health=self.player.hp, character_sprite=self.player.sprite, score=self.player.score, coins=self.player.coins, items=self.player.items)
            self.screen.destroy()
            menu.MenuWindow(player)
        else:
            lost_hp = random.randint(1,3)
            self.display_fail_escape(True, lost_hp)
            self.player.hp -= lost_hp
            self.CAN_Zone.itemconfigure(self.statsHp, text=f"Vie : {self.player.hp} Hp")

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

    def display_item(self):
        return "Hello World"

    def get_sprite(self):
        with open(FilePath.get("data", "registration.json"), "r") as r:
            data = json.load(r)
            for username in data :
                if username == self.player.name:
                    return data[username]["character_sprite"]

    def fight(self):
        self.display_fail_escape(False)
        FightLoser = Jeu.FightCreature(self.player, self.creature)
        if FightLoser.kind == "character":
            self.player.hp = FightLoser.hp
            if self.player.hp <= 0:
                self.player.hp = 0
                player = self.player
                self.screen.destroy()
                go_or_win.GameOverWindow(player, self.creature.kind)
            else:
                self.CAN_Zone.itemconfigure(self.statsHp, text=f"Vie : {self.player.hp} Hp")
        else:
            self.creature.hp = FightLoser.hp
            if self.creature.hp <= 0:
                player = self.player
                self.CAN_Zone.itemconfigure(self.CAN_SpriteCreature_Image, image=self.imgExplosion)
                self.CAN_Zone.delete(self.statsCreature, self.statsNameCreature, self.statsStrengthCreature, self.statsHpCreature)
                #time.sleep(4)
                self.screen.destroy()
                go_or_win.WinWindow(player, self.creature.kind)
            else:
                self.CAN_Zone.itemconfigure(self.statsHpCreature, text=f"Vie : {self.creature.hp} Hp")


    def __init__(self, player, creature) :
        
        self.screen = Tk() 
        self.screen.title("Combat ton adversaire !")
        self.screen.geometry("1536x845")
        self.player = player
        self.creature = creature

        pyglet.font.add_file(FilePath.get("assets", "fonts", "Letters for Learners.ttf"))

        self.CAN_Zone = Canvas(self.screen, height=845, width=1536)
        img = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "PixelBG3.png")))
        CAN_BG_Image = self.CAN_Zone.create_image(0, 0, image=img, anchor="nw")

        self.imgExplosion = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "explosion.png")))
        self.imgExplosion = self.imgExplosion._PhotoImage__photo.zoom(6)

        sprite_player = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", self.get_sprite())))
        sprite_player = sprite_player._PhotoImage__photo.zoom(6)
        self.CAN_SpritePlayer_Image = self.CAN_Zone.create_image(400, 400, image=sprite_player, anchor="nw")

        sprite_creature = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", self.creature.sprite)))
        sprite_creature = sprite_creature._PhotoImage__photo.zoom(4)
        self.CAN_SpriteCreature_Image = self.CAN_Zone.create_image(850, 420, image=sprite_creature, anchor="nw")

        attack_button = Button(self.CAN_Zone, text = "Attaque", command= self.fight, height=1, width=9, bg="#59322d", fg="white", font=("Letters for Learners", 26))
        windowAttack = self.CAN_Zone.create_window(20, 710, anchor="nw", window=attack_button)

        item_button = Button(self.CAN_Zone, text = "Items", command = self.display_item, height=1, width=9, bg="#59322d", fg="white", font=("Letters for Learners", 26))
        windowItem = self.CAN_Zone.create_window(190, 710, anchor="nw", window=item_button)

        leak_button = Button(self.CAN_Zone, text = "Fuite", command = self.to_escape, height=1, width=9, bg="#59322d", fg="white", font=("Letters for Learners", 26))
        windowLeak = self.CAN_Zone.create_window(360, 710, anchor="nw", window=leak_button)
        
        self.stats = self.CAN_Zone.create_rectangle(340, 260, 580, 390, width=3, fill="#b4f3fa")
        self.statsName = self.CAN_Zone.create_text(460, 285, text=f"※ {self.player.name} ※", font=("Letters for Learners", 25), fill="#6d1212")
        self.statsStrength = self.CAN_Zone.create_text(460, 325, text=f"Force : {self.player.strength} Mana", font=("Letters for Learners", 23), fill="#6d1212")
        self.statsHp = self.CAN_Zone.create_text(460, 365, text=f"Vie : {self.player.hp} Hp", font=("Letters for Learners", 23), fill="#6d1212")
        
        self.statsCreature = self.CAN_Zone.create_rectangle(855, 260, 1095, 390, width=3, fill="#b4f3fa")
        self.statsNameCreature = self.CAN_Zone.create_text(975, 285, text=f"☬ {self.creature.kind} ☬", font=("Letters for Learners", 25), fill="#6d1212")
        self.statsStrengthCreature = self.CAN_Zone.create_text(975, 325, text=f"Force : {self.creature.strength} Mana", font=("Letters for Learners", 23), fill="#6d1212")
        self.statsHpCreature = self.CAN_Zone.create_text(975, 365, text=f"Vie : {self.creature.hp} Hp", font=("Letters for Learners", 23), fill="#6d1212")
        
        self.CAN_Zone.pack()

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
        self.screen.title("Tu n'as plus de vie !")
        self.player = player       

        pyglet.font.add_file(FilePath.get("assets", "fonts", "Letters for Learners.ttf"))

        self.CAN_Zone = Canvas(self.screen, height=845, width=1536)
        img = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "NoLifeBG.png")))
        CAN_BG_Image = self.CAN_Zone.create_image(0, 0, image=img, anchor="nw")

        RectangleInfo = self.CAN_Zone.create_rectangle(725, 100, 1450, 450, width=2)
        InformationText = self.CAN_Zone.create_text(750, 120, text="Vous possèdez actuellement 0 Hp.\nOr combattre avec 0 Hp est impossible.\nDeux choix s'offrent à vous :\n➜ Acheter un régénérateur\n➜ Obtenir une vie aléatoire entre 10 et 20,\n     mais en contrepartie perdre 3 Mana", anchor="nw", font=("Letters for Learners", 35))

        FrameButtons = Frame(self.CAN_Zone, height=120, width=300, bg="#8601af")
        
        ButtonShop = Button(FrameButtons, text = "Magasin", command = lambda :print("Magasin"), height=2, width=15, bg="#808080", fg="black", font=("Letters for Learners", 30))
        ButtonShop.grid(column=0, row=0, padx=40)
        
        ButtonRandomLife = Button(FrameButtons, text = "Vie Aléatoire", command = self.GiveRandomLife, height=2, width=15, bg="#808080", fg="black", font=("Letters for Learners", 30))       
        ButtonRandomLife.grid(column=1, row=0, padx=40)

        WindowButtons = self.CAN_Zone.create_window(760, 530, anchor="nw", window=FrameButtons)

        self.CAN_Zone.pack()

        self.screen.mainloop()