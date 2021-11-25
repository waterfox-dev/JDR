# -*- coding: utf-8 -*-

from tkinter.font import BOLD
from collections import Counter
from typing import TextIO
import pyglet
import random

from tkinter import * 
from tkinter.messagebox import *
from PIL import ImageTk, Image

from .utils.saver import save_character
from .utils.file_path import FilePath
from .creatures.fabriquecreature import FabriqueCreature
import src.battle_window as battle_window

class InventoryWindow:

    def return_to_figth(self, item=None):
        if item == None:
            creature = self.creature
            player = self.player
            self.screen.destroy()
            battle_window.BattleWindow(player, creature)
        else:
            item = self.CAN_Zone.itemcget(self.Title_Choice, "text")
            self.player.items.remove(item)
            if item == "Grimoire d'Or":
                item_for_fight = "Book"
            elif item == "Potion de Vie":
                self.player.hp += random.randint(10, 20)
                item_for_fight = None
            elif item == "Portail de Téléportation":
                item_for_fight = "Portal"
            elif item == "Epée Sacrée":
                self.player.strength += random.randint(4, 8)
                item_for_fight = None
            elif item == "Anneau de Sorcier":
                item_for_fight = "Ring"
            elif item == "Invocateur de Légende":
                self.creature = FabriqueCreature.get_creature("Boss")
                item_for_fight = None
            creature = self.creature
            player = self.player
            save_character(name=self.player.name, strength=self.player.strength, health=self.player.hp, character_sprite=self.player.sprite, score=self.player.score, coins=self.player.coins, items=self.player.items)
            self.screen.destroy()
            battle_window.BattleWindow(player, creature, item_for_fight)


    def display_item_info(self, item):
        if item == "Grimoire d'Or":
            ImageZoom = self.Book_Image._PhotoImage__photo.zoom(2)
            text_item = "En lisant les quelques incantations de\nce Grimoire d'Or, vous multiplierez par 3 les\ncoins obtenu en terrassant votre ennemi."
        elif item == "Potion de Vie":
            ImageZoom = self.Potion_Image._PhotoImage__photo.zoom(2)
            text_item = "Absorber cette hideuse Potion de Vie aura\nun effet miraculeux pour régénérer un nombre\nde points de vie entre 10 et 20."
        elif item == "Portail de Téléportation":
            ImageZoom = self.Portal_Image._PhotoImage__photo.zoom(2)
            text_item = "Si vous invoquez ce mystique Portail de\nTéléportation aux flux mauve, vous serez sûr de\npouvoir vous enfuir, non pas sans déshonorer\nvotre gloire d'invincible."
        elif item == "Epée Sacrée":
            ImageZoom = self.Sword_Image._PhotoImage__photo.zoom(2)
            text_item = "L'Epée Sacrée saura récompenser votre gloire\net votre bravoure. Elle vous conférera un\npouvoir immense, qui rajoutera entre 4 et 8\nde Mana."
        elif item == "Anneau de Sorcier":
            ImageZoom = self.Ring_Image._PhotoImage__photo.zoom(2)
            text_item = "En enfilant cette Anneau de Sorcier au bout\nde votre doigt, une déferlante de pouvoir\naussi magiques qu'obscurs prendra possesSion de\nvous, et vous rendra invisible."
        elif item == "Invocateur de Légende":
            ImageZoom = self.Invocator_Image._PhotoImage__photo.zoom(2)
            text_item = "Ce mythique artefact, un Invocateur de\nLégende, vous mettra sur la route d'un ennemi,\nnon pas un simple monstre de conte de fée,\nmais bien une incarnation du diable."

        self.CAN_Zone.itemconfig(self.Text_Choice, text=text_item)
        self.CAN_Zone.itemconfig(self.Image_Choice, image=ImageZoom)
        self.CAN_Zone.image = ImageZoom
        self.CAN_Zone.itemconfig(self.Title_Choice, text=item)
        self.CAN_Zone.itemconfig(self.Info_Choice, text="En votre possesion : {}".format(self.player.items.count(item)))
        
    def __init__(self, player, creature):

        self.screen = Tk()
        self.screen.geometry("1536x845")
        self.screen.title("Ton inventaire")
        self.player = player
        self.creature = creature

        pyglet.font.add_file(FilePath.get("assets", "fonts", "Letters for Learners.ttf"))

        self.CAN_Zone = Canvas(self.screen, height=845, width=1536, bg="#a135a3")
        
        self.Book_Image = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "book.png"))) #200 coins
        self.Potion_Image = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "potion.png"))) #150 coins
        self.Portal_Image = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "portal.png"))) #50 coins
        self.Sword_Image = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "sword.png"))) #250 coins
        self.Ring_Image = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "ring.png"))) #100 coins
        self.Invocator_Image = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "invocator.png"))) #500 coins

        Frame1 = Frame(self.CAN_Zone, height=120, width=300, bg="#a135a3")
        Frame2 = Frame(self.CAN_Zone, height=120, width=300, bg="#a135a3")

        self.CAN_Zone.create_rectangle(70, 70, 280, 280, width=3)
        ButtonFirstItem = Button(Frame1, text="Utiliser : {}".format(self.player.items.count("Grimoire d'Or")), fg="white", font=("Letters for Learners", 27), height=1, width=10, bg="#8601af", command = lambda: self.display_item_info("Grimoire d'Or"))
        ButtonFirstItem.grid(column=0, row=0)
        self.CAN_Zone.create_rectangle(390, 70, 600, 280, width=3)
        ButtonSecondItem = Button(Frame1, text="Utiliser : {}".format(self.player.items.count("Potion de Vie")), fg="white", font=("Letters for Learners", 27), height=1, width=10, bg="#8601af", command = lambda: self.display_item_info("Potion de Vie"))
        ButtonSecondItem.grid(column=1, row=0, padx=160)
        self.CAN_Zone.create_rectangle(710, 70, 920, 280, width=3)
        ButtonThirdItem = Button(Frame1, text="Utiliser : {}".format(self.player.items.count("Portail de Téléportation")), fg="white", font=("Letters for Learners", 27), height=1, width=10, bg="#8601af", command = lambda: self.display_item_info("Portail de Téléportation"))
        ButtonThirdItem.grid(column=2, row=0)
        self.CAN_Zone.create_rectangle(70, 430, 280, 640, width=3)
        ButtonFourthItem = Button(Frame2, text="Utiliser : {}".format(self.player.items.count("Epée Sacrée")), fg="white", font=("Letters for Learners", 27), height=1, width=10, bg="#8601af", command = lambda: self.display_item_info("Epée Sacrée"))
        ButtonFourthItem.grid(column=0, row=0)
        self.CAN_Zone.create_rectangle(390, 430, 600, 640, width=3)
        ButtonFifthItem = Button(Frame2, text="Utiliser : {}".format(self.player.items.count("Anneau de Sorcier")), fg="white", font=("Letters for Learners", 27), height=1, width=10, bg="#8601af", command = lambda: self.display_item_info("Anneau de Sorcier"))
        ButtonFifthItem.grid(column=1, row=0, padx=160)
        self.CAN_Zone.create_rectangle(710, 430, 920, 640, width=3)
        ButtonSixthItem = Button(Frame2, text="Utiliser : {}".format(self.player.items.count("Invocateur de Légende")), fg="white", font=("Letters for Learners", 27), height=1, width=10, bg="#8601af", command = lambda: self.display_item_info("Invocateur de Légende"))
        ButtonSixthItem.grid(column=2, row=0)

        FirstButtonsWindow = self.CAN_Zone.create_window(95, 310, anchor="nw", window=Frame1)
        SecondButtonsWindow = self.CAN_Zone.create_window(95, 670, anchor="nw", window=Frame2)

        Different_Items = Counter(self.player.items).keys()
        for item in Different_Items:
            x = 815 if item == "Portail de Téléportation" else 495 if item == "Anneau de Sorcier" else 495 if item == "Potion de Vie" else 175 if item == "Grimoire d'Or" else 175 if item == "Epée Sacrée" else 815 if item == "Invocateur de Légende" else None
            y = 175 if item == "Portail de Téléportation" else 535 if item == "Anneau de Sorcier" else 175 if item == "Potion de Vie" else 175 if item == "Grimoire d'Or" else 535 if item == "Epée Sacrée" else 535 if item == "Invocateur de Légende" else None
            img = self.Portal_Image if item == "Portail de Téléportation" else self.Ring_Image if item == "Anneau de Sorcier" else self.Potion_Image if item == "Potion de Vie" else self.Book_Image if item == "Grimoire d'Or" else self.Sword_Image if item == "Epée Sacrée" else self.Invocator_Image if item == "Invocateur de Légende" else None
            print(x, y, img)
            self.CAN_Zone.create_image(x, y, image=img)

        Demarcation_Line = self.CAN_Zone.create_line(1000, 0, 1000, 832, fill="#ffca18", width=20)
        
        FrameButtonsChoice = Frame(self.CAN_Zone, height=120, width=300, bg="#a135a3")

        ButtonValidation = Button(FrameButtonsChoice, text="Continuer", fg="white", font=("Letters for Learners", 30), height=1, width=13, bg="#8601af", command = lambda: self.return_to_figth("Buy"))
        ButtonValidation.grid(column=0, row=0, padx=10)
        ButtonExit = Button(FrameButtonsChoice, text="Annuler", fg="white", font=("Letters for Learners", 30), height=1, width=13, bg="#8601af", command = self.return_to_figth)
        ButtonExit.grid(column=1, row=0, padx=10)

        ChoiceButtonsWindow = self.CAN_Zone.create_window(1035, 700, anchor="nw", window=FrameButtonsChoice)

        self.Text_Choice = self.CAN_Zone.create_text(1275, 530, anchor="center", text="", font=("Letters for Learners", 23))
        self.Image_Choice = self.CAN_Zone.create_image(1270, 195, image="")
        self.Title_Choice = self.CAN_Zone.create_text(1270, 415, anchor="center", text="", font=("Letters for Learners", 40, UNDERLINE))
        self.Info_Choice = self.CAN_Zone.create_text(1270, 640, anchor="center", text="", font=("Letters for Learners", 25))

        self.CAN_Zone.pack()

        self.screen.mainloop()

if __name__ == "__main__":
    InventoryWindow()