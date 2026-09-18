"""
Functions in Python

A function is a reusable block of code

Basic pattern:
def function_name(parameters)
    return value
"""

# Basic function
def add(a:int|float, b:int|float)->float|int:
    return a + b

result = add(3, 4)
print(result)
print()

# Function with a default argument
def greet(name:str="Unknown")->str:
    return f'Hello, {name}'

print(greet("Frank"))
print()

# Keyword arguments
def describe_person(name:str, age:int, city:str)->str:
    return f'{name} is {age} years old and lives in {city}'

# In same order as the function
print(describe_person("Frank", 34, "Denver"))
# Out of order from function but spelled out
print(describe_person(city="Denver", name="Frank", age=34))
print()

def get_min_and_max(numbers: list[int])-> tuple[int, int]:
    return min(numbers), max(numbers)

low, high = get_min_and_max([5, 2, 9, 1])
print(low)
print(high)
print()