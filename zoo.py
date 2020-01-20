from animals import Penguin, PaintedDog
from habitats import Habitat


bob = Penguin("Bob")
bob.run()
bob.swim()

ralph = PaintedDog("Ralph")

# Create a habitat
seaworld = Habitat("Sea World")
seaworld.add_swimmer_pythonic(bob)
seaworld.add_swimmer_pythonic(ralph)
# seaworld.add_swimmer_type_check(ralph)

for animal in seaworld.animals:
    print(f'{animal} lives in Sea World')

for animal in seaworld.animals:
    print(animal)