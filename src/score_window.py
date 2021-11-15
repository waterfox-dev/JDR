import pyglet
import random
import json

from utils.file_path import FilePath
from tkinter import * 
from tkinter.messagebox import *
from PIL import ImageTk, Image

class ScoreWindow:

    def get_player_score(self):
        with open(FilePath.get("data", "registration.json"), "r") as r:
            data = json.load(r)
            for username in data :
                if username == self.player.name:
                    return data[username]["characteristic"]["score"]

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

    def __init__(self):
        
        self.screen = Tk()
        #self.player = player
        print(self.get_best_scores())
        self.screen.mainloop()

if __name__ == "__main__":
    ScoreWindow()