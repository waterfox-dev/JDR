import pyglet
import random
import json

from .utils.file_path import FilePath
from tkinter import * 
from tkinter.messagebox import *
from PIL import ImageTk, Image
import src.menu as menu


class ScoreWindow:

    """
    Fonction qui renvoie à la page du Menu.
    """
    def return_to_menu(self):
        player = self.player
        self.screen.destroy()
        menu.MenuWindow(player)

    """
    Fonction qui récupère et renvoie la score attribué à l'utilisateur.
    """
    def get_player_score(self):
        with open(FilePath.get("data", "registration.json"), "r") as r:
            data = json.load(r)
            for username in data :
                if username == self.player.name:
                    return data[username]["characteristic"]["score"]

    """
    Fonction qui renvoie une liste, contenant des tuples, qui eux mêmes contiennent un nom d'utilisateur et un score.
    Ces tuples sont les meilleurs joueurs, en terme de score;
    3 par défaut, et moins s'il y a moins de joueurs d'enregistrer sur le jeu.
    """
    def get_best_scores(self):
        scores, usernames, best_scores = [], [], []
        
        with open(FilePath.get("data", "registration.json"), "r") as r:
            data = json.load(r)
            for username in data :
                scores.append(data[username]["characteristic"]["score"])
                usernames.append(username)

            nb = 3 if len(usernames) >= 3 else len(usernames)
            for _ in range(nb):
                best_scores.append((usernames.pop(scores.index(max(scores))), scores.pop(scores.index(max(scores)))))
        
        return best_scores

    """
    Fonction qui récupère et renvoie la classement du joueur en terme de score.
    """
    def get_player_position(self):
        scores = []
        with open(FilePath.get("data", "registration.json"), "r") as r:
            data = json.load(r)
            
            for username in data :
                scores.append(data[username]["characteristic"]["score"])
            scores.sort(reverse=True)

            for score in scores:
                if score == self.player.score:
                    return scores.index(score) + 1

    def __init__(self, player):
        
        """
		Paramètres de la page TKinter :
        - Titre
        - Taille
        - Couleur de fond
	    """
        self.screen = Tk()
        self.screen.geometry("1536x800")
        self.screen.resizable(width=False, height=False)
        self.screen.title("Scores")
        self.player = player
        
        """
		Ajout d'une police externe grâce au module pyglet
	    """
        pyglet.font.add_file(FilePath.get("assets", "fonts", "Letters for Learners.ttf"))

        #Création du canvas
        CAN_Zone = Canvas(self.screen, height=845, width=1536, bg="#463f61")
    
        #Insertion d'un titre
        CAN_Title_Frame = CAN_Zone.create_rectangle(175, 40, 850, 160, width=2, fill="#8d70fd")
        CAN_Title = CAN_Zone.create_text(230, 50, text="Meilleurs Joueurs :", font=("Letters for Learners", 70), anchor="nw")

        """
        Création des images des trois médailles correspondant aux meilleurs joueurs.
        """
        IMG_GoldenMedal = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "golden_medal.png")))
        IMG_SilverMedal = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "silver_medal.png")))
        IMG_BronzeMedal = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "bronze_medal.png")))

        """Placement des images de médailles.
        """
        CAN_GoldMedal_Image = CAN_Zone.create_image(90, 200, image=IMG_GoldenMedal, anchor="nw")
        CAN_SilverMedal_Image = CAN_Zone.create_image(90, 400, image=IMG_SilverMedal, anchor="nw")
        CAN_BronzeMedal_Image = CAN_Zone.create_image(90, 600, image=IMG_BronzeMedal, anchor="nw")

        Best_Players = self.get_best_scores()

        #Si le nombre de joueurs enregistrés est supérieur ou égal à 3
        if len(Best_Players) >= 3:
            CAN_First_Player = CAN_Zone.create_text(250, 240, text=f"{Best_Players[0][0]} avec {str(Best_Players[0][1])} points", font=("Letters for Learners", 50), anchor="nw", fill="#fdc911")
            CAN_Second_Player = CAN_Zone.create_text(250, 440, text=f"{Best_Players[1][0]} avec {str(Best_Players[1][1])} points", font=("Letters for Learners", 50), anchor="nw", fill="#b2b2b2")
            CAN_Third_Player = CAN_Zone.create_text(250, 640, text=f"{Best_Players[2][0]} avec {str(Best_Players[2][1])} points", font=("Letters for Learners", 50), anchor="nw", fill="#ea8a24")
            #Vérifie s'il y a des égalites, et adapte les couleurs et les médailles
            if Best_Players[1][1] == Best_Players[0][1]:
                CAN_Zone.itemconfigure(CAN_SilverMedal_Image, image=IMG_GoldenMedal)
                CAN_Zone.itemconfigure(CAN_Second_Player, fill="#fdc911")
            if Best_Players[2][1] == Best_Players[0][1]:
                CAN_Zone.itemconfigure(CAN_BronzeMedal_Image, image=IMG_GoldenMedal)
                CAN_Zone.itemconfigure(CAN_Third_Player, fill="#fdc911")
            elif Best_Players[2][1] == Best_Players[1][1]:
                CAN_Zone.itemconfigure(CAN_BronzeMedal_Image, image=IMG_SilverMedal)
                CAN_Zone.itemconfigure(CAN_Third_Player, fill="#b2b2b2")
        #Si le nombre de joueurs enregistrés est égal à 2
        elif len(Best_Players) == 2:
            CAN_First_Player = CAN_Zone.create_text(250, 240, text=f"{Best_Players[0][0]} avec {str(Best_Players[0][1])} points", font=("Letters for Learners", 50), anchor="nw", fill="#fdc911")
            CAN_Second_Player = CAN_Zone.create_text(250, 440, text=f"{Best_Players[1][0]} avec {str(Best_Players[1][1])} points", font=("Letters for Learners", 50), anchor="nw", fill="#b2b2b2")
            #Vérifie s'il y a des égalites, et adapte les couleurs et les médailles
            if Best_Players[0][1] == Best_Players[1][1]:
                CAN_Zone.itemconfigure(CAN_SilverMedal_Image, image=IMG_GoldenMedal)
                CAN_Zone.itemconfigure(CAN_Second_Player, fill="#fdc911")
            CAN_Zone.delete(CAN_BronzeMedal_Image)
        #Si le nombre de joueurs enregistrés est égal à 1
        elif len(Best_Players) == 1:
            CAN_First_Player = CAN_Zone.create_text(250, 240, text=f"{Best_Players[0][0]} avec {str(Best_Players[0][1])} points", font=("Letters for Learners", 50), anchor="nw", fill="#fdc911")
            CAN_Zone.delete(CAN_BronzeMedal_Image, CAN_SilverMedal_Image)
            
        #Différents textes et stats
        CAN_Player_Position_Frame = CAN_Zone.create_rectangle(950, 150, 1450, 600, width=2, fill="#8d70fd")
        CAN_Player_Position_Title = CAN_Zone.create_text(985, 170, text="Votre classement :", font=("Letters for Learners", 55, UNDERLINE), anchor="nw", fill="#9a1f26")
        CAN_Player_Position_Number = CAN_Zone.create_text(1200, 375, text=self.get_player_position(), font=("Letters for Learners", 180), anchor="center", fill="#9a1f26")
        CAN_Player_Position_Text = CAN_Zone.create_text(1200, 525, text=f"avec {self.get_player_score()} points", anchor="center", font=("Letters for Learners", 45), fill="#9a1f26")

        #Création d'un bouton pour retourner au menu
        ButtonQuit = Button(CAN_Zone, text="Menu", font=("Letters for Learners", 20), height=2, width=15, bg="#8d70fd", fg="white", command=self.return_to_menu)
        ButtonWindowQuit = CAN_Zone.create_window(1490, 680, anchor="ne", window=ButtonQuit)

        #Initialisation du canvas dans la page avec tous ses composants
        CAN_Zone.pack()
        
        #Création de la page
        self.screen.mainloop()