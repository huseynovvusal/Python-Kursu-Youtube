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

import time

def timer(func):
    def wrapper():
        t1 = time.time()
        print("Start")
        func()
        print("End")
        t2 = time.time()

        res = round((t2 - t1) * 1000)

        print(f"{func.__name__} executed in {res} milliseconds")

    return wrapper

@timer
def task():
    # i = 0
    #
    # while(i < 100000000):
    #     i += 1

    time.sleep(3)
task()
