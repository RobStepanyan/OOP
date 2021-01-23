# Encapuslation
class ClassName:
    attribute = 'value'
    __hidden_attribute = 'value2'


c = ClassName()
print(c.__class__.attribute)
print(c.__class__.hidden_attribute)  # causes error (has no attribute


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method


class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
