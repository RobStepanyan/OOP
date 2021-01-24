'''
Example of __getitem__ and __setitem__ in Python
'''


class Ex6:
    def __init__(self, len=1):
        self.data = [None] * len

    def __setitem__(self, index, item):
        self.data[index] = item
        print(f'from __setitem__: inserted: "{item}" at index: "{index}"')

    def __getitem__(self, index):
        return f'from __getitem__: {self.data[index]}'


obj = Ex6()
obj[0] = 'Some value'  # from __setitem__: inserted: "Some value" at index: "0"
print(obj[0])  # from __getitem__: Some value
