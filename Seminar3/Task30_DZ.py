# Задание 1.
# Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# [2, 3, 4, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import random
# My_list = []
# def rand(n):
#     n = random.randint(4, 5)
#     return [(random.randint(1,9)) for i in range(n)]
# print(rand(My_list))
# My_list = [2, 3, 4, 9, 3]

import random
# My_list = []
n = random.randint(4, 5)
My_list = [(random.randint(1,9)) for i in range(n)]
def sums(Spisok):
    sim = 0
    return [sim + (Spisok[i]) for i in range(len(Spisok)) if i % 2 != 0]
print(f' Элементы списка: {(My_list)};\n',f'Нечетный index: {(sums(My_list))};\n', f'Сумма:[{(sum(sums(My_list)))}]')


'''Вариант 2'''

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

'''Третий вариант решения'''
# list = [2, 3, 4, 9, 3]
# print(sum(list[1::2])) # идем от первого элемента это 3(интекс с 0) и берем каждый второй, все складываем



# listss = [2, 3, 4, 9, 3]
# summ = 0
# # for i in range(len(list)):
# #     if i % 2 != 0:
# #         sum += list[i]
# My_lists = [summ + (listss[i]) for i in range(len(listss)) if i % 2 != 0]
# print(My_lists)      
# print(sum(My_lists))



