"""
Composition

When one object stores a reference to another object and uses it as part of its behavior

- If you can say “X is a Y”, inheritance may fit. `Dog is an Animal`.
- If you can say “X has a Y”, composition fits. `Dog has an Owner`.
"""

##################################################
# Engine Class
##################################################
class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower

    def start(self):
        return f'Vroom with {self.horsepower} HP!'

##################################################
# Vehicle Class
##################################################
class Vehicle:
    def __init__(self, brand: str, model:str, engine:Engine):
        self.brand = brand
        self.model = model
        self.engine = engine

    def describe(self)->str:
        return f'{self.brand} {self.model}'

##################################################
# Truck Class
##################################################
class Truck(Vehicle):
    def __init__(self, brand: str, model: str, engine:Engine, bed_length: float):
        super().__init__(brand, model, engine) # Vehicle sets self.brand and self.model
        self.bed_length = bed_length   # Truck sets self.bed_length

    def describe(self)->str:
        base_description = super().describe()
        return f'{base_description} with a {self.bed_length} ft bed'

##################################################
# Testing
##################################################
v8 = Engine(380)
v1 = Truck("Toyota", "T100", v8, 6.5)
print(v1.describe())
print(issubclass(Truck, Vehicle))
print(isinstance(v1, Truck))
print(isinstance(v1, Vehicle))
print(v1.engine.start())