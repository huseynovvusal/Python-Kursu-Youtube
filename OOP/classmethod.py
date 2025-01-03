"""
- Class Method-da ilk parametr class olur. Static Method üçün spesifik bir parametr tələb olunmur.
- Class Method class-ın cari vəziyyətini əldə edə və dəyişə bilir. Static Method isə class haqda heç bir məlumatı bilmir.
"""

class Student:
    student_count = 0
    instances = []

    def __init__(self,name,score):
        self.name = name
        self.score = score
        Student.student_count += 1
        Student.instances.append(self)

    @classmethod
    def get_student_count(cls):
        return f"Student count: {cls.student_count}"

    @classmethod
    def convert(cls, students):
        result = []

        for student in students:
            result.append(cls(student["name"], student["score"]))

        return result




bob = Student('Bob', 93)
alice = Student('Alice', 89)
mark = Student('Mark', 75)

# print(Student.student_count)
# print(Student.instances)

# for instance in Student.instances:
#     print(instance.name)

# print([instance.name for instance in Student.instances])

# print(Student.get_student_count())


data = [
    {
       "name": "Nihad",
        "score": 95
    },
    {
       "name": "Akif",
        "score": 83
    },
    {
       "name": "Nilay",
        "score": 94
    },
]

convertedData = Student.convert(data)

print(*[f"{instance.name}'s score is {instance.score}" for instance in convertedData],sep='\n')




