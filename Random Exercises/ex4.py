'''
Variables declared inside the class definition, but not inside a method are class or static variables or attributes (not properties).
'''


class Ex4:
    x = 25


obj = Ex4()
print(obj.x)  # 25
obj.x = 30
print(obj.x)  # 30
print(Ex4.x)  # 25
Ex4.age = 30
print(Ex4.age)  # 30
