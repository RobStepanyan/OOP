'''
How to use a super with parent class method.
'''


class Ex9:
    def shout(self, arg):
        return f'From Ex9\'s shout: {arg}'


class Ex99(Ex9):
    def __init__(self):
        print(super(Ex99, self).shout('Some msg from Ex99'))


Ex99()
# Output: From Ex9's shout: Some msg from Ex99
