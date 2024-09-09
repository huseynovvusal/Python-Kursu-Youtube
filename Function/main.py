# def istifadecini_qarsila():
#     print("Proqrama xoş gəlmisiniz!")
#     print("Ümid edirik ki, burada vaxtınızı yaxşı keçirəcəksiniz.")
#     print("Gözəl günlər arzulayırıq!")
#
# istifadecini_qarsila()
# istifadecini_qarsila()
# istifadecini_qarsila()
# istifadecini_qarsila()
# istifadecini_qarsila()
# istifadecini_qarsila()
# istifadecini_qarsila()

# def salamla(ad = 'User'):
#     print(f"Salam {ad}!")
#
# salamla('Vusal')
# salamla()

# RETURN
# def f():
#     print("Funksiya - Print")
#
#     return "Funksiya - Return"
#
#     # ...
#     print("Return-dan sonra")

# a = f()

# print(a)

# print(f())

# Example

# def sade(n):
#     for i in range(2,n):
#         if(n % i == 0):
#             print("Murekkeb")
#             return
#
#     print("Sade")
#
# eded = int(input('EDED: '))
#
# sade(eded)

def sade(n):
    for i in range(2,n):
        if(n % i == 0):
            return 'Murekkeb'

    return "Sade"

eded = int(input('EDED: '))

print(sade(eded))