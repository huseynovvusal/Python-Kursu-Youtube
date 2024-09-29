l = [1,2,3,4,5]

# def f(x):
#     return x % 2 == 1

# new_list = list(filter(f,l))
new_list = list(filter(lambda x : x % 2 == 1,l))

print(new_list)