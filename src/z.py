class BattleWindow:

    def to_escape(self):
        chance = [True, False, False]
        if random.choice(chance):
            player = self.player
            save_character(name=self.player.name, strength=self.player.strength, health=self.player.hp, character_sprite=self.player.sprite, score=self.player.score)
            self.screen.destroy()
            menu.MenuWindow(player)
        else:
            self.display_fail_escape(True)
            lost_hp = random.randint(1,3)
            self.player.hp -= lost_hp

    def display_fail_escape(self, state):
        if state:
            self.CAN_Zone.itemconfigure(fail_escape_frame, state="hidden")
            self.CAN_Zone.itemconfigure(fail_escape_text1, state="hidden")
            self.CAN_Zone.itemconfigure(fail_escape_text2, state="hidden")

    def display_item(self):
        return "Hello World"

    def get_sprite(self):
        with open(FilePath.get("data", "registration.json"), "r") as r:
            data = json.load(r)
            for username in data :
                if username == self.player.name:
                    return data[username]["character_sprite"]

    def fight(self, statsHp, statsHpCreature):
        self.display_fail_escape(False)
        FightLoser = Jeu.FightCreature(self.player, self.creature)
        if FightLoser.kind == "character":
            self.player.hp = FightLoser.hp
            if self.player.hp <= 0:
                self.player.hp = 0
                player = self.player
                self.screen.destroy()
                go_or_win.GameOverWindow(player, self.creature.kind)
            else:
                self.CAN_Zone.itemconfigure(statsHp, text=f"Vie : {self.player.hp} Hp")
        else:
            self.creature.hp = FightLoser.hp
            if self.creature.hp <= 0:
                player = self.player
                self.screen.destroy()
                go_or_win.WinWindow(player, self.creature.kind)
            else:
                self.CAN_Zone.itemconfigure(statsHpCreature, text=f"Vie : {self.creature.hp} Hp")


    def __init__(self, player, creature) :
        
        self.screen = Tk() 
        self.screen.title("Combat ton adversaire !")
        self.screen.geometry("1536x845")
        self.player = player
        self.creature = creature

        pyglet.font.add_file(FilePath.get("assets", "fonts", "Letters for Learners.ttf"))

        self.CAN_Zone = Canvas(self.screen, height=845, width=1536)
        img = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", "PixelBG3.png")))
        CAN_BG_Image = self.CAN_Zone.create_image(0, 0, image=img, anchor="nw")

        sprite_player = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", self.get_sprite())))
        sprite_player = sprite_player._PhotoImage__photo.zoom(6)
        CAN_SpritePlayer_Image = self.CAN_Zone.create_image(400, 400, image=sprite_player, anchor="nw")

        sprite_creature = ImageTk.PhotoImage(Image.open(FilePath.get("assets", "images", self.creature.sprite)))
        sprite_creature = sprite_creature._PhotoImage__photo.zoom(4)
        CAN_SpriteCreature_Image = self.CAN_Zone.create_image(850, 420, image=sprite_creature, anchor="nw")

        attack_button = Button(self.CAN_Zone, text = "Attaque", command=lambda: self.fight(statsHp, statsHpCreature), height=1, width=9, bg="#59322d", fg="white", font=("Letters for Learners", 26))
        windowAttack = self.CAN_Zone.create_window(20, 710, anchor="nw", window=attack_button)

        item_button = Button(self.CAN_Zone, text = "Items", command = self.display_item, height=1, width=9, bg="#59322d", fg="white", font=("Letters for Learners", 26))
        windowItem = self.CAN_Zone.create_window(190, 710, anchor="nw", window=item_button)

        leak_button = Button(self.CAN_Zone, text = "Fuite", command = self.to_escape, height=1, width=9, bg="#59322d", fg="white", font=("Letters for Learners", 26))
        windowLeak = self.CAN_Zone.create_window(360, 710, anchor="nw", window=leak_button)
        
        stats = self.CAN_Zone.create_rectangle(340, 260, 580, 390, width=3, fill="#b4f3fa")
        statsName = self.CAN_Zone.create_text(460, 285, text=f"※ {self.player.name} ※", font=("Letters for Learners", 25), fill="#6d1212")
        statsStrength = self.CAN_Zone.create_text(460, 325, text=f"Force : {self.player.strength} Mana", font=("Letters for Learners", 23), fill="#6d1212")
        statsHp = self.CAN_Zone.create_text(460, 365, text=f"Vie : {self.player.hp} Hp", font=("Letters for Learners", 23), fill="#6d1212")
        
        statsCreature = self.CAN_Zone.create_rectangle(855, 260, 1095, 390, width=3, fill="#b4f3fa")
        statsNameCreature = self.CAN_Zone.create_text(975, 285, text=f"☬ {self.creature.kind} ☬", font=("Letters for Learners", 25), fill="#6d1212")
        statsStrengthCreature = self.CAN_Zone.create_text(975, 325, text=f"Force : {self.creature.strength} Mana", font=("Letters for Learners", 23), fill="#6d1212")
        statsHpCreature = self.CAN_Zone.create_text(975, 365, text=f"Vie : {self.creature.hp} Hp", font=("Letters for Learners", 23), fill="#6d1212")
        
        lost_hp = random.randint(1,3)
        self.fail_escape_frame = self.CAN_Zone.create_rectangle(855, 260, 1095, 390, width=3, fill="#b4f3fa")
        self.fail_escape_text1 = self.CAN_Zone.create_text(975, 285, text="Tu as voulu fuir ?", font=("Letters for Learners", 23), fill="#6d1212")
        self.fail_escape_text2 = self.CAN_Zone.create_text(975, 340, text=f"Pour le peine tu\nvas perdre {lost_hp} Hp", font=("Letters for Learners", 23), fill="#6d1212")
        self.CAN_Zone.itemconfigure(self.fail_escape_frame, state="hidden")
        self.CAN_Zone.itemconfigure(self.fail_escape_text1, state="hidden")
        self.CAN_Zone.itemconfigure(self.fail_escape_text2, state="hidden")

        self.CAN_Zone.pack()

        self.screen.mainloop()