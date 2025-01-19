"""
"r" - Read - Defolt dəyər. Oxumaq üçün faylı açır, əgər fayl mövcud deyilsə, xəta baş verir
"a" - Append - Əlavə etmək üçün faylı açır, mövcud olmadığı təqdirdə faylı yaradır
"w" - Write - Yazmaq üçün faylı açır, mövcud deyilsə faylı yaradır
"x" - Create - Göstərilən faylı yaradır, fayl varsa xətanı qaytarır
"""

import os

# Read
# f = open("file.txt", "r")

# content = f.read(10)
# print(content)

# print(f.readline())
# print(f.readline())

# for line in f:
#     print(line)

# f.close()

# try:
#     for line in f:
#         print(line)
# except:
#     print('There is no such file')
# finally:
#     f.close()


# Append
# f = open("file.txt", "a")
#
# f.write("11) New Line\n")
#
# f.close()

# Append
# f = open("langs.txt", "w")
#
# f.write("Python\nKotlin\nC++\nTypeScript\nC#")
#
# f.close()

# Create
# if(not os.path.exists('test.txt')):
#     f = open("test.txt",'x')

# Delete
# if(os.path.exists('test.txt')):
#     os.remove('test.txt')
# else:
#     print("There is no such file to delete")

with open('langs.txt','w') as f:
    f.write('JavaScript')

with open('langs.txt','r') as f:
    content = f.read()

    print(content)









