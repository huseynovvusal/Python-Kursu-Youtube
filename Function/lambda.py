def topla(a,b):
    return a + b

# print(topla(5,3))

t = lambda a,b: a + b

# a = t(2,3)
#
# print(a)

# l = ['Emin Məmmədov', 'Günay Salmanova', 'Cavid Rzayev', 'Elvin Quliyev', 'Leyla Abdullayeva']

# l.sort(key = lambda x : x.split(' ')[1])

# print(l)

l = [
    {'ad' : 'Emin', 'yas' : 20},
    {'ad' : 'Günay', 'yas' : 30},
    {'ad' : 'Cavid', 'yas' : 23},
    {'ad' : 'Elvin', 'yas' : 54},
    {'ad' : 'Leyla', 'yas' : 42}
]

# ADI QAYDA
# def f(x):
#     return x['ad']
#
# l.sort(key=f)

# LAMBDA
# l.sort(key = lambda x : x['ad'])

l.sort(key = lambda x : x['yas'])


print(l)