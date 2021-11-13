from tkinter import * 
from tkinter.messagebox import *

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
    fenetre.title("Connexion")
    fenetre.config(background="#c2fcf3")

    """
    can = Canvas(fenetre, width=500, height=250)
    img = PhotoImage(file="pixelBG.png")
    can.create_image(200, 20, anchor=NW, image=img)
    can.place(x=0, y=0)
    """

    Frame1 = Frame(fenetre, height=300, width=500, borderwidth=10, bg="#ce71f0")
    Frame1.pack(expand=YES)

    labelUser = Label(Frame1, text="Nom d'utilisateur :")
    labelUser.pack(pady=1, padx=20)
    valueUser = StringVar()
    entreeUser = Entry(Frame1, textvariable=valueUser, width=30)
    entreeUser.pack(pady=20, padx=20)

    labelPassword = Label(Frame1, text="Mot de passe :")
    labelPassword.pack(pady=1, padx=20)
    valuePassword = StringVar()
    entreePassword = Entry(Frame1, textvariable=valuePassword, width=30)
    entreePassword.pack(pady=20, padx=20)

    Button(Frame1, text ='Connexion', command=lambda: verify(1)).pack(side=LEFT, padx=5, pady=5)
    Button(Frame1, text ='Inscription', command=lambda: verify(2)).pack(side=RIGHT, padx=5, pady=5)

    fenetre.attributes('-fullscreen',True)


    fenetre.mainloop()