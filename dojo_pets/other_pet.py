from dojo_pets_classes.pet import Pet

class Stray(Pet):
    def __init__(self, name, type, tricks, health, energy, noise):
        super().__init__(name, type, tricks, health, energy, noise)
    def deep_sleep(self):
        self.sleep()
        self.sleep()
    def eat(self):
        self.energy += 10
        self.health += 20
        print(f"{self.name} ate a lot of food!\nPet Energy: {self.energy}\nPet Health: {self.health}\n")
        return self

athena = Stray("Athena", "Dog", "backflip", 0, 0, "bark")

athena.deep_sleep()
athena.eat()