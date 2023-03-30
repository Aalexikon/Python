import random

class Being:
    
    def __init__(self, race, name, health, attack, defense):
        self.race    = race
        self.name    = name
        self.health   = health
        self.attack  = attack
        self.defense = defense
        
    def fight(self, defender):
        attackComplete = self.attack + random.randint(0, 6)
        defense = defender.defend()
        result = attackComplete - defense
        if result <= 0:
            print(f"Obránce {defender.name} se ubránil útoku")
            return
        else:
            defender.health -= result
            if defender.health <= 0:
                print(f"Obránce {defender.name} zemřel")
            else:
                print(f"Obránce {defender.name} má nyní {defender.health} zdraví")
    
    def defend(self):
        return self.defense + random.randint(0, 6)
    
postava01 = Being("trpaslík", "Monsoon", 40, 6, 8)
postava02 = Being("troll", "Sundowner", 40, 8, 3)

while(postava01.health > 0 and postava02.health > 0):
    
    postava01.fight(postava02)
    postava02.fight(postava01)
