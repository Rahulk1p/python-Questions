from collections import namedtuple
Car = namedtuple('Car','color mileage')
my_car = Car('red', 3124.8)

# We can retrieve the attribute
print(my_car.color)
print(my_car.mileage)

# We can get nice string
print(my_car)

# Like tuples, namedtuples are immutable:
my_car.color = 'blue'
# This will lead to below error.
"""
File "C:/MyDrive/D-Drive/Development/python-Questions/Tricks 7 Tips/NamedTupleAlternateToClass.py", line 13, in <module>
    my_car.color = 'blue'
AttributeError: can't set attribute
"""