class Person:
    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age

    def greet(self):
        print(f"Salam!")

    def show_info(self):
        print("Full Name:", self.full_name)
        print("Age:", self.age)

# +grade
class Student(Person):
    def __init__(self, full_name, age,grade):
        super().__init__(full_name, age)
        self.grade = grade

    def say_grade(self):
        super().greet()
        print(f"{self.full_name}'s grade is {self.grade}")

    def show_info(self):
        super().show_info()
        print("Grade:", self.grade)

student1 = Student('John Doe', 13, 7)

person1 = Person("Nazim Ramazanli", 30)

# print(student1.grade)

# student1.say_grade()

# student1.greet()
# print(student1.full_name, student1.age)

# Student Info
# student1.show_info()

# Person Info
person1.show_info()