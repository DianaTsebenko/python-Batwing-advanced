class Person:
    def __init__(self, my_attr=0):
        self.my_attr = my_attr

class_name = 'Person'
param = 0

MetaClass = type(class_name, (object, ), {"my_attr": param})

print(type(Person))
print(type(MetaClass))

obj = Person()
print(obj.my_attr)