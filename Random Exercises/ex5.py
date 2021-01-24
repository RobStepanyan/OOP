'''
An iterator
'''


class Iterator:
    def __init__(self, start, end, step=1):
        self.index = start
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        # __iter__ is called before __next__ once
        print(self)  # <__main__.Iterator object at 0x000001465A203DC8>
        return self

    def __next__(self):
        if not (self.index + self.step) in range(self.start, self.end+self.step):
            raise StopIteration
        else:
            self.index += self.step
            return self.index - self.step


iteratable = Iterator(0, 10, 2)
while True:
    try:
        print(iteratable.__next__())
        # or print(next(iterable))
    except StopIteration:
        break

'''
Result:
0
2
4
6
8
'''
