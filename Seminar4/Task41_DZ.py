# Задание 8.
# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

import random

def number(num):
    return [random.randint(1,90) for i in range(num)]   

def min_max(Stroka):   
    return [(Stroka[i]) for i in range(len(Stroka))] # функция для выделения каждого элемента из списка для 
                                                    # нахождения минимального и максимального элемента
n = random.randint(4,21)
Mu_List = number(n) # тут мы значение функции рандомного числа переписываем в будущий список
Mu_List2 = str(Mu_List).replace(',', '') #сдесь мы убираем все запятые и меняем на пробелы как просили
print(Mu_List2)
print(f'Минимальный элемент: [{min(min_max(Mu_List))}], Максимальный элемент: [{max(min_max(Mu_List))}]')

'''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
''' Важно когда делаем рандломную функцию то саму функцию выводить не надо'''
'''Она никогда не совпадет с другой функцией, потому что рандомы то разные'''
'''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''

'''Вариант 2'''
import random

n = random.randrange(5, 20)
My_list = []
for i in range(n):
    My_list .append(random.randint(1, n+80))
lists = str(My_list).replace(',', '')  # меняем запятые разделители на пробелы
print(lists)

print(f'Минимальное число:', min(My_list))
print(f'Максимальное число:', max(My_list))


# ' '.join(map(str(['1','2','3','4'])))

'''Вариант 3'''

a = '11 3 8 89 47 2'
print(a) # 11 3 8 89 47 2
b = list(map(int, a.split(' ')))  # s.split на выходе мы получим набор строк,  ['11', '3', '8', '89', '47', '2']
'''благодаря вот этой части list(map(int получается красиво - [11, 3, 8, 89, 47, 2]'''
print(b) #  [11, 3, 8, 89, 47, 2]
print(f'Минимальное число:', min(b))
print(f'Максимальное число:', max(b))

'''Вариант 4'''

from random import randint
import random
def znachenie(num):
    num = random.randrange(5, 20)
    s = '' # создаем строку для стринга
    for i in range(num):
        s += f'{str(randint(1, 100))} '
        result = list(map(int, s.split(' ')[:-1])) # s.split на выходе мы получим набор строк, 
    return result                                        # [:-1] - это означает все значения , от 0 до последнего
num = []   
number3 = []     
number2 = znachenie(num)                               
print(number2) # вышло значение со всеми запятыми [60, 57, 36, 45, 30, 11, 79, 39, 54, 11, 42, 12, 3, 33]
number3 = str(number2).replace(',', '') # убираем все запятые нпа пробелы
print(number3) # итог [60 57 36 45 30 11 79 39 54 11 42 12 3 33]
print(f'VМинимальное число: {str(min(number2))} + Максимальное число: {str(max(number2))}')
# когда убираешь запятые значения перестают выводиться, поэтому надо отдельно делать просто для строчки если тербуется


"""Функция map
При написании программы очень часто возникает задача, которая состоит в том, 
чтобы применить специальную функцию для всех элементов в последовательности. 
В функциональном программировании она называется отображением от англ. map.

Встроенная в Python функция map – это функция более высокого порядка, 
которая предназначена для выполнения именно такой задачи. 
Она позволяет обрабатывать одну или несколько последовательностей с 
использованием заданной функции. Вот общий формат функции map:

map(функция, последовательности)"""

'''Вариант 5'''
from random import randint
numbers = [] # готовим будущзий спискок
for i in range(20):
    numbers.append(randint(-10,10)) # заполняем список рандомными значениями от -10 до 10
numbers.sort() # возвращает список с отсортированными последовательно данными по возрастанию
numbers = ' '.join(map(str, numbers)) # формируем строковый список из отсортированных рандомных элементов
print(numbers) # -7 -6 -6 -5 -4 0 0 1 3 4 4 5 5 7 7 7 9 9 9 10
print(f'gНаибольшее число:', numbers.split()[-1],) # берем последнее значение с конца списка
print(f'Н:аименьшее число:', numbers.split()[0],) # берем первое значение с начала списка

