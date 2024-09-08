# BREAK

# i = 1
#
# while(i <= 10):
#     print(i)
#
#     i += 1
#
#     if(i == 5): break

# for i in range(1,11):
#     print(i)
#
#     if(i == 4): break
#
#     print("after break")

# CONTINUE

# i = 1
#
# while(i <= 10):
#     if(i == 5):
#         i += 1
#         continue
#
#     print(i)
#
#     i += 1

# for i in range(1,11):
#     if(i % 2 == 0): continue
#
#     print(i)

# WHILE-ELSE
# i = 1
#
# while(i <= 10):
#     print(i)
#
#     if(i == 5): break
#
#     i += 1
# else:
#     print("ELSE")


# FOR-ELSE

# for i in range(1,6):
#     print(i)
#     if(i == 3): break
# else:
#     print("ELSE")

# EXAMPLE

n = int(input("N: "))

for i in range(2,n):
    if(n % i == 0):
        print("MUREKKEB")
        break
else:
    print("SADE")

