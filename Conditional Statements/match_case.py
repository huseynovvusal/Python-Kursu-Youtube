# Match-Case Statement

"""
hava = input("Hava: ")

if hava == 'yağışlı':
    # Sertin govdesi
    print('Siz yağmurluq geyinəcəksiniz.')

elif hava == 'günəşli':
    print('Siz gün eynəyi taxacaqsınız.')

elif hava == 'qarlı':
    print('Siz isti palto geyinəcəksiniz.')

else:
    print('Adi geyim geyinəcəksiniz.')
"""

hava = 'çiskinli'

match hava:
    case "yağışlı" | "çiskinli":
        print('Siz yağmurluq geyinəcəksiniz.')
    case "günəşli":
        print('Siz gün eynəyi taxacaqsınız.')
    case 'qarlı':
        print('Siz isti palto geyinəcəksiniz.')
    case _:
        print('Adi geyim geyinəcəksiniz.')
























