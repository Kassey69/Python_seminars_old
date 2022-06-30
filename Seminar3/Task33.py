# это просто примеры, не задачи

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
a.upper() # если не присвоить значение то и никуда не сохранить и буквы не станут большими
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


'''еще вариант рандома списка'''
import random
import string
def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    print("Alphanum Random string of length", length, "is:", rand_string)
generate_alphanum_random_string(8)

'''еще вариант рандома списка'''
# 3 вариант
import random
import string
def generate_alphanum_random_string(length):
    length = random.randint(7,9)
    for i in range(length):
        # Чтобы сгенерировать буквенно-цифровую случайную строку в Python, 
        # используйте константы string.ascii_letters и string.digits, чтобы получить комбинации букв и цифр.-
        letters_and_digits = string.ascii_letters + string.digits
        rand_string = ''.join(random.sample(letters_and_digits, length))
        # print("Рандомная строка", length, "символов:", rand_string)
    return rand_string
strika2 = ''
print("Рандомная строка", generate_alphanum_random_string(strika2))
stroka1 = 'sikj529LFnfe'
print(f'Сравниваем с первой строкой:  {stroka1}')
result = 0
for i in stroka1: # раскладываем каждый индекс элемента строки
    for x in generate_alphanum_random_string(strika2): #сравниваем каждый индекс элемента со строкой2
        if x == i: # если находятся одинаоквые элементы при сравнени индексов то
            result += 1 # ведем счет всех повторений элементов
print (f'Символы повторяющиеся {result} раз(а)')