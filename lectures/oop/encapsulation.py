class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self._age = age
        self.__sex = sex

    def __test(self):
        pass

x = Person('Devid', 28, 'Male')
print(x.name)
print(x._age)
print(x.__sex)