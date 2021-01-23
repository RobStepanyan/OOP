# Polymorphism is the ability to treat a class differently depending on which subclass is implemented.
class Dog:
    def make_sound(self):
        print('Bark')


class Cat:
    def make_sound(self):
        print('Meow')


for x in [Cat(), Dog()]:
    x.make_sound()

# Result:
# Meow
# Bark
