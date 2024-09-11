# List Comprehension

# l = list()
#
# for i in range(1,11):
#     l.append(i)
#
# print(l)

# l = list(range(1,11))
# print(l)

# l = [i for i in range(1,11)]
# print('LIST:',l)

# EXAMPLE
ededler = [4,30,23,36,87,59,102,114,56,78,26]

# yeni_list = [i for i in ededler if i % 2 == 0]
yeni_list = [i for i in ededler if i % 2]
print(yeni_list)

# print([i + 10 for i in ededler])

