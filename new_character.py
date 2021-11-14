from tkinter import * 
from tkinter.messagebox import *
from PIL import ImageTk, Image
from fabriquecreature import FabriqueCreature
from menu import MenuWindow

class NewPerso:

    def change_page(self):
        
        self.screen.destroy()
        MenuWindow(self.player)

    def __init__(self, player):

        self.screen = Tk()
        self.screen.title("Création d'un nouveau personnage")
        self.screen.geometry("1536x845")
        self.player = player

        IMG_Image = PhotoImage(file="PixelBG.png")
        CAN_Zone = Canvas(self.screen, height=845, width=1536)
        CAN_Zone_Image = CAN_Zone.create_image(0, 0, image=IMG_Image, anchor="nw")
        
        img = ImageTk.PhotoImage(Image.open("spriteTest.png"))  
        CAN_Sprite_Image = CAN_Zone.create_image(768, 200, image=img, anchor="n")
        
        congratulation = CAN_Zone.create_text(750, 60, text="Bravo ! Tu viens de creer ton personnage.", font=("Roman", 40), fill="#6d1212")
        charaName = CAN_Zone.create_text(750, 130, text=f"Bienvenue {self.player.name}", font=("Roman", 40), fill="#6d1212")
        
        stats = CAN_Zone.create_rectangle(145, 300, 445, 446, width=2)
        statsStrength = CAN_Zone.create_text(295, 340, text=f"Force : {self.player.strength} Mana", font=("Roman", 30), fill="#6d1212")
        statsHp = CAN_Zone.create_text(295, 400, text=f"Vie : {self.player.hp} Hp", font=("Roman", 30), fill="#6d1212")

        
        ContinueButton = Button(CAN_Zone, text="Continuer", fg="white", font=("Ebrima", 15), command=self.change_page, height=1, width=10, bg="#8601af")
        window = CAN_Zone.create_window(20, 20, anchor="nw", window=ContinueButton)

        CAN_Zone.pack()

        self.screen.mainloop()

if __name__ == "__main__":
    NewPerso(FabriqueCreature.get_creature("perso", "claude"))