'''Вариант 6'''
import random

strings = ' '.join([str(random.randint(1, 40)) for i in range(10)])
print(strings) # 6 39 21 39 18 2 19 19 11 19
print(f'max = {max(map(int, strings.split(" ")))} min = {min(map(int, strings.split(" ")))}') # впервые кавычки имеют значение, ошибка если ''
# впервые кавычки имеют значение, ошибка если ''

'''Вариант 7'''

s = ''
for i in range(5):
    s = s + str(randint(1, 10)) + ' '
print(s) # 7 8 2 9 1
my_list = list(map(int, s.split(' ')[:-1]))
print('min = ' + str(min(my_list)))
print('max1 = ' + str(max(my_list)))

'''Вариант 8'''
# def min_max(list):

# n = random.randrange(5,10) #задает рандомное количесво чисел в диапазоне от 2 до 10
# list = []
# for i in range(n):
#     list.append(random.randint(1, n+1))
#     lists  = str(list).replace(',','')
# print(lists)

# srt_list = min_max(list)
# print(min(srt_list)), max(srt_list)

'''Вариант 9'''
string = '49 25 46 7 4 3 8 5'

def convert_to_int(str):
    return [int(x) for x in str.split()]
                 # Функция split сканирует всю строку и разделяет ее в случае нахождения разделителя.
str_list = convert_to_int(string)
print(min(str_list), max(str_list))

l = list(range(1, 15))
random.shuffle(l)
for i in l:
    print(i, end=' ')

print("")

'''Вариант 10'''
# import random
# n = random.randrange(5,10) #задает рандомное количесво чисел в диапазоне от 2 до 10
# list = []
# for i in range(n):
#     list.append(random.randint(1, n+1))
# print(list)

# max = i
# min = i
# for i in list:
#     if i > max:
#         max = i
#     elif i < min:
#         min = i
# print(max)
# print(min)

'''-------------------------------------------------------------------------------------------------------------'''
'''Немного отступления и обучения методам'''

MList = '1, 2, 3, 4'.split(',')
print(MList) # ПОлучается на выходе  ['1', ' 2', ' 3', ' 4']
print(''.join(['1', ' 2', ' 3', ' 4'])) # он принимает тошлько строки  -- ПОлучается на выходе 1 2 3 4
print(''.join(map(str, [1, 2, 3, 4]))) # чтоб не расставлять кавычки можно использовать map -- Олучается на выходе 1234

b = list(map(int, a.split(' ')))  # s.split(' ') на выходе мы получим набор строк,  ['11', '3', '8', '89', '47', '2']
'''благодаря вот этой дополненной части list(map(int,      получается красиво - [11, 3, 8, 89, 47, 2]'''
print(b) #  [11, 3, 8, 89, 47, 2]

number2 = [1,2,3,45,5,6,3]
number3 = str(number2).replace(',', '')
print(number3 ) # [1 2 3 45 5 6 3] убирает запыятые

import random
num = random.randint(1,6)
s = '' # создаем строку для стринга
for i in range(num):
        s += f'{str(randint(1, 100))} '
        result = list(map(int, s.split(' ')[:-1])) # s.split на выходе мы получим набор строк,
print(result)                                      # [:-1] - это означает все значения , от 0 до последнего

'''numbers.sort() # возвращает список с отсортированными последовательно данными по возрастанию'''

strings = ' '.join([str(random.randint(1, 40)) for i in range(10)])
print(strings) # 6 39 21 39 18 2 19 19 11 19
print(f'max = {max(map(int, strings.split(" ")))} min = {min(map(int, strings.split(" ")))}') # впервые кавычки имеют значение, ошибка если ''
# впервые кавычки имеют значение, ошибка если ''
                                     
s = ''
for i in range(5):
    s = s + str(randint(1, 10)) + ' '
print(s) # 7 8 2 9 1
my_list = list(map(int, s.split(' ')[:-1]))
print('min = ' + str(min(my_list)))
print('max1 = ' + str(max(my_list)))                                    