'''
What are metaclasses in Python?
Classes describe objects. Meta-classes describe classes.
'''


class MetaEx(type):
    print('lol')


class Ex(metaclass=MetaEx):
    print('lol2')


obj = Ex()
# lol
# lol2
print('*'*50)


class MetaEx11(type):
    # Ex11 - __init__ gets salary, MetaEx11 created getSalary() for Ex11, etc.
    def __new__(cls, clsName, bases, dct):
        # this arguments (cls, clsName...) are just typed to use them in return statement,
        # dct used here has nothing to do with object.__dict__ or vars(object) which return properties, not attributes
        print(cls)  # <class '__main__.MetaEx11'>
        print(clsName)  # Ex11
        print(bases)  # ()
        print(dct)
        # {'__module__': '__main__', '__qualname__': 'Ex11', '__init__': <function Ex11.__init__ at 0x0000022A4F950A68>}

        # get var names of child class's __init__, including self--so we use slicing
        for var_name in dct['__init__'].__code__.co_varnames[1:]:
            # convert to lower_case to camelCase
            func_name = var_name.replace('_', ' ').title().replace(' ', '')

            dct['get' + func_name] = lambda self, var_name=var_name: print(
                self.__dict__[var_name])
            dct['set' + func_name] = lambda self, value, var_name=var_name: \
                setattr(self, var_name, value)

        return type.__new__(cls, clsName, bases, dct)  # just remember it


class Ex11(metaclass=MetaEx11):
    def __init__(self, first_name, last_name, age, salary, profession):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary
        self.profession = profession


obj = Ex11('Joe', 'Smith', 30, 120000.00, 'Back-End Developer')
obj.getFirstName()  # Joe
obj.getLastName()  # Smith
obj.getAge()  # 30
obj.getSalary()  # 120000.0
obj.getProfession()  # Back-End Developer
print()
obj.setFirstName('Joe2')  # Joe
obj.setLastName('Smith2')  # Smith
obj.setAge(302)  # 30
obj.setSalary(240000.0)  # 120000.0
obj.setProfession('Back-End 2')  # Back-End Developer
print()
obj.getFirstName()  # Joe2
obj.getLastName()  # Smith2
obj.getAge()  # 302
obj.getSalary()  # 240000.0
obj.getProfession()  # Back-End 2
