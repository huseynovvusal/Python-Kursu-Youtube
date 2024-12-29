# Dunder or Magic Methods

class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.arr = ['A','B','C']

    def is_died(self):
        return self.health == 0

    def damage(self, value):
        self.health = max(0,self.health - value)

    def __str__(self):
        return f"{self.name} with {self.health}HP"

    def __len__(self):
        return self.health

    def __getitem__(self, item):
        # print("ITEM:",item)
        return self.arr[item]

    def __eq__(self, other):
        return self.health == other.health

    def __lt__(self, other):
        return self.health < other.health

    def __add__(self, other):
        return self.health + other.health

    def __sub__(self, other):
        return self.health - other.health

    def __mul__(self, other):
        pass



alpha = Character(name="Alpha")
beta = Character(name="Beta")

# print(len(alpha))
# print(beta)

# print(alpha[1])

# print(alpha == beta)

# alpha.damage(75)

# print(alpha == beta)

alpha.damage(75)
# print(alpha < beta)

# print(alpha + beta)