from abc import ABC, abstractmethod

VEHICLES = ["bike", "car", "bus", "truck"]
WASHING_TYPES = {
    'express': 0,
    'inside': 1,
    'outside': 2,
    'complex': 3,
    'full': 4,
    'super': 5
}
DIRTY_LEVELS = {
    0: 'super',
    1: 'full',
    2: 'complex',
    3: 'outside',
    4: 'inside',
    5: 'express'
}

class CarWashLuxMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class CarWashLux(metaclass=CarWashLuxMeta):
    def __init__(self, bikes, cars, buses, trucks, workers):
        self.bikes = bikes
        self.cars = cars
        self.buses = buses
        self.trucks = trucks
        self.workers = workers

    def info(self):
        print(f"Our car wash can serve: {self.bikes, self.cars, self.buses, self.trucks} and it has {self.workers} workers")

    def summary(self):
        print(f"bikes: {len(self.bikes)}, cars: {len(self.cars)}, buses: {len(self.buses)}, trucks: {len(self.trucks)}")


class Vehicle(ABC):

    def __init__(self, wash_type, vehicle_type, additional_service):
        self.wash_type = wash_type
        self.vehicle_type = vehicle_type
        self.additional_service = additional_service

    def type_of_vehicle(self):
        if self.vehicle_type not in VEHICLES:
            raise Exception(f"Incorrect vehicle type. Your vehicle type is {self.vehicle_type}, but should be one from this list: {VEHICLES}")
        else:
            return self.vehicle_type

    @abstractmethod
    def dirty_of_vehicle(self):
        raise NotImplementedError("This method is not realized")

    @abstractmethod
    def is_vehicle_clean(self):
        raise NotImplementedError("This method is not realized")

    def __repr__(self):
        return self.vehicle_type


class Worker(ABC):

    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle

    @abstractmethod
    def check_dirty_level(self):
        raise NotImplementedError("This method is not realized")

    @abstractmethod
    def clean_vehicle(self):
        raise NotImplementedError("This method is not realized")

    @abstractmethod
    def polish_vehicle(self):
        raise NotImplementedError("This method is not realized")

    def __repr__(self):
        return self.name


class Bike(Vehicle):

    def __init__(self, wash_type, vehicle_type, additional_service, clean_level=0):
        super().__init__(wash_type, vehicle_type, additional_service)
        self.clean_level = clean_level

    def dirty_of_vehicle(self):
        return DIRTY_LEVELS[self.clean_level]

    def is_vehicle_clean(self):
        return True if self.clean_level  <= 0 else False

    def cleaning(self):
        if self.is_vehicle_clean():
            print('Vehicle is clean')
        else:
            if self.additional_service and not self.is_vehicle_clean():
                self.clean_level -= 2
                if self.clean_level < 0:
                    self.clean_level = 0
            else:
                self.clean_level -= 1

    def print_state(self):
        print(f"State is: {DIRTY_LEVELS[self.clean_level]}")


class SomeWorker(Worker):

    def __init__(self, name, vehicle):
        super().__init__(name, vehicle)

    def check_dirty_level(self):
        print(f"Dirty level is {self.vehicle.dirty_of_vehicle()}")

    def clean_vehicle(self):
        while not self.vehicle.is_vehicle_clean():
            self.vehicle.cleaning()

    def polish_vehicle(self):
        if self.vehicle.additional_service:
            self.vehicle.cleaning()


bike1 = Bike('express', 'Bike1', True, 5)
bike2 = Bike('full', 'Bike2', False, 3)
worker1 = SomeWorker('Worker1', bike1)
worker2 = SomeWorker('Worker2', bike2)
car_wash = CarWashLux([bike1, bike2], [], [], [], [worker1, worker2])


car_wash.info()
car_wash.summary()
worker1.check_dirty_level()
worker1.clean_vehicle()
worker1.check_dirty_level()
print('-------------')
worker2.check_dirty_level()
worker2.clean_vehicle()
worker2.check_dirty_level()