"""
*args and **kwargs

*args collects extra positional arguments into a tuple.
**kwargs collects extra keyword arguments into a dictionary
"""

def add_many(*numbers):
    return sum(numbers)

print(add_many(1,2))
print(add_many(1, 2, 3, 4, 5))
print()

def describe_person(**person):
    print(person)
    print(person["name"])
    print(person["city"])
    print()

describe_person(name="Frank", age=34, city="Denver")

def print_report(title, *items):
    print(f'Report: {title}')

    for item in items:
        print(f'- {item}')

# Will print out as if the * is not needed
print_report("Walls", "Wall A", "Wall B", "Wall C")
print()

# Where * can come in handy
title = "Walls"
items = ("Wall A", "Wall B", "Wall C")

# Have to pass the * in the argument
print_report(title, items)
print()
print_report(title, *items)
print()
# Can easily change it
print_report("Watter", *items)


