adlar = ['Ilqar','Namiq','Nazim','Vuqar','Malik']
yaslar = [20,16,25,33,27]

# insanlar = []
#
# for i in range(len(adlar)):
#     insanlar.append((adlar[i],yaslar[i]))

# print(insanlar)
# print(dict(insanlar))

insanlar = dict(zip(adlar,yaslar))

print(insanlar)