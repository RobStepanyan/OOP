'''
The __del__ is a finalizer. 
It is called when an object is garbage collected 
which happens at some point after ALL references to the object have been deleted.
'''


class Ex7:
    def __del__(self):
        print('Byeee')


obj = Ex7()
obj = 'Other value'
# Output: Byeee

obj = Ex7()
del obj
# Output: Byeee
