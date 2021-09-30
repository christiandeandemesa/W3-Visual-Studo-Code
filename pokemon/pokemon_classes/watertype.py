import random
class WaterType:

    def __init__(self, name):
        self.name = name
        self.strength = 25
        self.defense = 10
        self.health = 100
        self.original_health = 100

    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nDefense: {self.defense}\nHealth: {self.health}/{self.original_health}\n")

    def skull_bash(self, firetype):
        firetype.health -= (self.strength - firetype.defense)
        self.health -= (self.strength - self.defense)
        print(f"{self.name} used skull bash!\n{self.name} took recoil damage.\n")
        self.show_stats()
        return self
    
    def water_gun(self, firetype):
        firetype.health -= (self.strength - firetype.defense)*1.5
        print(f"{self.name} used water gun!\nIt's super effective!\n")
        return self
    
    def withdraw(self, firetype):
        self.defense += 1
        firetype.defense += 0
        print(f"{self.name} used withdraw!\n")
        self.show_stats()
        return self

    def splash(self, firetype):
        firetype.defense += 0
        print(f"{self.name} used splash!\nNothing happened.\n")
        return self

    def water_attack(self, firetype):
        attacks = [self.skull_bash, self.water_gun, self.withdraw, self.splash]
        random_num = random.randint(0,len(attacks)-1)
        attacks[random_num](firetype)

    def water_death(self):
        if self.health <= 0:
            print(f"{self.name} is unable to battle. \n")
        else:
            pass
        return self

    def water_win(self):
        print(f"{self.name} won the battle!\n")