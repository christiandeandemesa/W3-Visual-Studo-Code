from pokemon_classes.firetype import FireType
from pokemon_classes.watertype import WaterType
import random

def battle_begins(firetype, watertype):
    print("\nYou have challenged Gym Leader Tyler to a battle!\n\nGym Leader Tyler sent out Charmander!\n\nGo Squirtle!\n")
    counter = 0
    while firetype.health > 0 and watertype.health > 0:
        if counter%2 == 0:
            firetype.fire_attack(watertype)
            squirtle.show_stats()
        else: 
            watertype.water_attack(firetype)
            charmander.show_stats()
        counter += 1
        if firetype.health <= 0:
            firetype.fire_death()
            watertype.water_win()
            print("Gym Leader Tyler gave you the Python Badge!")
        elif watertype.health <= 0:
            watertype.water_death()
            firetype.fire_win()
            print("Gym Leader Tyler says you should study instead of playing Pokemon!")

charmander = FireType("Charmander")
squirtle = WaterType("Squirtle")

battle_begins(charmander, squirtle)