# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений подстроки в строку.

# Пример:

# "Проснувшись однажды утром после беспокойного сна."
# "Проснувшись однажды утром"
# Количество вхождений - 1

# первый вариант
# text1 = input(f'Введите полную фразу\n')
# text2 = input(f'Введите отрезок\n')
# text = text1.count(text2) 
# print(text)

# Метод count() возвращает количество раз, когда указанный элемент появляется в списке.
# Источник: https://pythonstart.ru/list/count-python

my_string = "Проснувшись однажды утром после беспокойного сна"
start = -1
count = 0

while True:
    start = my_string.find("Проснувшись однажды утром", start+1)
    if start == -1:
        break
    count += 1
    # Метод find() помогает найти индекс первого совпадения подстроки в данной строке. 
    # Возвращает -1, если подстрока не была найдена.
print("Количество вхождений символа в строку: ", count )


'''2 вариант условия задачи!!!!!!!!!!!!!!!!!!'''

# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другую строку.

# 1 вариант решения
stroka1 = 'sikjnfe' # создаем 1 строку
stroka2 = '234jfk' # создаем 2 строку
count = 0
for i in stroka1:
        if stroka2.find(i) >= 0: # find ищем элементы строки 2 в строке 1 (i выступает как элементы символов строки)
            count += 1
print(count)

# Как сгенерировать случайную строку в Python
# https://dev-gang.ru/article/kak-sgenerirovat-sluczainuu-stroku-v-python-wwnl77lvl4/

import random
import string
def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    print("Alphanum Random string of length", length, "is:", rand_string)
generate_alphanum_random_string(8)


# определить есть ли такая буква в строке
stroka = 'sdf33333sdfs'
count = 0
start = -1
while True:
    start = stroka.find("d", start+1)
    if start == -1:
        break
    count += 1
print(f' символ : {count}')


# 2 вариант решения
print(len(set(list('rgs5tt4')) & set(list('kbkk5r')))) # мы сравниваем две строки и находим количество одинаковых 
                                                       # символов в этих мнрожествах
                                                       
# print(len(set(list(input('Введите 1 строчку \n'))) & set(list(input('Введите 2 строчку\n')))))

# есть строка, нужно получить другую строку с только уникальными значениями
# для этого надо преобразовать нашу строку во множества
l = list('sjdfwefjwfwesjdfwefjwfwesjdfwefjwfwe')
print(l) 
l = set('sjdfwefjwfwesjdfwefjwfwesjdfwefjwfwe') #реобразовать нашу строку во множества 
l = set(l) # либо так !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print(l) # {'j', 'e', 's', 'd', 'w', 'f'}
# создадим еще одно множество
n = set(list('wefw23zds'))
''' теперь посмотрим их пересечение l & n
print(l & n) # остаются только уникальные элементы в этом случае из двух множеств {'w', 'd', 'f', 'e', 's'}
# или например являются общими l| n
print(l | n) # общие значения {'3', 'w', 'd', 'f', 'e', '2', 'j', 's', 'z'}
print(l - n ) # ищет чем разные множества'''

"""с помощью set можно создать коллекцию с уникальными значениями"""
# 2 вариант
stroka1 = 'sikjnfe'
strika2 = '234jfk'
result = 0
for i in stroka1: # раскладываем каждый индекс элемента строки
    for x in strika2: #сравниваем каждый индекс элемента со строкой2
        if x == i: # если находятся одинаоквые элементы при сравнени индексов то
            result += 1 # ведем счет всех повторений элементов
print (f'Символы повторяющиеся {result} раз(а)')

''' Строки. Функции и методы строк - https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html'''

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

# еще вариант 4 - их пересечение  & 

import random

first_string = 'wefwerg'
second_string = 'ergervsd'

stroka1 = set(first_string)
stroka2 = set(second_string)

print(stroka1)
print(stroka2)

result = (stroka1 & stroka2 )
print(len(result))

# 5 вариант

first_string = 'wefw5656g'
second_string = 'ergervsd'
result = 0

for i in range(0, len(first_string)):
    for j in range(0, len(second_string)):
        if first_string[i] == second_string[j]:
            result +=1
print(result)

# 6 вариант с функцией zip
from itertools import zip_longest
a = 'fwef33fsd'
b= 'fqwdffas'
z = zip(a, b)
print(next((z))) # next поочереди объединяет индесыы обоих элементов ('f', 'f')
print(next((z))) # ('w', 'q')
print(next((z))) # ('e', 'w')
print(next((z))) # ('f', 'd')
print(next((z))) # ('3', 'f')
print(next((z))) # ('3', 'f')
print(next((z))) # 'f', 'a')
print(next((z))) # ('s', 's')
# print(next((z))) # бцудет ошибкой, потому что с одной из сторон закончились эдементы для объединения

# вариант 7 с фуккцией zip_longest
from itertools import zip_longest
a = 'fwef33fsd'

result = {} # картэж
for key, value in zip(a, range(len(a))): # zip сшивает две последовательностия и возвращает их по очереди
    # когда мы итерируемся мы получаем по очереди каждывй элемент, а олн соберает два элемента
    print(key, value) #  ключом будет буква, а значение индекс этой буквы e 2  f 3  3 4  3 5  f 6  s 7  d 8
    result[key] = value
print(result) # {'f': 6, 'w': 1, 'e': 2, '3': 5, 's': 7, 'd': 8} result это словарь







