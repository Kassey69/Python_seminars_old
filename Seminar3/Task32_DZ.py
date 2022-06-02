# Задача 3.
# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элемента.

# Пример:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

n = random.randrange(2,10) #задает рандомное количесво чисел в диапазоне от 2 до 10
list = []
for i in range(n):
    list.append(round(random.uniform(0, 10),2))
print(list)
    #https://all-python.ru/osnovy/sluchajnoe-chislo.html - Реализации случайных чисел в Python
list2 = []
for i in list:
    list2.append(round(i - int(i), 2)) # избавляемся от целых чисел
print(list2)
max = round(i - int(i), 2)  # делаем это чтоб максимум был без целых, а в минимумах это не нужно
min = i
result = 0
for i in list2:
    if i > max:
        max = i      
    elif i < min:
        min = i
result = round((max - min),2)
print (f'Максимальная дробная часть: {max}')
print (f'Минимальное дробная часть: {min}')
print(f'Разница: {max} - {min} = {result}')
    
