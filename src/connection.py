import random
import json
import pyglet

from tkinter import * 
from tkinter.messagebox import *
from PIL import ImageTk, Image

from .utils.saver import create_new_character
from .utils.file_path import FilePath
from .creatures.creature import Creature
from .creatures.fabriquecreature import FabriqueCreature
from .menu import MenuWindow
from .new_character import NewPerso

class Connection:

    def __init__(self, player, password):
        self.username = player.name
        self.password = password
        self.player = player
    
    """
    Fonction qui vérifie si l'utilisateur existe déjà dans le base de données et renvoie si oui ou non.
    """
    def already_registered_or_not(self):
        with open(FilePath.get("data", "registration.json"), "r") as r:
            data = json.load(r)
            for username in data :
                if username == self.username :
                    return True 
            else :
                False

    """
    Fonction qui vérifie quand le bouton Connexion est cliqué, si un couple Nom d'utilisateur/Mot de passe existe dans la base de données, et renvoie si oui ou non.
    """
    def login(self):
        with open(FilePath.get("data", "registration.json"), "r") as r:
            data = json.load(r)
            for _ in data :
                try:
                    if data[self.username]["password"] == self.password:
                        return True
                except:
                    return False

    """
    Fonction qui retourne l'objet player qui correspond au nom d'utilisateur.
    """
    def get_player_object(self):
        with open(FilePath.get("data", "registration.json"), "r") as r:
            data = json.load(r)
            for username in data :
                if username == self.username:
                    player = Creature("character", data[username]["characteristic"]["strength"], data[username]["characteristic"]["health"], data[username]["character_sprite"], username, data[username]["characteristic"]["score"], data[username]["characteristic"]["coins"], data[username]["items"])
                    return player

    """
    Enregistre un nouveau profil dans la base de données quand une inscription a lieu.
    """
    def register(self):
        create_new_character(
            name=self.username,
            strength=self.player.strength,
            health=self.player.hp,
            character_sprite=self.player.sprite,
            password=self.password,
            score = 0,
            coins=0)

class ConnectionPage:

    """
    Fonction qui permet de vérifier mot de passe et nom d'utilisateur en cas de connexion ou d'inscription.
    Vérifie si l'utilisateur n'existe pas déjà s'il y a demande d'inscription;
    Vérifie si couple : mot de passe/nom d'utilisateur existe si connexion.
    """
    def verify(self, id_button):
        #Si nombre de caractères obligatoires non respectés
        if len(self.entreeUser.get()) > 13 or len(self.entreeUser.get()) < 3:
            showerror("Erreur", "Veuillez choisir un nom d'utilisateur entre 3 et 13 caractères.")
        #Si l'utilisateur a inscrit quelque chose dans les entrées de textes
        elif self.entreeUser.get() != "" and self.entreePassword.get() != "":
            player = FabriqueCreature.get_creature("character", self.entreeUser.get())
            connection = Connection(player, self.entreePassword.get())
            #Si demande de connexion
            if id_button == 1:
                if connection.login():
                    print("Connecté")
                    self.screen.destroy()
                    MenuWindow(connection.get_player_object())
                else:
                    showerror("Erreur", "Votre nom d'utilisateur ou votre mot de passe est incorrect.")
            #Si demande d'inscription
            elif id_button == 2:
                if not connection.already_registered_or_not():
                    connection.register()
                    print("Enregistré")
                    self.screen.destroy()
                    NewPerso(player)
                else:
                    showinfo("Erreur", "Ce nom d'utilisateur est déjà pris.")
        #Si l'utilisateur demande à se connecter ou à s'inscrire sans remplir les entrées
        else:
            showerror("Erreur", "Veuillez remplir votre nom d'utilisateur et votre mot de passe.")

    def __init__(self):
        
        """
		Paramètres de la page TKinter :
        - Titre
        - Icône
        - Taille
        - Couleur de fond
	    """
        self.screen = Tk() 
        self.screen.title("WizardsRevenge")
        #self.screen.iconbitmap(FilePath.get("assets", "icon", "grimoire.ico"))
        self.screen.geometry("1536x845")
        self.screen.config(background="#282c34")

        """
		Ajout d'une police externe grâce au module pyglet
	    """
        pyglet.font.add_file(FilePath.get("assets", "fonts", "Letters for Learners.ttf"))

        """
		Création des différents frame de page (cadre pour placer des éléments)
	    """
        #Frame Titre du Jeu
        Frame1 = Frame(self.screen, height=80, width=300, borderwidth=10, bg="black")
        Frame1.grid(column=1, row=0, pady=50)
        #Frame Sprite gauche
        Frame2 = Frame(self.screen, height=500, width=300, borderwidth=1, bg="#282c34")
        Frame2.grid(column=0, row=1, padx=80)
        #Frame Menu de connexion
        Frame3 = Frame(self.screen, height=80, width=300, borderwidth=10, bg="#fafaee")
        Frame3.grid(column=1, row=1)
        #Frame Sprite droit
        Frame4 = Frame(self.screen, height=500, width=300, borderwidth=1, bg="#282c34")
        Frame4.grid(column=2, row=1, padx=100)

        #Titre du Jeu
        labelTitle = Label(Frame1, text="WizardsRevenge", fg="white", bg="#7f5fdd", font=("Letters for Learners", 80, "bold"))
        labelTitle.grid(column=0, row=0)

        """
		Création des images à initialiser sur la page. Sprites des deux personnages du jeu.
	    """
        img1 = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "wizard1-final.png")))
        img1 = img1._PhotoImage__photo.zoom(12)
        img2 = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "wizard2-flip.png")))
        img2 = img2._PhotoImage__photo.zoom(12)

        #Initialisation de l'image Gauche
        label1 = Label(Frame2, image=img1, bg="#282c34", width=300, height=500)
        label1.pack(expand=YES)
        #Initialisation de l'image Droite
        label2 = Label(Frame4, image=img2, bg="#282c34", width=300, height=500)
        label2.pack(expand=YES)

        """
        Initialisation du cadre de connexion.
        Avec nom d'utilisateur, mot de passe et boutons.
        """
        labelUser = Label(Frame3, text="Nom d'utilisateur :", fg="#8601af", bg="#fafaee", font=("Letters for Learners", 40))
        labelUser.grid(column=1, row=0)
        
        #Cadre pour inscrire son nom d'utilisateur
        valueUser = StringVar()
        self.entreeUser = Entry(Frame3, textvariable=valueUser, width=30)
        self.entreeUser.grid(column=1, row=1, pady=20)

        #Texte Complémentaire
        labelPassword = Label(Frame3, text="Mot de passe :", fg="#8601af", bg="#fafaee", font=("Letters for Learners", 40))
        labelPassword.grid(column=1, row=2)
        
        #Cadre pour inscrire son mot de passe
        valuePassword = StringVar()
        self.entreePassword = Entry(Frame3, textvariable=valuePassword, width=30)
        self.entreePassword.grid(column=1, row=3, pady=20)

        #Texte Complémentaire
        Button(Frame3, text ='Connexion', command=lambda: self.verify(1), fg="#8601af", font=("Letters for Learners", 20)).grid(column=0, row=4, pady=10, padx=10)
        Button(Frame3, text ='Inscription', command=lambda: self.verify(2), fg="#8601af", font=("Letters for Learners", 20)).grid(column=2, row=4 ,pady=10, padx=10)

        #Création de la page
        self.screen.mainloop()     