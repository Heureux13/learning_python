"""An instance is an object from a class

Class is a blueprint of an object
when that object is created it is an instance


"""


# Dog is our class
class Animal:
    def __init__(self, species):
        self.species = species

class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def bark(self) ->str:
        return 'Woof'

# Doggo is an instance of Class Dog
# Dog() means create a new instance of Dog
wolfie = Dog("Wolfie")
spot = Dog("spot")

x = isinstance(spot, Dog)
y = type(wolfie)

print(f'Is spot an instance of Dog: {x}')
print(f'What kind of type is doggo? {y}')
