import json

from .file_path import FilePath

def create_new_character(name : str, strength : int, health : int, caracter_sprite : str, password : str, score : int):
    with open(FilePath.get("data", "registration.json"), "r") as file :
        file = json.load(file)
        file[name] = {}
        file[name] = {
            "password" : password,
            "character_sprite" : caracter_sprite,
            "characteristic" : {
                "name" : name, 
                "strength" : strength,
                "health" : health,
                "score" : score 
            }
        }
        with open(FilePath.get("data", "registration.json"), "w") as writer : 
            json.dump(file, writer)

def save_character(name : str, strength : int, health : int, caracter_sprite : str, password : str, score : int):
    with open(FilePath.get("data", "registration.json"), "r") as file :
        file = json.load(file)
        file[name] = {
            "password" : password,
            "character_sprite" : caracter_sprite,
            "characteristic" : {
                "name" : name, 
                "strength" : strength,
                "health" : health,
                "score" : score 
            }
        }
        with open(FilePath.get("data", "registration.json"), "w") as writer : 
            json.dump(file, writer)

