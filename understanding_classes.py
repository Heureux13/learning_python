"""
A class is a blueprint of what an object is
containing attributes

A child class inherit behavior from its parent and can add to it, replace, or reuse it.
It does not control or modify the parent class.
"""

class Animal:
    def __init__(self, species:str, name:str):
        self.species = species
        self.name = name

    def describe(self):
        return f'{self.name} is a {self.species}'

    def speak(self):
        return f"{self.species} sounds"


"""Inheritance, here dog inherits from Animal, but
speak from Dog and Cat, override speak from Animal

It is create a new class from an existing class
"""
class Dog(Animal):
    def speak(self) -> str:
        return 'Woof'


"""super() lets the child class reuse methods from its parent"""
class Cat(Animal):
    def speak(self) -> str:
        animal_sound = super().speak()
        return f'{animal_sound}, but specifically: Meow'


doggo = Dog('Dog',  "Barko")
catto = Cat('Cat',  "Pickles")

print(doggo.describe())
print(catto.describe())
print(doggo.speak())
print(catto.speak())
print(f'\n')

"""Nested classes: an organizational relationship

A nested class is a class defined inside another class. It does not automatically inherit fro the outer class"""


def show_info() ->str:
    return "This is a processor"


class Computer:
    class Processor:
        pass

processor = Computer

print(processor.show_info())
print(f'\n')

"""They can be combined"""
class Zoo:
    class Lion(Animal):
        def speak(self) ->str:
            return "Roar"

lion = Zoo.Lion("Lion", "Leo")

print(lion.speak())
print(isinstance(lion, Animal))
print(isinstance(lion, Zoo))
print(f'Does class {Zoo} have an attribute called lion?: {hasattr(Zoo, "Lion")}')
print(f'\n')

"""Composition means one object contains another object"""
class Engine:
    def start(self) ->str:
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return self.engine.start()

car = Car()
print(car.start())

class Toolbox:
    class Hammer:
        def swing(self) ->str:
            return "swish"

hammer = Toolbox.Hammer()
print(Toolbox.Hammer.swing("string"))
print(f'Hammer is an attribute of toolbox: {hasattr(Toolbox, "Hammer")}')
print(f'Hammer is an instance of toolbox: {isinstance(hammer, Toolbox)}')
print(f'Hammer is an instance of Toolbox.Hammer: {isinstance(hammer, Toolbox.Hammer)}')