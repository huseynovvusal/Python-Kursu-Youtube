class CustomRange:
    def __init__(self,start,end,step = 1):
        self.value = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if(self.value >= self.end):
            raise StopIteration

        current = self.value
        self.value += self.step

        return current

numbers = CustomRange(1,5,1)

# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))

# for i in numbers:
#     print(i)

# Generators

def custom_range(start,end,step = 1):
    current = start

    while(current < end):
        yield current
        current += step


numbers2 = custom_range(1,12,3)

# print(next(numbers2))
# print(next(numbers2))
# print(next(numbers2))

for i in numbers2:
    print(i)






