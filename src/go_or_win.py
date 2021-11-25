import pyglet
import random

from tkinter import *

from .utils.file_path import FilePath
from .utils.saver import save_character
import src.menu as menu

class GameOverWindow:

    def lose_point(self):
        lost_points = 3 if self.winning_kind == "Loup" else 2 if self.winning_kind == "Gobelin" else 1 if self.winning_kind == "Troll" else 50 if self.winning_kind == "Boss" else None
        self.player.score -= lost_points
        return lost_points

    def return_to_menu(self):
        player = self.player
        self.screen.destroy()
        menu.MenuWindow(player)

    def __init__(self, player, winning_kind):

        self.screen = Tk()
        self.screen.geometry("1536x845")
        self.screen.title("GameOver")
        self.player = player
        self.winning_kind = winning_kind

        pyglet.font.add_file(FilePath.get("assets", "fonts", "Letters for Learners.ttf"))

        IMG_Image = PhotoImage(file=FilePath.get("assets", "images", "GameOverBG.png"))
        CAN_Zone = Canvas(self.screen, height=845, width=1536)
        CAN_Zone_Image = CAN_Zone.create_image(0, 0, image=IMG_Image, anchor="nw")

        PointsLoseFrame = CAN_Zone.create_rectangle(380, 350, 1150, 550, width=3, fill="#fee206")

        PointsLose = CAN_Zone.create_text(500, 360, text=f"Vous avez perdu {self.lose_point()} points pour\navoir été vaincu par un {winning_kind.lower()} !", font=("Letters for Learners", 40), anchor="nw")
        PointsInfo = CAN_Zone.create_text(425, 480, text=f"A ce jour, vous possédez {self.player.score} points.", font=("Letters for Learners", 45, UNDERLINE), anchor="nw")

        QuitButton = Button(CAN_Zone, text="Continuer", font=("Letters for Learners", 25), height=1, width=10, bg="#faa413", fg="#20a0ff", command=lambda: self.return_to_menu())
        WindowToMenu = CAN_Zone.create_window(20, 20, anchor="nw", window=QuitButton)

        save_character(name=self.player.name, strength=self.player.strength, health=self.player.hp, character_sprite=self.player.sprite, score=self.player.score, coins=self.player.coins, items=self.player.items)

        CAN_Zone.pack()

        self.screen.mainloop()

class WinWindow:

    def win_point(self):
        win_points = 1 if self.winning_kind == "Loup" else 3 if self.winning_kind == "Gobelin" else 5 if self.winning_kind == "Troll" else 50 if self.winning_kind == "Boss" else None
        self.player.score += win_points
        if self.item == None:
            self.player.coins += win_points
            return win_points
        elif self.item == "Book":
            self.player.coins += win_points*10
            return win_points*10        

    def return_to_menu(self):
        player = self.player
        self.screen.destroy()
        menu.MenuWindow(player)

    def __init__(self, player, winning_kind, item):

        self.screen = Tk()
        self.player = player
        self.screen.geometry("1536x845")
        self.screen.title("Victoire")
        self.winning_kind = winning_kind
        self.item = item

        pyglet.font.add_file(FilePath.get("assets", "fonts", "Letters for Learners.ttf"))

        IMG_Image = PhotoImage(file=FilePath.get("assets", "images", "WinBG.png"))
        CAN_Zone = Canvas(self.screen, height=845, width=1536)
        CAN_Zone_Image = CAN_Zone.create_image(0, 0, image=IMG_Image, anchor="nw")

        PointsWinFrame = CAN_Zone.create_rectangle(660, 300, 1450, 500, width=3, fill="#fbcd24")

        win_coins_score = self.win_point()
        PointsWin = CAN_Zone.create_text(1050, 370, text=f"Vous avez gagné {win_coins_score} points, ainsi que {win_coins_score}\nCoins, pour avoir vaincu un {winning_kind.lower()} !", font=("Letters for Learners", 40), anchor="center")
        PointsInfo = CAN_Zone.create_text(705, 430, text=f"A ce jour, vous possédez {self.player.score} points.", font=("Letters for Learners", 45, UNDERLINE), anchor="nw")

        QuitButton = Button(CAN_Zone, text="Continuer", font=("Letters for Learners", 25), height=1, width=10, bg="#ff3455", fg="white", command=lambda: self.return_to_menu())
        WindowToMenu = CAN_Zone.create_window(20, 20, anchor="nw", window=QuitButton)
        
        if winning_kind == "Boss":
            items_to_give = []
            nb_items_to_give = random.randint(3, 5)
            for _ in range(nb_items_to_give):
                items_to_give.append(random.choice(["Epée Sacrée", "Portail de Téléportation", "Potion de Vie", "Grimoire d'Or", "Anneau de Sorcier"]))
            for i in items_to_give:
                self.player.items.append(i)
            ItemsWinFrame = CAN_Zone.create_rectangle(580, 570, 1450, 700, width=3, fill="#fbcd24")
            congratulation = CAN_Zone.create_text(600, 590, text="Bravo, vous avez vaincu un Boss ! Vous avez récupéré ses armes :", anchor="nw", font=("Letters for Learners", 25))
            items_congratulations = CAN_Zone.create_text(600, 650, text=', '.join(items_to_give), anchor="nw", font=("Letters for Learners", 20))

        save_character(name=self.player.name, strength=self.player.strength, health=self.player.hp, character_sprite=self.player.sprite, score=self.player.score, coins=self.player.coins, items=self.player.items)

        CAN_Zone.pack()

        self.screen.mainloop()