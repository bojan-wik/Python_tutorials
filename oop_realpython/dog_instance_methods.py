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

# Instantiate the Dog object
pluto = Dog("Pluto", 2)

# Call out our instance methods
print(pluto.description())
print(pluto.speak("hau-hau"))