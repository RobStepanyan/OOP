'''
How to copy all properties of an object
to another object in python
'''


class Ex1:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def __str__(self):
        return f'{self.value1}, {self.value2}'


obj1 = Ex1(1, 10)
obj2 = Ex1(2, 20)

print(obj1, obj2, sep=' / ')
# 1, 10 / 2, 20

print(obj1.__dict__)
# {'value1': 1, 'value2': 10}

obj2.__dict__.update(obj1.__dict__)

print(obj1, obj2, sep=' / ')
# 1, 10 / 1, 10
