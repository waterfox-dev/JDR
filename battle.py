from PIL import ImageTk
from tkinter import *
from fabriquecreature import FabriqueCreature
import PIL.Image
import random

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb   

class BattleWindow :

    def display_item(self):
        return "Hello World"

    def __init__(self, player, creature=FabriqueCreature.get_creature(random.choice(["Loup", "Gobelin", "Troll"]))) :
        
        self.screen = Tk() 
        self.screen.title("Combat ton adversaire !")
        self.screen.geometry("1536x845")

        opponent_label = Label(self.screen, text = f"{creature.kind}\nVie : {creature.hp} Hp\nForce : {creature.strength} Mana")
        opponent_label.config(borderwidth=3, relief="ridge")
        opponent_label.grid(column=3, row=0)

        opponent_canvas = Canvas(self.screen, width=64, height=64)
        opponent_canvas.grid(column=3, row=1)
        
        opponent_pic = ImageTk.PhotoImage(PIL.Image.open("artwork.png"))  
        opponent_canvas.create_image(0,0, anchor = NW, image = opponent_pic)

        player_label = Label(self.screen, text = f"{player.name}\nVie : {player.hp} Hp\nForce : {player.strength} Mana")
        player_label.config(borderwidth=3, relief="ridge")
        player_label.grid(column=2, row=0)

        
        player_canvas = Canvas(self.screen, width=64, height=64)
        player_canvas.grid(column=2, row = 1)

        player_pic = ImageTk.PhotoImage(PIL.Image.open("artwork.png"))  
        player_canvas.create_image(0,0, anchor = NW, image = player_pic)

        self.command_label = Label(self.screen, borderwidth=3, relief="ridge")
        self.command_label.grid(column=2, row = 2)

        attack_button = Button(self.command_label, text = "Attaque", command=lambda:print("hello world"))
        attack_button.grid(column = 1, row = 0)

        item_button = Button(self.command_label, text = "Items", command = lambda : self.display_item())
        item_button.grid(column = 2, row= 0)

        leak_button = Button(self.command_label, text = "FUITE !", command = lambda :print("Vous prenez la fuite"))
        leak_button.grid(column = 3, row= 0)


        self.screen.mainloop()

if __name__ == "__main__":  
    BattleWindow(FabriqueCreature.get_creature("character", "Waterfox"))