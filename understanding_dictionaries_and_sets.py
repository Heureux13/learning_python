"""
Dictionaries and Sets

Dictionary comprehension:
{key_expr: value_expr for item in iterable}

set comprehension:
{expression for item in iterable}

Dictionary stores data as (key: value) pairs
"""

person = {
    "name": "Frank",
    "height": 6.0,
    "age": 34,
}

print(person["name"])       # Frank
print(person['height'])     # 6.0
print()

# Adding / updating
person["age"] = 35          # update
person["city"] = "Denver"   # add new key
print(person)
print()

# Safe access with .get()
# Using  person["email"] directly would raise a KeyError if the key does not exist .get() avoids that.
print(person.get("email"))  # None (no error)
print(person.get("email", "unknown")) # unknown
print()

# Looping over a dictionary
for key in person:
    print(key, "->", person[key])
print()

for key, value in person.items():
    print(key, "->", value)
print()

for value in person.values():
    print(value)
print()

for key in person.keys():
    print(key)
print()

# Dict comprehensions
# Same pattern as list comprehensions but with key: value
# {key_expr: value_expr for item in iterable}
numbers = [1, 2, 3, 4]
squares = {number: number * number for number in numbers}
print(squares)
print()

# With filtering
even_squares = {number: number * number for number in numbers if number % 2 == 0}
print(even_squares)
print()

#pyRevit style example building a local lookup table
rooms = [
    {"name":"Office", "area": 250},
    {"name":"Storage", "area": 80},
]

area_by_name = {room["name"]: room["area"] for room in rooms}
print(area_by_name)
print()

# Sets unique, unordered values
# A set automatically removes duplicates
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = set(numbers)
print(unique_numbers)
print()

# Set support fast membership checks
seen = {1, 2, 3}
print(2 in seen)
print(5 in seen)
print()

# Set operations
a = {1, 2, 3}
b = {2, 3, 4}

print(a | b)    # union: {1, 2, 3, 4}
print(a & b)    # intersection: {2, 3}
print(a - b)    # difference: {1}
print()

# Set comprehension
# {expression for item in iterable}
numbers = {1, 2, 2, 3, 4, 4}
unique_numbers = {number * number for number in numbers}
print(unique_numbers)   # {1, 4, 9, 16}
print()

# Practice
words = {"apple", "banana", "cherry", "date", "fig"}
word_dict = {word: len(word) for word in words}
print(word_dict)
print()

first_letters = {word[0] for word in words}
print(first_letters)
print()

words_longer_than_4 = {word: word.upper() for word in words if len(word) > 4}
print(words_longer_than_4)
print()