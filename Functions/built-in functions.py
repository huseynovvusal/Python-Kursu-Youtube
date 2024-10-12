from math import floor

t = list((1,2,3,4,5))

d = dict([(str(i) + '.',i) for i in t])

# print(t)
# print(d)

# print(abs(10),abs(-10)) # |x|

# print(bin(10),bin(5))
# print(hex(10),type(hex(1342)))

# print(round(5.5),type(round(5.1)))

# print(chr(97),chr(98))
# print(ord('A'),chr(ord('A')))

# print(floor(5.9),floor(5.1))

# print(divmod(5,2))

# print(pow(5,3,3))

# s = input("S: ")
# print(eval(s))

l = ['A','B','C','D']

# print(list(enumerate(l)))

# for i in range(len(l)):
#     simvol = l[i]

# for i,simvol in enumerate(l):
#     print(i,simvol)

# a,b = [0, 'A']
#
# print(a,b)

# print(oct(100),oct(11))

l = [1,2,3,4]
# print(sum(l))

print(min([10,5,16]), min(5,3,10), min(l))
print(max([10,5,16]), max(5,3,10), max(l))