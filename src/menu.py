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

    def QuitGame(self):
        save_character(name=self.player.name, strength=self.player.strength, health=self.player.hp, character_sprite=self.player.sprite, score=self.player.score, coins=self.player.coins, items=self.player.items)
        self.screen.destroy()

    def GoToFight(self):
        player = self.player
        self.screen.destroy()
        if player.hp > 0:
            creature = FabriqueCreature.get_creature(random.choice(["Loup", "Gobelin", "Troll"]))
            battle_window.BattleWindow(player, creature)
        else:
            battle_window.NoLifeToFight(player)

    def GoToShop(self):
        player = self.player
        self.screen.destroy()
        shop_window.ShopWindow(player)

    def GoToScore(self):
        player = self.player
        self.screen.destroy()
        ScoreWindow(player)

    def __init__(self, player):

        self.screen = Tk()
        self.screen.title("Menu de WizardsRevenge")
        #self.screen.iconbitmap(FilePath.get("assets", "icon", "grimoire.ico"))
        self.screen.geometry("1536x845")
        self.player = player
        
        pyglet.font.add_file(FilePath.get("assets", "fonts", "Letters for Learners.ttf"))

        CAN_Zone = Canvas(self.screen, height=845, width=1536)
        img = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "PixelBG2.png")))
        CAN_Sprite_Image = CAN_Zone.create_image(0, 0, image=img, anchor="nw")
        
        Frame1 = Frame(CAN_Zone, height=120, width=300, bg="#333399")
        
        ButtonFight = Button(Frame1, text="Combattre !", font=("Letters for Learners", 20), height=2, width=15, bg="#4e5180", fg="white", command=self.GoToFight)
        ButtonFight.grid(column=0, row=0, padx=30, pady=50)
        
        ButtonShop = Button(Frame1, text="Magasin", font=("Letters for Learners", 20), height=2, width=15, bg="#4e5180", fg="white", command=self.GoToShop)
        ButtonShop.grid(column=1, row=1, padx=30, pady=50)
        
        ButtonScore = Button(Frame1, text="Score", font=("Letters for Learners", 20), height=2, width=15, bg="#4e5180", fg="white", command=self.GoToScore)
        ButtonScore.grid(column=2, row=0, padx=30, pady=50)
        
        ButtonQuit = Button(CAN_Zone, text="Quitter", font=("Letters for Learners", 20), height=2, width=15, bg="#313350", fg="white", command=self.QuitGame)

        ButtonWindowQuit = CAN_Zone.create_window(1450, 90, anchor="ne", window=ButtonQuit)
        ButtonsWindow = CAN_Zone.create_window(130, 280, anchor="nw", window=Frame1)

        MessageRectangle = CAN_Zone.create_rectangle(120, 70, 1035, 190, width=8, fill="#7d4e80", outline="#313350")
        MessageText = CAN_Zone.create_text(580, 130, text=f"Menu de WizardsRevenge", font=("Letters for Learners", 75, "bold"), fill="white")

        CAN_Zone.pack()


        self.screen.mainloop()