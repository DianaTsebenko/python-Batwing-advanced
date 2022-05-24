
class Car:
    def __init__(self, engine):
        self.engine = engine

class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type


engine = Engine('Diesel')
car = Car(engine)

