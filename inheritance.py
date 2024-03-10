class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("the animal is eating..")


class dog(Animal):
    def bark(self):
        print("Woof Woof!")


d = dog("Rover", 5)
print(d.name)  # output is Rover
print(d.age)  # output is 5
d.eat()
d.bark()


# in this example the class "dog" is Drived from the class "Animal". the drived class "dog" inherite the attributes "name" "age" and the method "eat"
# from the base class "Animal". the drived class "dog" can also has its own metod "bark()".

# Multilple Inheritance#

class Bird:
    def fly(self):
        print("the bird is flying")


class Mammal:
    def run(self):
        print("the mammal is running")


class Bat(Bird, Mammal):
    pass


b = Bat()
b.fly()  # output: the bird is flying
b.run()  # output: the mammal is running


# In this example bat is drived from two base class "Bird" and "Mammal". the drived class "Bat" inherite the method "fly" and "run" from the base class "Bird" and "Mammal".

# SuperFunction#

class Animal:
    def eat(self):
        print("the animal is eating")


class Dog(Animal):
    def eat(self):
        super().eat()


print("the dog is also eating..")
d = Dog()
d.eat()  # output: the animal is eating.../n the dog is also eatin..


# In this example the "Dog" Overrides the method "eat" from the base class "Animal". the overriden method in the drived class calls the oveeriden method of the base class using super() function.

# Overriding Methods in Python:

class Animale:
    def make_sound(self):
        print("the animal make a sound")


class Dog(Animale):
    def make_sound(self):
        print("the dog make a sound")


a = Animale()  # Output: the animal make a sound
a.make_sound()

d = Dog()  # The animal make a sound
d.make_sound()  # the dog make s sound

# in this example "dog" override the method
# "make_sound" from the base class "Animal"
# when the method is called on an object of the drived class "dog" the ovverridden method in the drived class is excuted instead of the origen method the base class..
