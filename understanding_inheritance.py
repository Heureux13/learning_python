"""
Inheritance

inheritance means creating a child class from a parent class.

Patterns:

class Child(Parent):
    pass

The parent class goes inside the parentheses.

Example:
    - Animal is the parent/base class.
    - Dog is the child/sublcass.
    - A Dog is also an Animal.

- If you can say “X is a Y”, inheritance may fit. `Dog is an Animal`.
- If you can say “X has a Y”, composition fits. `Dog has an Owner`.
"""

class Animal:
    def __init__(self, species:str, name:str):
        self.species = species
        self.name = name

    def describe(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    def __init__(self, name:str, breed:str):
        # Give super().__init__ the arguments it needs for the Animal part of Dog
        super().__init__("dog", name)
        self.breed = breed

    def describe(self):
        # Dog.describe overrides Animal.describe, but reuses the parent version with super()
        base_description = super().describe()
        return f"{base_description}. Breed: {self.breed}"

dog = Dog("Spot", "Chihuahua")

print(dog.describe())
print(isinstance(dog, Dog))     # dog is an instance of Dog
print(isinstance(dog, Animal))  # dog is an instance of Animal
print(isinstance(Dog, Animal))  # Dog is not an instance of Animal
print(issubclass(Dog, Animal))  # Dog is a subclass of