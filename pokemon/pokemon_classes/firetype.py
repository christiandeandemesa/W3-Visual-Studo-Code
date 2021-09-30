import random
class FireType:

    def __init__(self, name):
        self.name = name
        self.strength = 30
        self.defense = 5
        self.health = 100
        self.original_health = 100
    
    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nDefense: {self.defense}\nHealth: {self.health}/{self.original_health}\n")

    def flamethrower(self, watertype):
        watertype.health -= (self.strength - watertype.defense)/1.5
        print(f"{self.name} used flamethrower!\nIt's not very effective.\n")
        return self

    def scratch(self, watertype):
        watertype.health -= (self.strength - watertype.defense)
        print(f"{self.name} used scratch!\n")
        return self

    def tail_whip(self, watertype):
        watertype.defense -= 2
        print(f"{self.name} used tail whip!\n")
        return self

    def guillotine(self, watertype):
        print(f"{self.name} used guillotine!")
        if watertype.health <= 40:
            watertype.health = 0
            print(f"It's a one-hit KO!\n")
        else:
            pass
            print(f"{self.name}'s guillotine missed.\n")
        return self
    
    def fire_attack(self, watertype):
        attacks = [self.flamethrower, self.scratch, self.tail_whip, self.guillotine]
        random_num = random.randint(0,len(attacks)-1)
        attacks[random_num](watertype)

    def fire_death(self):
        if self.health <= 0:
            print(f"{self.name} is unable to battle.\n")
        else:
            pass
        return self

    def fire_win(self):
        print(f"{self.name} won the battle!\n")