# Задача 3.
# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элемента.

# Пример:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


My_list = [1.1, 1.2, 3.1, 5, 10.01]
def max_min(My_list):
    return [round(i - int(i),2) for i in My_list if round(i - int(i),2) != 0] # очень важно. 0 исключаем из уровнения
print(max_min(My_list))
print((max(max_min(My_list))))
print(min(max_min(My_list)))
print((max(max_min(My_list))) - (min(max_min(My_list))))


# 2 варинат решения

import random

# задает рандомное количесво чисел в диапазоне от 2 до 10
# n = random.randrange(2, 10)
# list = []
# for i in range(n):
#     list.append(round(random.uniform(0, 10), 2))
# print(list)
# # list = [1.1, 1.2, 3.1, 5, 10.01]
# # https://all-python.ru/osnovy/sluchajnoe-chislo.html - Реализации случайных чисел в Python
# list2 = []
# for i in list:
#     list2.append(round(i - int(i), 2))  # избавляемся от целых чисел
# print(list2)
# # делаем это чтоб максимум был без целых, а в минимумах это не нужно
# max = round(i - int(i), 2)
# min = i
# result = 0
# for i in list2:
#     if i > max:
#         max = i
#     elif i < min:
#         min = i
# result = round((max - min), 2)
# print(f'Максимальная дробная часть: {max}')
# print(f'Минимальное дробная часть: {min}')
# print(f'Разница: {max} - {min} = {result}')


'''3 вариант, упрощенный алгоритм'''
import random

n = random.randrange(2, 20)
list = []
for i in range(n):
    list.append(round(random.uniform(0, 10), 2))
print(list)
# list = [1.1, 1.2, 3.1, 5, 10.01]
My_list = [round((i - int(i)),2) for i in list if round((i - int(i)),2) != 0]
# # i*100) % 100 - элемент списка умнодаем на 100, откидываем дробную часть и
# # получаем остаток от деления на 100, конкрентно дробную часть
# # и проверяем чтоб она была больше нуля и ее записываем +  приводим к int значению
# # в пайтон если мы приводим числа к int то лишний хвостик отбрасываем с дробью
# и в конце за счет min и max , берем минимальное и максималдьное и выситаемся, вычислять их не нужно
# в пайтоне минимум и максимум автоматом считается, но есть особые моменты
print(f'Убрали целое значение: {(My_list)}')
print(f'Максимальная дробная часть: [{max(My_list)}]')
print(f'Минимальное дробная часть: [{min(My_list)}]')
print(f'Разница: [{max(My_list)}] - [{min(My_list)}] = [{round((max(My_list) - min(My_list)),2)}]')
print(f'Итого: [{round((max(My_list) - min(My_list)),2)}]')


'''4 вариант, упрощенный алгоритм'''
mu_list = [1.1, 1.2, 3.1, 5, 10.01]
def delim_bez_ostatka(mu_list):
    return [int((i*100) % 100) for i in mu_list if int((i*100) % 100) > 0]
print(delim_bez_ostatka(mu_list))
print(max(delim_bez_ostatka(mu_list)) - min(delim_bez_ostatka(mu_list)))
    # int((i*100) % 100) - таким образом ьы конкретно отбрасываем дробную часть

'''5 вариант, упрощенный алгоритм'''
mu_list = [1.1, 1.2, 3.1, 5, 10.01]
def delim_bez_ostatka(mu_list):
    return [round((i % 1),2) for i in mu_list if round((i % 1),2) > 0]
print(delim_bez_ostatka(mu_list))
print(max(delim_bez_ostatka(mu_list)) - min(delim_bez_ostatka(mu_list)))