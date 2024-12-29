# Pascal Case
class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f"{self.brand} {self.model} is driving...")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping...")

# car1 = Car()
# car1.brand = "BMW"

car1 = Car("BMW", "X5", 2021, "Black")
car2 = Car("Ford", "Mustang", 2022, "Blue")

car1.drive()
car2.drive()
car1.stop()

# print(id(car1))
# print(id(car2))

# print(car1.brand,car1.model, car1.year, car1.color)
