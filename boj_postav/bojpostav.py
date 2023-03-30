import tkinter as tk
import random

class Character:
    def __init__(self, race, name, health, attack, defense):
        self.race = race
        self.name = name
        self.health = int(health)
        self.max_health = int(health)
        self.attack = int(attack)
        self.defense = int(defense)
        self.is_alive = True

    def take_damage(self, damage):
        damage -= self.defense
        if damage > 0:
            self.health -= damage
            if self.health <= 0:
                self.is_alive = False

    def attack_target(self, target):
        damage = self.attack - target.defense
        target.take_damage(damage)

def start_battle():
    # Vytvoření dvou postav
    races = ["Human", "Elf", "Dwarf", "Orc", "Dragon"]
    player_race = "Human"  # Místo "Human" může být zvolena jiná rasa
    player_name = "Player"
    player_health = 50
    player_attack = 10
    player_defense = 5
    player = Character(player_race, player_name, player_health, player_attack, player_defense)

    enemy_race = random.choice(races)
    enemy_name = "Enemy"
    enemy_health = random.randint(30, 70)
    enemy_attack = random.randint(5, 15)
    enemy_defense = random.randint(1, 10)
    enemy = Character(enemy_race, enemy_name, enemy_health, enemy_attack, enemy_defense)

    # Souboj mezi postavami
    while player.is_alive and enemy.is_alive:
        player.attack_target(enemy)
        if enemy.is_alive:
            enemy.attack_target(player)

    # Výpis výsledků souboje
    if player.is_alive:
        result_label.config(text="Vítěz: " + player.name)
    else:
        result_label.config(text="Vítěz: " + enemy.name)

root = tk.Tk()
root.title("Souboj postav")

battle_button = tk.Button(root, text="Spuštění souboje", command=start_battle)
battle_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

quit_button = tk.Button(root, text="Ukončení aplikace", command=root.quit)
quit_button.pack()

root.mainloop()