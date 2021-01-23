'''
How to iterate over object attributes and properties in python.
'''


class Ex2:
    a1 = True
    a2 = False

    def __init__(self):
        self.prop1 = 'smth'
        self.prop2 = 'smth2'

    def attr_func(self):
        return 'Hi'


obj = Ex2()
print([x for x in dir(obj) if not x[:2] == '__'])
# ['a1', 'a2', 'attr_func', 'prop1', 'prop2']

# for properties only
print(obj.__dict__)
# or
print(vars(obj))
