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
    
    def already_registered_or_not(self):
        with open(FilePath.get("data", "registration.json"), "r") as r:
            data = json.load(r)
            for username in data :
                if username == self.username :
                    return True 
            else :
                False

    def login(self):
        with open(FilePath.get("data", "registration.json"), "r") as r:
            data = json.load(r)
            for username in data :
                if data[username]["password"] == self.password:
                    return True
            return False 

    def get_player_object(self):
        with open(FilePath.get("data", "registration.json"), "r") as r:
            data = json.load(r)
            for username in data :
                if username == self.username:
                    player = Creature("character", data[username]["characteristic"]["strength"], data[username]["characteristic"]["health"], "", username, data[username]["characteristic"]["score"])
                    return player

    def register(self):
        create_new_character(
            name=self.username,
            strength=self.player.strength,
            health=self.player.hp,
            caracter_sprite=random.choice(['wizard1-final.png','wizard2-final.png']),
            password=self.password,
            score = 0)

class ConnectionPage:

    def verify(self, id_button):
        if self.entreeUser.get() != "" and self.entreePassword.get() != "":
            player = FabriqueCreature.get_creature("character", self.entreeUser.get())
            connection = Connection(player, self.entreePassword.get())
            if id_button == 1:
                if connection.login():
                    print("Connecté")
                    self.screen.destroy()
                    MenuWindow(connection.get_player_object())
                else:
                    showerror("Erreur", "Votre nom d'utilisateur ou votre mot de passe est incorrect.")
            elif id_button == 2:
                if not connection.already_registered_or_not():
                    connection.register()
                    print("Enregistré")
                    self.screen.destroy()
                    NewPerso(player)
                else:
                    showinfo("Erreur", "Ce nom d'utilisateur est déjà pris.")
        else:
            showerror("Erreur", "Veuillez remplir votre nom d'utilisateur et votre mot de passe.")

    def __init__(self):
        
        self.screen = Tk() 
        self.screen.title("Connexion")
        #w, h = self.screen.winfo_screenwidth(), self.screen.winfo_screenheight()
        self.screen.geometry("1536x845")
        self.screen.config(background="#282c34")

        pyglet.font.add_file(FilePath.get("assets", "fonts", "Letters for Learners.ttf"))

        #Frame Titre du Jeu
        Frame1 = Frame(self.screen, height=80, width=300, borderwidth=10, bg="black")
        Frame1.grid(column=1, row=0, pady=50)
        #Frame Sprite gauche
        Frame2 = Frame(self.screen, height=500, width=300, borderwidth=1, bg="#282c34")
        Frame2.grid(column=0, row=1, padx=90)
        #Frame Menu de connexion
        Frame3 = Frame(self.screen, height=80, width=300, borderwidth=10, bg="#fafaee")
        Frame3.grid(column=1, row=1)
        #Frame Sprite droit
        Frame4 = Frame(self.screen, height=500, width=300, borderwidth=1, bg="#282c34")
        Frame4.grid(column=2, row=1, padx=100)

        labelTitle = Label(Frame1, text="Adventuria", fg="white", bg="#7f5fdd", font=("Letters for Learners", 80, "bold"))
        labelTitle.grid(column=0, row=0)

        img1 = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "wizard1-final.png")))
        img1 = img1._PhotoImage__photo.zoom(12)
        img2 = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "wizard2-flip.png")))
        img2 = img2._PhotoImage__photo.zoom(12)

        label1 = Label(Frame2, image=img1, bg="#282c34", width=300, height=500)
        label1.pack(expand=YES)
        
        label2 = Label(Frame4, image=img2, bg="#282c34", width=300, height=500)
        label2.pack(expand=YES)

        labelUser = Label(Frame3, text="Nom d'utilisateur :", fg="#8601af", bg="#fafaee", font=("Letters for Learners", 40))
        labelUser.grid(column=1, row=0)
        
        valueUser = StringVar()
        self.entreeUser = Entry(Frame3, textvariable=valueUser, width=30)
        self.entreeUser.grid(column=1, row=1, pady=20)

        labelPassword = Label(Frame3, text="Mot de passe :", fg="#8601af", bg="#fafaee", font=("Letters for Learners", 40))
        labelPassword.grid(column=1, row=2)
        
        valuePassword = StringVar()
        self.entreePassword = Entry(Frame3, textvariable=valuePassword, width=30)
        self.entreePassword.grid(column=1, row=3, pady=20)

        Button(Frame3, text ='Connexion', command=lambda: self.verify(1), fg="#8601af", font=("Letters for Learners", 20)).grid(column=0, row=4, pady=10, padx=10)
        Button(Frame3, text ='Inscription', command=lambda: self.verify(2), fg="#8601af", font=("Letters for Learners", 20)).grid(column=2, row=4 ,pady=10, padx=10)

        self.screen.mainloop()     