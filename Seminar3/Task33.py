import random
import string


def ar(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters.upper()) for i in range(length)) # нашел куда вставить - letters.upper()
    print("Random string of length", length, "is:", rand_string)
    return rand_string
ar(8)
# a = input('Введите строку \n')
a = 'sdf'
a.upper() # если не присвоить значение то и никуда не созранит и буквы не станут большими
print(a)
a = a.upper() # если присвоить значение то она созранит с большими буквами
print(a)

sp = ['бла-бла', 'гру']
sp.remove('гру') #удаляет выбранный в скобках элемент
print(sp)

sp = ['бла-бла', 'гру', '1','2','3','4']
sp.sort() # отсортировывает
print(sp)
print(sorted(sp)) 