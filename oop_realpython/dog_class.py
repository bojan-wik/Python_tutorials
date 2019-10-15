'''
https://realpython.com/python3-object-oriented-programming/
'''
# The class is for defining the Dog, not actually creating instances of individual dogs with specific names and ages
class Dog:

    # Class Attribute (the same for all instance)
    species = "mammal"

    # Initializer: __init__() method gets called automatically when you create a new ‘Dog’ instance.
    def __init__(self, name, age):
        # Instance Attributes (specific to each object)
        self.name = name
        self.age = age

# Instantiate the Dog object
burek = Dog("Burek", 5)
azor = Dog("Azor", 6)

# Access the instance attributes
print("{} is {} and {} is {}.".format(burek.name, burek.age, azor.name, azor.age))

# Is Burek a mammal?
if burek.species == "mammal":
    print("{0} is a {1}!".format(burek.name, burek.species))

