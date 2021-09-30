from dojo_pets_classes.pet import Pet

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    def walk(self):
        print(f"{self.first_name} {self.last_name} took {self.pet.name} on a walk, and gave {self.pet.name} {self.treats}.\n")
        self.pet.play()
        return self
    def feed(self):
        print(f"{self.first_name} {self.last_name} fed {self.pet.name} {self.pet_food}.\n")
        self.pet.eat()
        return self
    def bathe(self):
        print(f"{self.first_name} {self.last_name} bathed {self.pet.name}.\n")
        print(f"{self.pet.name} said {self.pet.noise}.\n")
        return self

oliver = Pet("Oliver", "Cat", "backflip", 0, 0, "meow")
bianca = Ninja("Bianca", "Demesa", oliver, "Temptations", "Meow Mix")

bianca.walk().feed().bathe()