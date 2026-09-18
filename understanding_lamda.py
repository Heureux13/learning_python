"""
Lambda

lambda arguments: expression

Lambda is a small unnamed function written in one line
"""


def square(x:int|float)->float|int:
    # Same as the lambda below
    return x * x

square_lambda = lambda x:x * x
print(square(5))

# Store it as a varible and call it yourself
add = lambda a, b: a + b
print(add(3,4))

# filter() keep only items that pass a test
numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda n: n % 2 == 0, numbers)
print(list(evens))

# map() transform every item
numbers = [1, 2, 3]
double = map(lambda n: n*2, numbers)
print(list(double))

# max()/min() same key= idea as sorted
class Person:
    def __init__(self, name: str, height:float):
        self.name = name
        self.height = height

people = [
    Person("Frank", 6.0),
    Person("James", 5.5),
    Person("Sam", 6.2),
]
# Returns the object Person(name, height)
tallest_person = max(people,key=lambda person: person.height)

print(tallest_person.name)
print(tallest_person.height)

# Lambda with 3 arguments
multiply = lambda a, b, c: a * b * c
print(multiply(2,3, 4))