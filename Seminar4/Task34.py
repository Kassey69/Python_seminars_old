# Задача 1.
# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

# Пример:

# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

import random
num = random.randint(2,6)
# num = int(input())
my_dict = {}
for i in range(1, num + 1):
# my_dict[1] = 3*1 + 1
# my_dict[2] = 3*2 + 1
# my_dict[3] = 3*3 + 1
    my_dict[i] = 3*i + 1
print(f' Получичтся: {my_dict}')


'''ниже разбор данных и одна из структур данных подробно разобрано items, update, dict'''
import random
# n = int(input('Введите натуральное число \n'))
n = random.randint(4,7)
my_dict = {} # создаем словарик
for i in range(1, n+1): # тут записано что индекс элементов равен от 1 до n+1 потому что не с 0 а с 1
    my_dict[i] = 3*i + 1 # 3 * 1 + 1 = 4; 3 * 2 + 1 = 7; 3 * 3 + 1 = 10; 3 * 4 + 1 = 13 
print(my_dict)

# 2 вариант
# n = int(input('Введите натуральное число \n'))
# slovar = {}
# slovar = {i: ((3*i) + 1) for i in range(1, n+1)}
# print(slovar)


import random
n = random.randint(4,7)
slovar = {}
slovar = {i: ((3*i) + 1) for i in range(1, n+1)}
print(slovar) # {1: 4, 2: 7, 3: 10, 4: 13, 5: 16}



''' Объяснения'''

my_dict = {}
for i in range(1,2):
    my_dict[i] = 4
print(my_dict.get(1))
print(dir(my_dict)) # показывает море методов

''' посмотрим классы методы в словаре
clear - очистка
copy - скопировать
get - получить
items - вернет список картежей, состоящих из ключей и значений
keys - вернет список ключей
pop - убрать элемент по индексу
setdefault - вставь дефолтное значение
update - обнови, можно добавить
values - получить ключи'''

my_dict.items() 

print(my_dict)  # dict_items([(1, 4), (2, 7), (3, 10), (4, 13)])
my_dict.update({2:7, 3:10, 4:13})
print(my_dict)
for i in my_dict:
    print(my_dict[i]) # так мы получили значение индекса
for key, value in my_dict.items():
    print(f'key = {key} --> value = {value}') # получаем ключи и значения

my_dict.items() 
print(my_dict)
new_dict = dict()
print(new_dict)
l = list(my_dict.items())
print(l) # список картежей [(1, 4), (2, 7), (3, 10), (4, 13)]
print(dict(l)) # делаем из списка картежей словарь {1: 4, 2: 7, 3: 10, 4: 13}
# наполним наш новый словарь
my_dict['key'] = 'value'
print(my_dict) # добавился {1: 4, 2: 7, 3: 10, 4: 13, 'key': 'value'}