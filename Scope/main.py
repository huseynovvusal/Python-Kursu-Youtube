"""
Scope - Python-da scope (görünüş sahəsi), dəyişənlərin və ya funksiyaların mövcud olduğu və əlçatan
        olduğu kod hissəsini ifadə edir.

Local: Funksiya daxilində yaradılan dəyişənlər, yalnız həmin funksiyada mövcuddur.
Enclosing: Funksiyanın içindəki daxili funksiyalar üçün xarici funksiyanın scope-u.
Global: Proqramın hər yerində əlçatan olan dəyişənlər.
Built-in: Python-un daxili funksiyaları və adları.

Qeyd: Python-da dəyişənlər LEGB ardıcıllığı ilə axtarılır.
"""

x = 5 # Global variable

# def f():
#     x = 10 # Local variable
#     print(x)

# def outer():
#     y = 20 # Enclosing Variable
#
#     def inner():
#         nonlocal y
#         y += 1
#         print('Inner:',y)
#
#     inner()
#     print('Outer:',y)

# Call the function
# f()
# print('Global:',y)

# outer()


x = 5 # Global variable

def f():
    def g():
        global x
        x += 10
        print('g():',x)


    g()

# Call the function
f()
print('Global:',x)

# Built-in
# print(max(10,15,20))




