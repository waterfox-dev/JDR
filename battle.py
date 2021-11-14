from tkinter import * 
from tkinter.messagebox import *
from PIL import ImageTk, Image
from fabriquecreature import FabriqueCreature
from jeu import Jeu
#from menu import MenuWindow
import random
import json
import pyglet

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb   

class BattleWindow :

    def display_item(self):
        return "Hello World"

    def get_sprite(self):
        with open("registration.json", "r") as r:
            data = json.load(r)
            for username in data :
                if username == self.player.name:
                    return data[username]["character_sprite"]

    def fight(self, CAN_Zone, statsHp, statsHpCreature):
        FightWinner = Jeu.FightCreature(self.player, self.creature)
        if FightWinner.kind == "character":
            self.creature.hp = FightWinner.hp
            if self.creature.hp <= 0:
                #Ouvrir une page Victoire
                #MenuWindow(self.player)
                pass
            else:
                CAN_Zone.itemconfigure(statsHpCreature, text=f"Vie : {self.creature.hp} Hp")
        else:
            self.player.hp = FightWinner.hp
            if self.player.hp <= 0:
                #Ouvrir une page GameOver
                #MenuWindow(self.player)
                pass
            else:
                CAN_Zone.itemconfigure(statsHp, text=f"Vie : {self.player.hp} Hp")


    def __init__(self, player, creature=FabriqueCreature.get_creature(random.choice(["Loup", "Gobelin", "Troll"]))) :
        
        self.screen = Tk() 
        self.screen.title("Combat ton adversaire !")
        self.screen.geometry("1536x845")
        self.player = player
        self.creature = creature

        pyglet.font.add_file("Letters for Learners.ttf")

        CAN_Zone = Canvas(self.screen, height=845, width=1536)
        img = ImageTk.PhotoImage(Image.open("PixelBG3.png"))
        CAN_BG_Image = CAN_Zone.create_image(0, 0, image=img, anchor="nw")

        sprite_player = ImageTk.PhotoImage(Image.open(self.get_sprite()))
        sprite_player = sprite_player._PhotoImage__photo.zoom(6)
        CAN_SpritePlayer_Image = CAN_Zone.create_image(400, 400, image=sprite_player, anchor="nw")

        sprite_creature = ImageTk.PhotoImage(Image.open(self.creature.sprite))
        sprite_creature = sprite_creature._PhotoImage__photo.zoom(4)
        CAN_SpriteCreature_Image = CAN_Zone.create_image(850, 420, image=sprite_creature, anchor="nw")

        attack_button = Button(CAN_Zone, text = "Attaque", command=lambda: self.fight(CAN_Zone, statsHp, statsHpCreature), height=1, width=9, bg="#59322d", fg="white", font=("Letters for Learners", 26))
        windowAttack = CAN_Zone.create_window(20, 710, anchor="nw", window=attack_button)

        item_button = Button(CAN_Zone, text = "Items", command = lambda : self.display_item(), height=1, width=9, bg="#59322d", fg="white", font=("Letters for Learners", 26))
        windowItem = CAN_Zone.create_window(190, 710, anchor="nw", window=item_button)

        leak_button = Button(CAN_Zone, text = "Fuite", command = lambda :print("Vous prenez la fuite"), height=1, width=9, bg="#59322d", fg="white", font=("Letters for Learners", 26))
        windowLeak = CAN_Zone.create_window(360, 710, anchor="nw", window=leak_button)
        
        stats = CAN_Zone.create_rectangle(360, 260, 555, 390, width=3, fill="#b4f3fa")
        statsName = CAN_Zone.create_text(460, 285, text=f"※ {self.player.name} ※", font=("Letters for Learners", 25), fill="#6d1212")
        statsStrength = CAN_Zone.create_text(460, 325, text=f"Force : {self.player.strength} Mana", font=("Letters for Learners", 23), fill="#6d1212")
        statsHp = CAN_Zone.create_text(460, 365, text=f"Vie : {self.player.hp} Hp", font=("Letters for Learners", 23), fill="#6d1212")
        
        statsCreature = CAN_Zone.create_rectangle(875, 260, 1070, 390, width=3, fill="#b4f3fa")
        statsNameCreature = CAN_Zone.create_text(975, 285, text=f"☬ {self.creature.kind} ☬", font=("Letters for Learners", 25), fill="#6d1212")
        statsStrengthCreature = CAN_Zone.create_text(975, 325, text=f"Force : {self.creature.strength} Mana", font=("Letters for Learners", 23), fill="#6d1212")
        statsHpCreature = CAN_Zone.create_text(975, 365, text=f"Vie : {self.creature.hp} Hp", font=("Letters for Learners", 23), fill="#6d1212")
        
        CAN_Zone.pack()

        self.screen.mainloop()

if __name__ == "__main__":  
    BattleWindow(FabriqueCreature.get_creature("character", "waterfox"))