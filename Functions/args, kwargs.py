# def topla(*a):
#     netice = 0
#
#     for eded in a:
#         netice += eded
#
#     return netice
#
# cem = topla(2,5,6,10,15)
#
# print(cem)

# topla(2,5,6,10)

# def f(**kwargs):
#     print(kwargs)
#
# f(a=5,b = 10, c = 5)

def f(x,y,*args,**kwargs):
    print(x,y)
    print(args)
    print(kwargs)

f(1,2,3,a=5,b = 10, c = 5)