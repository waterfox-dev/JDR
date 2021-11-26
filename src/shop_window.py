from tkinter.font import BOLD
import pyglet

from tkinter import * 
from tkinter.messagebox import *
from PIL import ImageTk, Image

from .utils.saver import save_character
from .utils.file_path import FilePath
import src.menu as menu

class ShopWindow:

    """
    Fonction qui renvoie à la page du Menu.
    Mais sauvegarde avant, pour actualiser l'inventaire.
    """
    def return_to_menu(self):
        save_character(name=self.player.name, strength=self.player.strength, health=self.player.hp, character_sprite=self.player.sprite, score=self.player.score, coins=self.player.coins, items=self.player.items)
        player = self.player
        self.screen.destroy()
        menu.MenuWindow(player)

    """
    Fonction qui gère le payement de l'item;
    Retire l'argent ou envoie un message d'erreur.
    """
    def pay_item(self, item):
        price = 50 if item == "Portail de Téléportation" else 100 if item == "Anneau de Sorcier" else 150 if item == "Potion de Vie" else 200 if item == "Grimoire d'Or" else 250 if item == "Epée Sacrée" else 500 if item == "Invocateur de Légende" else None
        #Si le joueur a assez d'argent pour l'item choisi
        if self.player.coins >= price:
            if askyesno("Veuillez confirmer", f"Voulez vous vraiment acheter l'item suivant : {item}.\n\nCela vous coûtera {price} Coins. Solde : {self.player.coins} Coins"):
                self.player.coins -= price
                self.player.items.append(item)
                self.CAN_Zone.itemconfig(self.Balance_Text, text=f"Solde : {self.player.coins}")
        #Si le joueur ne possède pas assez d'argent
        else:
            showerror("Erreur", f"Vous ne possédez pas assez de coins. Le prix de l'item est {price} Coins\n\nSolde : {self.player.coins} Coins")

    def __init__(self, player):

        """
		Paramètres de la page TKinter :
        - Titre
        - Taille
        - Couleur de fond
	    """
        self.screen = Tk()
        self.screen.geometry("1536x845")
        self.screen.title("Magasin de WizardsRevenge")
        self.player = player

        """
		Ajout d'une police externe grâce au module pyglet
	    """
        pyglet.font.add_file(FilePath.get("assets", "fonts", "Letters for Learners.ttf"))

        #Création d'un canvas
        self.CAN_Zone = Canvas(self.screen, height=845, width=1536, bg="#a135a3")

        #Création d'un cadre
        FrameButtons = Frame(self.CAN_Zone, height=120, width=300, bg="#a135a3")

        """
		Création d'un cadre de titre pour annoncer le magasin.
	    """
        Title_Rectangle = self.CAN_Zone.create_rectangle(55, 35, 880, 170, width=5, outline="#4e5180")
        Shop_Title = self.CAN_Zone.create_text(85, 60, text="Magasin De WizardsRevenge", anchor="nw", font=("Letters for Learners", 60, BOLD), fill="#ffca18")

        """
		Création des images correspondant aux différents items disponibles à l'achat.
	    """
        Book_Image = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "book.png"))) #200 coins
        Potion_Image = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "potion.png"))) #150 coins
        Portal_Image = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "portal.png"))) #50 coins
        Sword_Image = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "sword.png"))) #250 coins
        Ring_Image = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "ring.png"))) #100 coins
        Invocator_Image = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "invocator.png"))) #500 coins

        """
        Placement des boutons qui permettent l'achat des items.
        """
        Book_Button = Button(FrameButtons, image=Book_Image, bg="#4e5180", command = lambda: self.pay_item("Grimoire d'Or"))
        Book_Button.grid(column=0, row=0, padx=30, pady=30)

        Potion_Button = Button(FrameButtons, image=Potion_Image, bg="#4e5180", command = lambda: self.pay_item("Potion de Vie"))
        Potion_Button.grid(column=1, row=0, padx=30, pady=30)

        Portal_Button = Button(FrameButtons, image=Portal_Image, bg="#4e5180", command = lambda: self.pay_item("Portail de Téléportation"))
        Portal_Button.grid(column=2, row=0, padx=30, pady=30)

        Sword_Button = Button(FrameButtons, image=Sword_Image, bg="#4e5180", command = lambda: self.pay_item("Epée Sacrée"))
        Sword_Button.grid(column=0, row=1, padx=30, pady=30)

        Ring_Button = Button(FrameButtons, image=Ring_Image, bg="#4e5180", command = lambda: self.pay_item("Anneau de Sorcier"))
        Ring_Button.grid(column=1, row=1, padx=30, pady=30)

        Invocator_Button = Button(FrameButtons, image=Invocator_Image, bg="#4e5180", command = lambda: self.pay_item("Invocateur Légendaire"))
        Invocator_Button.grid(column=2, row=1, padx=30, pady=30)

        ButtonsWindow = self.CAN_Zone.create_window(60, 180, anchor="nw", window=FrameButtons)

        #Création d'une ligne graphique pour séparer la page en deux
        Demarcation_Line = self.CAN_Zone.create_line(950, 0, 950, 832, fill="#ffca18", width=20)

        """
        Création des textes de description des items dans la partie droite de la page.
        """
        Book_Title = self.CAN_Zone.create_text(1100, 20, text="Grimoire d'Or (200 Coins)", anchor="nw", font=("Letters for Learners", 25), fill="#ffca18")
        Book_Desc = self.CAN_Zone.create_text(1060, 60, text="En lisant les quelques incantations de ce Grimoire\nd'Or, vous multiplierez par 3 les coins obtenu en\nterrassant votre ennemi.", anchor="nw", font=("Letters for Learners", 17), fill="#ffca18")

        Potion_Title = self.CAN_Zone.create_text(1100, 145, text="Potion de Vie (150 Coins)", anchor="nw", font=("Letters for Learners", 25), fill="#ffca18")
        Potion_Desc = self.CAN_Zone.create_text(1060, 185, text="Absorber cette hideuse Potion de Vie aura un effet\nmiraculeux pour régénérer un nombre de points de\nvie entre 20 et 30.", anchor="nw", font=("Letters for Learners", 15), fill="#ffca18")

        Portal_Title = self.CAN_Zone.create_text(1050, 270, text="Portail de Téléportation (50 Coins)", anchor="nw", font=("Letters for Learners", 25), fill="#ffca18")
        Portal_Desc = self.CAN_Zone.create_text(1060, 310, text="Si vous invoquez ce mystique Portail de Téléportation\naux flux mauve, vous serez sûr de pouvoir vous enfuir,\nnon pas sans déshonorer votre gloire d'invincible.", anchor="nw", font=("Letters for Learners", 15), fill="#ffca18")
        
        Sword_Title = self.CAN_Zone.create_text(1110, 395, text="Epée Sacrée (250 Coins)", anchor="nw", font=("Letters for Learners", 25), fill="#ffca18")
        Sword_Desc = self.CAN_Zone.create_text(1060, 435, text="L'Epée Sacrée saura récompenser votre gloire et votre\nbravoure. Elle vous conférera un pouvoir immense, qui\nrajoutera entre 4 et 8 de Mana.", anchor="nw", font=("Letters for Learners", 15), fill="#ffca18")
        
        Ring_Title = self.CAN_Zone.create_text(1075, 520, text="Anneau de Sorcier (100 Coins)", anchor="nw", font=("Letters for Learners", 25), fill="#ffca18")
        Ring_Desc = self.CAN_Zone.create_text(1060, 560, text="En enfilant cette Anneau de Sorcier au bout de votre\ndoigt, une déferlante de pouvoirs aussi magiqueS qu'obscurS\nprendra possesSion de vous, et vous rendra invisible.", anchor="nw", font=("Letters for Learners", 15), fill="#ffca18")
        
        Invocator_Title = self.CAN_Zone.create_text(1060, 645, text="Invocateur de Légende (500 Coins)", anchor="nw", font=("Letters for Learners", 25), fill="#ffca18")
        Invocator_Desc = self.CAN_Zone.create_text(1060, 685, text="Ce mythique artefact, un Invocateur de Légende, vous\nmettra sur la route d'un ennemi, non pas un simple monstre\nde conte de fée, mais bien une incarnation du diable.", anchor="nw", font=("Letters for Learners", 15), fill="#ffca18")
        
        Menu_Button = Button(self.CAN_Zone, text="Menu", bg="#313350", fg="white", font=("Letters for Learners", 25), width=10, height=1, command= self.return_to_menu)
        ButtonsWindow = self.CAN_Zone.create_window(385, 710, anchor="nw", window=Menu_Button)

        """
        Affiche la solde du joueur.
        """
        Balance_Rectangle = self.CAN_Zone.create_rectangle(0, 720, 230, 852, width=8, outline="#ef683c", fill="#ffca18")
        self.Balance_Text = self.CAN_Zone.create_text(20, 740, anchor="nw", text=f"Solde : {self.player.coins}", fill="#4e5180", font=("Letters for Learners", 30))

        #Initialisation du canvas dans la page avec tous ses composants
        self.CAN_Zone.pack()

        #Création de la page
        self.screen.mainloop()