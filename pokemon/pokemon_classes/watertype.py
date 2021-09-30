import random
class WaterType:

    def __init__(self, name, attack, defense, defense_original, special_attack, special_defense, hp, original_hp):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.defense_original = defense_original
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.hp = hp
        self.original_hp = original_hp

    def show_stats(self):
        print(f"Name: {self.name}\nAttack: {self.attack}\nDefense: {self.defense}\nSp. Atk: {self.special_attack}\nSp. Def: {self.special_defense}\nHP: {self.hp}/{self.original_hp}\n")

    def skull_bash(self, firetype):
        firetype.hp -= round((130+self.attack)/firetype.defense)
        self.hp -= round((130/3+self.attack)/self.defense)
        print(f"\n{self.name} used skull bash!\n{self.name} took recoil damage.\n")
        self.show_stats()
        return self
    
    def water_gun(self, firetype):
        firetype.hp -= round(((40+self.special_attack)/firetype.special_defense)*1.5)
        print(f"\n{self.name} used water gun!\nIt's super effective!\n")
        return self
    
    def withdraw(self, firetype):
        self.defense += round(self.defense_original/6)
        firetype.defense += 0
        print(f"\n{self.name} used withdraw!\n{self.name}'s defense was increased!\n")
        self.show_stats()
        return self

    def splash(self, firetype):
        firetype.defense += 0
        print(f"\n{self.name} used splash!\nNothing happened.\n")
        return self

    def water_attack(self, firetype):
        attacks = [self.skull_bash, self.water_gun, self.withdraw, self.splash]
        random_num = random.randint(0,len(attacks)-1)
        attacks[random_num](firetype)

    def death(self):
        print(f"{self.name} is unable to battle. \n")
        return self

    def win(self):
        print(f"{self.name} won the battle!\n")