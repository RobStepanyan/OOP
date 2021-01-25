'''
How to get the parents classes of a class in Python?
'''


class A:
    pass


class B:
    pass


class C(A, B):
    pass


print(C.__bases__)
# Output: (<class '__main__.A'>, <class '__main__.B'>)
