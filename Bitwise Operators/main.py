# Bitwise Operators

"""
& (AND) - Hər iki bit 1 olduğu halda, bit dəyərini 1 edir.
| (OR) - İki bitdən biri 1 olduğu halda, bit dəyərini 1 edir.
^ (XOR) - Yalnız iki bitdən biri 1 olduğu halda, bit dəyərini 1 edir.
~ (NOT) - Bütün bitləri əksinə çevirir (0 → 1, 1 → 0).
<< (Left Shift) - Sağdan sıfır əlavə edərək bitləri sola sürüşdürür, sol bitlər kənara düşür.
>> (Right Shift) - Soldan ən sol biti (işarəni) kopyalayaraq sağa sürüşdürür, sağ bitlər kənara düşür.
"""
# AND

# 101
# 110
# 100 = 4
# print(5 & 6)

# 0101
# 1000
# 0000 = 0
# print(5 & 8)


# OR

# 101
# 110
# 111 = 7
# print(5 | 6)


# 0101
# 1000
# 1101 = 13
# print(5 | 8)


# XOR

# 101
# 110
# 011 = 3
# print(5 ^ 6)

# 0101
# 1000
# 1101 = 13
# print(5 ^ 8)

# NOT

# 0101 = 5
# 1010 = -(0110)= -6
# print(~5)

# Left Shift
# |101-|
# |1010|
# print(5 << 1)

# Right Shift
# |101|
# |10| = 2
# print(5 >> 1)

# 1010
# 10 = 2
# print(10 >> 2)

n = 6

for i in range(4):
    print(1 & (n >> i))

# 6 = 110
# 3 = 11
# 1 = 001
# 0 = 000

# 011
# 001
# 001 = 1



