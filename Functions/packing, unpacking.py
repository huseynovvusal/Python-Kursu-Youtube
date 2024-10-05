# def f(*args):
#     print(args)
#
# l = [1,2,3]
#
# f(*l,4,5)

def f(**kwargs):
    print(kwargs)

d = {
"ad" : "Vusal",
"soyad" : 'Huseynov'
}

f(**d)