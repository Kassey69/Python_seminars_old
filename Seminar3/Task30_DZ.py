# Задание 1.
# Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# [2, 3, 4, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


import random

# n = int(input('ВВедите число \n'))
n = random.randrange(4,8) #задает дандомное количесво чисел в диапазоне от 4 до 8
list = []
for i in range(n):
    list.append(random.randint(1, n+1)) # заполняет числа рандомными значениями
    print('',i, end=' ') 
print()
print(list)
# list = [2, 3, 4, 9, 3]
sum = 0
for i in range(len(list)):
    if i % 2 != 0:
        sum += list[i]
    print(f'Индекс [{i}]  число [{list[i]}]  = [{sum}]')
print(f'Сумма элементов на нечетных позициях = [{sum}]')


# list = [2, 3, 4, 9, 3]
# sum = 0
# for i in range(0,5):
#     if i % 2 != 0:
#         sum += list[i]
#     print(f'{i}  {sum}')
