import json

from .file_path import FilePath

def create_new_character(name : str, strength : int, health : int, character_sprite : str, password : str, score : int, coins : int):
    with open(FilePath.get("data", "registration.json"), "r") as file :
        file = json.load(file)
        file[name] = {}
        file[name] = {
            "password" : password,
            "character_sprite" : character_sprite,
            "characteristic" : {
                "name" : name, 
                "strength" : strength,
                "health" : health,
                "score" : score,
                "coins" : coins
            },
            "items" : []
        }
        with open(FilePath.get("data", "registration.json"), "w") as writer : 
            json.dump(file, writer)

def save_character(name : str, strength : int, health : int, character_sprite : str, score : int, coins : int, items : list):
    with open(FilePath.get("data", "registration.json"), "r") as file :
        file = json.load(file)        
        file[name] = {
            "password" : file[name]["password"],
            "character_sprite" : character_sprite,
            "characteristic" : {
                "name" : name, 
                "strength" : strength,
                "health" : health,
                "score" : score,
                "coins" : coins
            },
            "items" : items
        }
        with open(FilePath.get("data", "registration.json"), "w") as writer : 
            json.dump(file, writer)

