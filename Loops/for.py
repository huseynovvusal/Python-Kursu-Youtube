# LIST

# l = [1,2,3]
#
# for a in l:
#     print(a)

# SET

# l = {1,2,3}
#
# for a in l:
#     print(a)

# TUPLE

# l = (1,2,3)
#
# for a in l:
#     print(a)

# DICT

# d = {
#     '(1)' : 'bir',
#     '(2)' : 'iki',
#     '(3)' : "üç"
# }
#
# for a in d:
#     print(a,d[a])

# STRING

# s = "Python"
#
# for a in s:
#     print(a)

# RANGE
# [a;b)
# print(list(range(1,11)))
# print(list(range(1,11,2)))

# for i in range(1,10):
#     print(i)

# l = ['a','b','c','d','e','f']
#
# for i in range(0,len(l)):
#     print(i,l[i])

# While ve For

# n = int(input('N: '))
#
# for i in range(n):
#     print(i,'salam')

s = 'Python is a programming language.'

# for i in range(0,10,4):
#     print(i,s[i])

# for simvol in s[0:10:4]:
#     print(simvol)

# n! = 1 * 2 * ... * (n - 1) * n

# davam = True
#
# while(davam):
#     n = int(input("N: "))
#
#     f = 1
#
#     for i in range(1, n + 1):
#         f *= i
#
#     print(f)
#
#     sorgu = input('Davam etmek isteyirsinizmi? (Yes/No): ')
#
#     if(sorgu.lower() == 'no'):
#         davam = False

n = int(input('N: '))

sade = True

# 1,2,3,4,5...,9,10

for i in range(2,n):
    if(n % i == 0):
        sade = False

print('Sade' if sade else 'Murekkeb')