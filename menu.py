from tkinter import * 
from tkinter.messagebox import *
from PIL import ImageTk, Image

class MenuWindow:

    def __init__(self):

        self.screen = Tk()

        """
        Faire 4 boutons :
            - [Combattre] --> Menu de Combat
            - [Magasin] --> Menu du Shop
            - [Score] --> Page de Score
            - [Quitter] --> Ferme tout et enregistre

        + décorer avec des sprites de personnages, ou d'items.    
        """

        self.screen.mainloop()