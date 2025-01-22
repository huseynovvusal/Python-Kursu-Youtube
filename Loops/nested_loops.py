# for i in range(1,5):
#     # i = 2
#     for j in range(1,4):
#         print(i,j)
#     # ...

# for i in range(3):
#     # i = 0
#     for j in range(4):
#         # j = 1
#         for k in range(5):
#             print(i,j,k)
#
# i = 0
#
# while(i < 5):
#     for j in range(3):
#         print(i,j)
#
#     i += 1

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(f"matrix[{i}][{j}] =",matrix[i][j])










