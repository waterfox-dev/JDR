import pyglet

from tkinter import *

from .utils.file_path import FilePath
from .creatures.fabriquecreature import FabriqueCreature
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

        CAN_Zone.pack()

        self.screen.mainloop()

if __name__ == "__main__":
    GameOverWindow(FabriqueCreature.get_creature("character", "waterfox"), "Loup")

#class WinWindow: