"""
List comprehensions

Basic pattern:
[expression for item in iterable]

With filtering:
[expression for item in iterable if condition]

With if/else:
[value_if_true if condition else value_if_false for item in iterable]

[number for number in numbers if condition]

['yes' if condition else 'no' for number in number]
"""

numbers = [1, 2, 3, 4, 5, 6]

# Transform every item
squares = [number * number for number in numbers]
print(squares)

# Keep only matching items
evens = [number for number in numbers if number % 2 == 0]
print(evens)

# Filter and transform
evens_square = [number * number for number in numbers if number % 2 == 0]
print(evens_square)

# Choose between two values
labels = ["even" if number % 2 == 0 else 'odd' for number in numbers]
print(labels)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cubes = [number ** 3 for number in numbers]
print(cubes)

greater_than_5 = [number for number in numbers if number > 5]
print(greater_than_5)

large_or_small = ["large" if number > 5 else 'small' for number in numbers]
print(large_or_small)