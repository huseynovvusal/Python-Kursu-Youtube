"""
Exception - Proqramın icrası zamanı baş verən səhv (error) və ya gözlənilməz hadisədir.
Exception Handling - Səhvləri idarə etmək və proqramın dayanmasının qarşısını almaq üçün istifadə olunan üsuldur.
"""

# print(x)
# n = int(input("N: "))

# try:
#     # print(x)
#     n = int(input("N: "))
#     print(N)
# except ValueError:
#     print("Please, enter an integer")
# except NameError:
#     print("There is no such variable")
#

# a = [0,1,3,5,10]
# x = 20
#
# for i in a:
#     try:
#         print(x / i)
#     except ZeroDivisionError:
#         continue # pass


# try:
#     print(z)
# except NameError as e:
#     print(e)


# a = [0,1,3,5,10]
# x = 20
#
# for i in a:
#     try:
#         print(x / i)
#         print(t)
#     except ZeroDivisionError as e:
#         # continue # pass
#         print(e)
#     except:
#         print('An unknown error occurred')


# a = [1]
# x = 20
#
# for i in a:
#     try:
#         print(x / i)
#     except ZeroDivisionError as e:
#         # continue # pass
#         print(e)
#     else:
#         print("Success")
#     finally:
#         print("End")




# x = '10'
#
# if type(x) is not int:
#     raise TypeError('Only integers are acceptable')





a = [1]
x = 20

for i in a:
    try:
        print(x / i)

        raise Exception('Unknown error')
    except ZeroDivisionError as e:
        # continue # pass
        print(e)
    except:
        pass
    else:
        print("Success")
    finally:
        print("End")








