# Задача 2.
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Если остается 1 элемент без пары - умножаем его самого на себя.

# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import math
import random

n = random.randrange(2,10) #задает дандомное количесво чисел в диапазоне от 4 до 8
list = []
for i in range(n):
    list.append(random.randint(1, n+1)) # заполняет числа рандомными значениями
print(list)
#list = [2, 3, 4, 5, 6]
proizv = 0
list2 = [] # создаем 2 список для произведение пар чисел из 1 списка
for i in range(math.ceil(len(list)/2)): # https://docs.python.org/3/library/math.html
                                # math.ceil(x) Возвращает потолок x, наименьшее целое число, большее или равное x
    proizv = list[i] * list[-1-i]
    print(f'{list[i]} * {list[-1-i]} = {proizv}')
    list2.append(proizv)
print(list2)


