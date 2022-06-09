# Задание 8.
# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

# import random

# n = random.randrange(5, 20)
# list = []
# for i in range(n):
#     list.append(random.randint(1, n+80))
# lists = str(list).replace(',', '')  # меняем запятые разделители на пробелы
# print(lists)

# print(f'Минимальное число:', min(list))
# print(f'Максимальное число:', max(list))


# ' '.join(map(str(['1','2','3','4'])))


# a = '11 3 8 89 47 2'
# b = list(map(int, a.split(' ')))
# print(f'Минимальное число:', min(b))
# print(f'Максимальное число:', max(b))



# from random import randint
# import random
# n = random.randrange(5, 20)
# s = ''
# for i in range(n):
#     s += f'{str(randint(1, 100))} '
#     result = list(map(int, s.split(' ')[:-1])) # s.split на выходе мы получим набор строк, 
#                                                # [:-1] - это означает все значения , от 0 до последнего
# print(s)
# print(result)
# print(f'Минимальное число:', str(min(result)))
# print(f'Максимальное число:', str(max(result)))

"""Функция map
При написании программы очень часто возникает задача, которая состоит в том, 
чтобы применить специальную функцию для всех элементов в последовательности. 
В функциональном программировании она называется отображением от англ. map.

Встроенная в Python функция map – это функция более высокого порядка, 
которая предназначена для выполнения именно такой задачи. 
Она позволяет обрабатывать одну или несколько последовательностей с 
использованием заданной функции. Вот общий формат функции map:

map(функция, последовательности)"""


# from random import randint
# number = [] # готовим будущзий спискок
# for i in range(20):
#     number.append(randint(-10,10)) # заполняем список рандомными значениями от -10 до 10
# number.sort() # возвращает список с отсортированными последовательно данными по возрастанию
# number = ' '.join(map(str, number)) # формируем строковый список из отсортированных рандомных элементов
# print(number)
# print(f'Наибольшее число:', number.split()[-1],) # берем последнее значение с конца списка
# print(f'Н:аименьшее число:', number.split()[0],) # берем первое значение с начала списка


import random

strings = ' '.join([str(random.randint(1, 40)) for i in range(10)])
print(strings)
print(f'max = {max(map(int, strings.split(" ")))} min = {min(map(int, strings.split(" ")))}') # впервые кавычки имеют значение, ошибка если ''
# впервые кавычки имеют значение, ошибка если ''


# def min_max(list):

# n = random.randrange(5,10) #задает рандомное количесво чисел в диапазоне от 2 до 10
# list = []
# for i in range(n):
#     list.append(random.randint(1, n+1))
#     lists  = str(list).replace(',','')
# print(lists)

# srt_list = min_max(list)
# print(min(srt_list)), max(srt_list)


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
