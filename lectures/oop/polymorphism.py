str_line = 'Testing'
list_obj = [1, 2, 3, 4]
dict_obj = {'1': 1, '2': 2, '3': 3}

print(len(str_line))
print(len(list_obj))
print(len(dict_obj))

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('I am cat')

    def make_sound(self):
        print('Meow')


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('I am dog')

    def make_sound(self):
        print('Bark')

cat = Cat('Cat', 2)
dog = Dog('Dog', 3)

for animal in (cat, dog):
    animal.make_sound()
    animal.info()