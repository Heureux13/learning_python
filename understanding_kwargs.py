"""
**kwargs

**kwargs collects keyword arguments into a dictionary
"""

# Keyword arguments have names
def show_values(**kwargs):
    # This function accepts any number of named arguments
    print(kwargs)

# When this is called they are collected into a dictionary
show_values(first="Wall A", second="Wall B")

# Collected into a dictionary
kwargs = {
    "first": "Wall A",
    "second": "Wall B",
}

# This is conceptually similar
show_values(first="Wall A", second="Wall B")

# To this
kwargs = {"first": "Wall A", "second": "Wall B"}


# At the function call **item unpacks
# With this dictionary
items ={
    "first": "Wall A",
    "second": "Wall B",
}

# This call unpacks the dictionary into named arguments
show_values(**items)

# It is the same as this
show_values(first="Wall A", second="Wall B")

# Which collects them right back into:
kwargs = {
    "first": "Wall A",
    "second": "Wall B",
}

# It is pointless in this example, but it shows what its doing

# if you did not know the names ahead of time
def print_settings(**settings):
    for name, value in settings.items():
        print(f"{name}: {value}")
print()

settings = {
    "view_name": "Floor Plan",
    "scale": 100,
    "discipline": "Architectural",
}

print_settings(**settings)