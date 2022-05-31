from abc import abstractmethod, ABC
import random


class Person(ABC):
    def __init__(self, name, age, availability_of_money, own_house):
        self.name = name
        self.age = age
        self.availability_of_money = availability_of_money
        self.own_house = own_house

    @abstractmethod
    def info(self):
        raise NotImplementedError("This method is not realized")

    @abstractmethod
    def make_money(self, house):
        raise NotImplementedError("This method is not realized")

    @abstractmethod
    def buy_house(self, house):
        raise NotImplementedError("This method is not realized")


class Human(Person):
    def __init__(self, name, age, availability_of_money, own_house):
        super().__init__(name, age, availability_of_money, own_house)

    def info(self):
        print(f'Hi I am {self.name}. I am {self.age}')

    def make_money(self, house):
        while self.availability_of_money < house.cost:
            print("What a pity I need more money for this awesome house.\nOkay, I am going to work...")
            self.availability_of_money += 5000

    def buy_house(self, house):
        if self.own_house == 0:
            print(f'{self.name}:\nI want to buy this starling house')
            self.make_money(house)
            self.availability_of_money = self.availability_of_money - house.cost
            print(f'{self.name} buy {house.name} and now has $ {self.availability_of_money} left')
            self.own_house = 1
        else:
            print(f'{self.name}:\nI already have house and now I don\'t need another one')


class House:
    def __init__(self, name, area, cost):
        self.name = name
        self.area = area
        self.cost = cost

    def house_info(self):
        print(f'{self.name}:Area of house - {self.area} and it costs {self.cost}$')

    def discount(self):
        if self.area >= 60:
            print(f'{self.name} has a 20% discount')
            self.cost = self.cost * 0.8
        elif self.area >= 40 and self.area < 60:
            print(f'{self.name} has a 10% discount')
            self.cost = self.cost * 0.9
        else:
            print(f'{self.name} hasn\'t any discounts')


class SmallHouse(House):
    def __init__(self, name, area, cost):
        super().__init__(name, area, cost)
        if area > 40:
            self.__class__ = House


class RealtorMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):
    def __init__(self, name, houses, discount: bool):
        self.name = name
        self.houses = houses
        self.discount = discount

    def realtor_info(self):
        print(f'Hi, I\'m realtor {self.name} and I can help you with buying house!\n'
              f'Soo I can offer you some houses: ')

    def houses_info(self):
        for house in self.houses:
            house.house_info()

    def make_discount(self, house):
        if self.discount is True:
            house.discount()

    def steal_money(self, person):
        if random.randrange(11) == 10:
            person.availability_of_money = 0
            print(f'Luckily for {self.name} today,he was able to steal money from {person.name}')
        else:
            print('The realtor tried to steal the money, but he did not succeed')


person1 = Human("Robin", 25, 8000, 0)
person2 = Human("Linda", 19, 5000, 0)
person3 = Human("Cole", 28, 10000, 1)

person1.info()
person2.info()
person3.info()

house1 = House("Mansion", 30, 7000)
house2 = House("Penthouse", 45, 10000)
house3 = House("Cottage", 60, 6000)

realtor = Realtor("Paul", [house1, house2, house3], True)

realtor.realtor_info()
print("-" * 40)
realtor.houses_info()
print("-" * 40)

person1.buy_house(house2)
print("-" * 40)

realtor.make_discount(house3)
person2.buy_house(house3)
print("-" * 40)
person3.buy_house(house1)

print("-" * 40)
realtor.steal_money(random.choice([person1, person2, person3]))
