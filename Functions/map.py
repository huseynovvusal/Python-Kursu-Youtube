l = ['1','2','3','4','5']

# for i in range(len(l)):
#     l[i] = int(l[i])
#
# print(type(l[0]))

# new_list = list(map(int,l))
#
# print(new_list,type(new_list[0]))


l = [1,2,3,4,5]

# def f(x):
#     return x * 2

# l = list(map(f,l))
l = list(map(lambda x : x * 2,l))

print(l)

