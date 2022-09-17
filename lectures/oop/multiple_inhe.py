class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_person_info(self):
        print(f'My name is {self.first_name} {self.last_name} and I am {self.age}')

class Student:
    def __init__(self, student_id, scores):
        self.scores = scores
        self.student_id = student_id

    def print_scores(self):
        print(self.scores)

    def student_id(self):
        print(self.student_id)

class Resident(Person, Student):
    def __init__(self, resident_id, first_name, last_name, age, student_id, scores):
        Person.__init__(self, first_name, last_name, age)
        Student.__init__(self, student_id, scores)
        self.resident_id = resident_id

    def get_resident_id(self):
        print(self.resident_id)

resident = Resident(123, 'Mike', 'Resident', 28, 245, ['A', 'A', 'A'])

resident.print_scores()
resident.print_person_info()
resident.get_resident_id()