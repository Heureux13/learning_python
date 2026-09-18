"""
Attributes are names attached to an object that describe what it is or what it can do.

There are two different types of Attributes: Data & Function

Data attributes usually store values assigned with self.name = value.

Methods are function attributes defined inside a class. There are 4 kinds:
    - Regular method   -> receives the instance automatically (self)
    - Static method     -> receives nothing automatically, just a helper related to the class
    - Class method      -> receives the class automatically (cls)
    - Property          -> a method (uses self) but accessed like a Data Attribute (no parentheses)

Rule of thumb:
    - Verb-like (does something, needs input) -> regular method
    - Noun-like (describes the object, no input needed) -> property
"""


class Worker:
    def __init__(self, fname, lname, ss_number) -> None:
        # Data Attributes
        self.fname = fname
        self.lname = lname
        self.ss_number = ss_number

    # Function Atrritubes

    # Regular Method Attribute
    def greet(self, greeting):
        return f'{greeting}!'

    @staticmethod
    # Static Method attribute
    def _get_emp_numb(number):
        return int(round(number**3/number*14, 0))

    @classmethod
    # Class Method Attribute
    def class_method(cls):
        pass

    @property
    # Property method attribute
    # Is function based but is accessed like a Data Attribute
    def whole_name(self):
        return f'{self.fname} {self.lname}'

    @property
    def emp_number(self):
        return int(round(self._get_emp_numb(self.ss_number)/10**10, 2))


def hasattr_00(self):
    # Greet attribute exisit in the class
    if hasattr(self, "greet"):
        return f'Greet attribute exist'
    else:
        return f'Grett attribute does not exist'


def hasattr_01(self):
    # Nothing attribute does not exisit in the class
    if hasattr(self, "nothing"):
        return f'Nothing attribute exist'
    else:
        return f'Nothing attribute does not exist'


e1 = Worker('John', 'Smith', 123121234)
print(e1.whole_name)
print(e1.emp_number)
print(hasattr_00(e1))
print(hasattr_01(e1))

print(e1.greet(
    f'Hello, my name is {e1.whole_name}, how can i help you today'))
