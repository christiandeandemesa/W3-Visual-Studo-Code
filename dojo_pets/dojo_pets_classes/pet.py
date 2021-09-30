class Pet:
    def __init__(self, name, type, tricks, health, energy, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.noise = noise
    def sleep(self):
        self.energy += 25
        print(f"{self.name} slept.\nPet Energy: {self.energy}\n")
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} ate.\nPet Energy: {self.energy}\nPet Health: {self.health}\n")
        return self
    def play(self):
        if self.energy > 15:
            self.health += 5
            self.energy -= 15
            print(f"{self.name} did a {self.tricks}.\nPet Energy: {self.energy}\nPet Health: {self.health}\n")
        else:
            print(f"{self.name} is too tired.\nPet Energy: {self.energy}\n")
        return self
    def noise(self, type):
        print(self.noise)