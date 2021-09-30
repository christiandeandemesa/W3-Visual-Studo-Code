import random
class FireType:

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
    
    def flamethrower(self, watertype):
        watertype.hp -= round(((90+self.special_attack)/watertype.special_defense)/1.5)
        print(f"\n{self.name} used flamethrower!\nIt's not very effective.\n")
        return self

    def scratch(self, watertype):
        watertype.hp -= round((40+self.attack)/watertype.defense)
        print(f"\n{self.name} used scratch!\n")
        return self

    def tail_whip(self, watertype):
        watertype.defense -= round(watertype.defense_original/6)
        print(f"\n{self.name} used tail whip!\nThe opponent's defense was lowered!\n")
        return self

    def guillotine(self, watertype):
        print(f"\n{self.name} used guillotine!")
        if watertype.hp <= 20:
            watertype.hp = 0
            print(f"It's a one-hit KO!\n")
        else:
            print(f"{self.name}'s guillotine missed.\n")
        return self
    
    def fire_attack(self, watertype):
        attacks = [self.flamethrower, self.scratch, self.tail_whip, self.guillotine]
        random_num = random.randint(0,len(attacks)-1)
        attacks[random_num](watertype)

    def death(self):
        print(f"{self.name} is unable to battle.\n")
        return self

    def win(self):
        print(f"{self.name} won the battle!\n")