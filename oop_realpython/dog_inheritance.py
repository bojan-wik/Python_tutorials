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

    # Instance methods
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

# Child class (inherits from Dog class)
class Pon(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child classes inherit attributes and behaviours from the parent class
figa = Pon("Figa", 7)
print(figa.description())

# Child classes have specific attributes and behaviours as well
print(figa.run("powolutku"))

# Is figa an instance of Pon()/Dog()?
print(isinstance(figa, Pon))
print(isinstance(figa, Dog))