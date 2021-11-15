import pyglet

from tkinter import *

from .utils.file_path import FilePath
from .utils.saver import save_character
import src.menu as menu

class GameOverWindow:

    def lose_point(self):
        lost_points = 3 if self.winning_kind == "Loup" else 2 if self.winning_kind == "Gobelin" else 1 if self.winning_kind == "Troll" else None
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
        PointsInfo = CAN_Zone.create_text(425, 480, text=f"A ce jour, vous possèdez {self.player.score} points.", font=("Letters for Learners", 45, UNDERLINE), anchor="nw")

        QuitButton = Button(CAN_Zone, text="Continuer", font=("Letters for Learners", 25), height=1, width=10, bg="#faa413", fg="#20a0ff", command=lambda: self.return_to_menu())
        WindowToMenu = CAN_Zone.create_window(20, 20, anchor="nw", window=QuitButton)

        save_character(name=self.player.name, strength=self.player.strength, health=self.player.hp, character_sprite=self.player.sprite, score=self.player.score)

        CAN_Zone.pack()

        self.screen.mainloop()

class WinWindow:

    def win_point(self):
        win_points = 1 if self.winning_kind == "Loup" else 3 if self.winning_kind == "Gobelin" else 5 if self.winning_kind == "Troll" else None
        self.player.score += win_points
        return win_points

    def return_to_menu(self):
        player = self.player
        self.screen.destroy()
        menu.MenuWindow(player)

    def __init__(self, player, winning_kind):

        self.screen = Tk()
        self.player = player
        self.screen.title("Victoire")
        self.winning_kind = winning_kind

        pyglet.font.add_file(FilePath.get("assets", "fonts", "Letters for Learners.ttf"))

        IMG_Image = PhotoImage(file=FilePath.get("assets", "images", "WinBG.png"))
        CAN_Zone = Canvas(self.screen, height=845, width=1536)
        CAN_Zone_Image = CAN_Zone.create_image(0, 0, image=IMG_Image, anchor="nw")

        PointsLoseFrame = CAN_Zone.create_rectangle(660, 300, 1420, 500, width=3, fill="#fbcd24")

        PointsLose = CAN_Zone.create_text(780, 310, text=f"Vous avez gagné {self.win_point()} points\npour avoir vaincu un {winning_kind.lower()} !", font=("Letters for Learners", 40), anchor="nw")
        PointsInfo = CAN_Zone.create_text(705, 430, text=f"A ce jour, vous possèdez {self.player.score} points.", font=("Letters for Learners", 45, UNDERLINE), anchor="nw")

        QuitButton = Button(CAN_Zone, text="Continuer", font=("Letters for Learners", 25), height=1, width=10, bg="#ff3455", fg="white", command=lambda: self.return_to_menu())
        WindowToMenu = CAN_Zone.create_window(20, 20, anchor="nw", window=QuitButton)
        
        save_character(name=self.player.name, strength=self.player.strength, health=self.player.hp, character_sprite=self.player.sprite, score=self.player.score)

        CAN_Zone.pack()

        self.screen.mainloop()