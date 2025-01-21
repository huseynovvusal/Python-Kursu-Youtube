"""
Decorator(s) - digər funksiyaların funksionallığını dəyişdirən funksiyalar.
"""

# def decorator(func):
#     def wrapper():
#         print("Start")
#         func()
#         print("End")
#
#     return wrapper
#
# @decorator
# def ordinary():
#     print("Ordinary Function")
#
# ordinary()

# import time
#
# def timer(func):
#     def wrapper():
#         t1 = time.time()
#         print("Start")
#         func()
#         print("End")
#         t2 = time.time()
#
#         res = round((t2 - t1) * 1000)
#
#         print(f"{func.__name__} executed in {res} milliseconds")
#
#     return wrapper
#
# @timer
# def task():
#     # i = 0
#     #
#     # while(i < 100000000):
#     #     i += 1
#
#     time.sleep(3)
# task()


# f(1,2,3,"salam", x = 5, y = 3)

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        res = func(*args, **kwargs)
        print("After")

        return res

    return wrapper

@decorator
def topla(x,y):
    return x + y

print(topla(5, y = 5))








