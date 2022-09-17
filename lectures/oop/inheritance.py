class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_person_info(self):
        print(f'My name is {self.first_name} {self.last_name} and I am {self.age}')

class Student(Person):
    def __init__(self, first_name, last_name, age, scores):
        super().__init__(first_name, last_name, age)
        self.scores = scores

    def print_scores(self):
        print(self.scores)

mike = Student('Mike', 'Torss', 28, ['A', 'C-', 'B'])

mike.print_person_info()
mike.print_scores()
print(issubclass(Student, Person))