# i = 1
#
# while (i <= 5):
#     print(f"{i}. Python")
#
#     i += 1
#
# print("SON")

# Python i = 2 -> Python i = 3 -> Python i = 4 -> Python i = 5 -> Python i = 6


# Proqram 1
# n = int(input("n: ")) # 4
#
# i = 1
# cem = 0
#
# while(i <= n):
#     cem += i
#
#     i += 1
#
# print(cem)

# cem = 1 i = 2
# cem = 3 i = 3
# cem = 6 i = 4
# cem = 10 i = 5

# Proqram 2
# s = input("S: ")

# 0,1,2,3,4,5
# p y t h o n -> len(s) = 6

# i = 0
#
# while(i < len(s)):
#     print(s[i])
#
#     i += 1

# Program 3

# * -> 1
# ** -> 2
# *** -> 3
# **** -> 4
# ...

# h = int(input("H: "))
# setir_no = 1
#
# while(setir_no <= h):
#     sutun_no = 1
#
#     # print('setir:',setir_no)
#
#     # while(sutun_no <= setir_no):
#     #     print("*",end='')
#     #
#     #     sutun_no += 1
#     #
#     # print()
#
#     print('*' * setir_no)
#
#     setir_no += 1

# Proqram 4

# n! = 1 * 2 * 3 * ... * (n - 1) * n
# f = 0 ->
# f = 1 -> 1 -> 2 -> 6 ->
# 0! = 1

# n = int(input("N: "))
# i = 1
# f = 1
#
# while(i <= n):
#     f = f * i
#
#     i += 1
#
# print(f)

# Proqram 5

# 10 -> 1,2,5,10
# 5 -> 1,5

# n -> 1,2,3,4,5,...,n

n = int(input("N: "))

bolen_sayi = 0
i = 1

while(i <= n):
    if(n % i == 0): bolen_sayi += 1

    i += 1

# print(bolen_sayi)

if(bolen_sayi == 1):
    print('Ne sade ne murekkeb')
else:
    print('Sade' if bolen_sayi == 2 else 'Murekkeb')