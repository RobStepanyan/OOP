'''
How to create data attributes of a class in run-time in python?
'''


class Ex3:
    pass


obj1 = Ex3()
obj2 = Ex3()

setattr(Ex3, 'attr', True)
print(obj1.attr)  # True
print(obj2.attr)  # True

# Setting attribute of an object (property)
setattr(obj1, 'attr2', False)
print(obj1.attr2)  # False
print(obj2.attr2)  # Error
