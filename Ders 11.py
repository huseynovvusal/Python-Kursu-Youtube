# Tuple

programlasdirma_dilleri = ("Python","Java","C++","Javascript","TypeScript","TypeScript")

# print(type(programlasdirma_dilleri))

# print(programlasdirma_dilleri[1:3])

# Error
# programlasdirma_dilleri[0] = "C#"

# print(programlasdirma_dilleri)

# t  = tuple()
#
# print(t)


# t = "Python",
#
# print(type(t))

t = (1,2,3)

# print(t.index(2))
# print(t.count(2))

t = list(t)

t.append(4)

t = tuple(t)

print(t,type(t))