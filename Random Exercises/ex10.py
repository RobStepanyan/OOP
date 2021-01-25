'''
mro stands for Method Resolution Order. It returns a list of types
the class is derived from, in the order they are searched for methods.
'''


class Ex10:
    def method(self):
        print('Ex10 method')


class Ex100(Ex10):
    pass


class Ex1000(Ex100):
    pass


obj = Ex10()
obj.method()  # Ex10 method
print(Ex1000.__mro__)
# (<class '__main__.Ex1000'>, <class '__main__.Ex100'>, <class '__main__.Ex10'>, <class 'object'>)
