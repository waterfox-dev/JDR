from tkinter import * 
from tkinter.messagebox import *
from PIL import ImageTk, Image
import tkinter.font as tkFont

import csv

class Connection:

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def already_registered_or_not(self):
        with open("registration.csv", "r") as r:
            data = csv.reader(r)
            for row in data:
                if self.username == row[0]:
                    return True
            return False     

    def login(self):
        with open("registration.csv", "r") as r:
            data = csv.reader(r)
            for row in data:
                if self.username == row[0] and self.password == row[1]:
                    return True
            return False 

    def register(self):
        with open('registration.csv','a' ,newline='\n', encoding='utf-8') as r:
            writer=csv.writer(r)
            writer.writerow([self.username, self.password])

#class ConnectionPage:
if __name__ == "__main__":

    def verify(id_button):
        if entreeUser.get() != "" and entreePassword.get() != "":
            connection = Connection(entreeUser.get(), entreePassword.get())
            if id_button == 1:
                if connection.login():
                    print("Connecté")
                else:
                    showerror("Erreur", "Votre nom d'utilisateur ou votre mot de passe est incorrect.")
                    #Envoyé par page du menu
            elif id_button == 2:
                if not connection.already_registered_or_not():
                    connection.register()
                    print("Enregistré")
                    #Envoyé sur page du menu
                else:
                    showinfo("Erreur", "Ce nom d'utilisateur est déjà prit.")
        else:
            showerror("Erreur", "Veuillez remplir votre nom d'utilisateur et votre mot de passe.")

    fenetre = Tk()
    w, h = fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()
    fenetre.geometry("%dx%d" % (w, h))   
    fenetre.title("Connexion")
    fenetre.config(background="#282c34")

    """
    background_image= PhotoImage("pixelBG.png")
    background_label = Label(fenetre, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    """
    #Frame Titre du Jeu
    Frame1 = Frame(fenetre, height=80, width=200, borderwidth=10, bg="black")
    Frame1.grid(column=1, row=0, pady=50)
    #Frame Sprite gauche
    Frame2 = Frame(fenetre, height=500, width=231, borderwidth=1, bg="#282c34")
    Frame2.grid(column=0, row=1, padx=120)
    #Frame Menu de connexion
    Frame3 = Frame(fenetre, height=80, width=200, borderwidth=10, bg="#fafaee")
    Frame3.grid(column=1, row=1)
    #Frame Sprite droit
    Frame4 = Frame(fenetre, height=500, width=231, borderwidth=1, bg="#282c34")
    Frame4.grid(column=2, row=1, padx=120)

    labelTitle = Label(Frame1, text="Adventuria", fg="white", bg="#7f5fdd", font=("Roman", 80, "bold"))
    labelTitle.grid(column=0, row=0)

    img = ImageTk.PhotoImage(Image.open("spriteTest.png"))  
    
    label1 = Label(Frame2, image=img, bg="#282c34", width=231, height=500)
    label1.pack(expand=YES)
    
    label2 = Label(Frame4, image=img, bg="#282c34", width=231, height=500)
    label2.pack(expand=YES)

    labelUser = Label(Frame3, text="Nom d'utilisateur :", fg="#8601af", bg="#fafaee", font=("Roman", 30))
    labelUser.grid(column=1, row=0)
    
    valueUser = StringVar()
    entreeUser = Entry(Frame3, textvariable=valueUser, width=30)
    entreeUser.grid(column=1, row=1, pady=20)

    labelPassword = Label(Frame3, text="Mot de passe :", fg="#8601af", bg="#fafaee", font=("Roman", 30))
    labelPassword.grid(column=1, row=2)
    
    valuePassword = StringVar()
    entreePassword = Entry(Frame3, textvariable=valuePassword, width=30)
    entreePassword.grid(column=1, row=3, pady=20)

    Button(Frame3, text ='Connexion', command=lambda: verify(1), fg="#8601af", font=("Ebrima", 12)).grid(column=0, row=4, pady=10, padx=10)
    Button(Frame3, text ='Inscription', command=lambda: verify(2), fg="#8601af", font=("Ebrima", 12)).grid(column=2, row=4 ,pady=10, padx=10)

    fenetre.mainloop()