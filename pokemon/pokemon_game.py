from pokemon_classes.firetype import FireType
from pokemon_classes.watertype import WaterType
def gym_battle(firetype, watertype):
    print(f"\nYou have challenged Gym Leader Tyler to a battle!\n\nGym Leader Tyler sent out {firetype.name}!\n") # How can I modify this to change the names of the pokemon battling?
    firetype.show_stats()
    print(f"Go {watertype.name}!\n") # How can I modify this to change the names of the pokemon battling?
    watertype.show_stats()
    counter = 0
    while firetype.hp > 0 and watertype.hp > 0:
        if counter%2 == 0:
            print("___________________________________________________________________________")
            print("Round: " + str(counter+1))
            firetype.fire_attack(watertype)
            watertype.show_stats()
        else:
            print("___________________________________________________________________________")
            print("Round: " + str(counter+1))
            watertype.water_attack(firetype)
            firetype.show_stats()
        counter += 1
        if firetype.hp <= 0:
            firetype.death()
            watertype.win()
            print("Gym Leader Tyler gave you the Python Badge!")
        elif watertype.hp <= 0:
            watertype.death()
            firetype.win()
            print("Gym Leader Tyler says you should study instead of playing Pokemon!\n\nGAME OVER!")

charmander = FireType("Charmander", 52, 43, 43, 60, 50, 39, 39)
squirtle = WaterType("Squirtle", 48, 65, 65, 50, 64, 44, 44)

gym_battle(charmander, squirtle)