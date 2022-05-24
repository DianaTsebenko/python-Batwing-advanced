from abc import abstractmethod, ABC

# Abstract class
class Hello:
    @abstractmethod
    def say_hello(self):
        raise NotImplementedError('This method was not implemented')

    def say_goodbye(self):
        print('bye')

# Interface
class HelloInterface:
    @abstractmethod
    def say_hello(self):
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def say_goodbye(self):
        raise NotImplementedError('This method was not implemented')

class English(Hello):
    def say_hello(self):
        print('Hello')

class Spanish(Hello):
    def say_hello(self):
        print('Hola')

class Ukrainian(Hello):
    def say_hello(self):
        print('Привіт')

vasyl = Ukrainian()
vasyl.say_hello()