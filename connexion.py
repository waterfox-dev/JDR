from tkinter import * 

#class ConnexionPage:

fenetre = Tk()

can = Canvas(fenetre, width=500, height=250)
img = PhotoImage(file="fond.jpg")
can.create_image(140, 20, anchor=NW, image=img)
can.place(x=0, y=0)

Frame1 = Frame(fenetre, borderwidth=1, relief=FLAT)
Frame1.pack(side=TOP, padx=20, pady=20)

labelUser = Label(Frame1, text="Nom d'utilisateur :")
labelUser.pack(pady=1)
valueUser = StringVar()
entreeUser = Entry(Frame1, textvariable=valueUser, width=30)
entreeUser.pack(pady=20)

labelMdp = Label(Frame1, text="Mot de passe :")
labelMdp.pack(pady=1)
valueMdp = StringVar()
entreeMdp = Entry(Frame1, textvariable=valueMdp, width=30)
entreeMdp.pack(pady=20)

Button(Frame1, text ='Connexion').pack(side=LEFT, padx=5, pady=5)
Button(Frame1, text ='Inscription').pack(side=RIGHT, padx=5, pady=5)

fenetre.attributes('-fullscreen',True)


fenetre.mainloop()