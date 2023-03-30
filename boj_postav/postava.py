class Being:

    def __init__(self, race, name, hp, attack, defense):
        self.race    = race
        self.name    = name
        self.hp      = hp
        self.attack  = attack
        self.defense = defense

    def fight(self, defender):
        pass

    def defend(self):
        pass