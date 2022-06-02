# Задание 8.
# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

import random

n = random.randrange(5, 20)
list = []
for i in range(n):
    list.append(random.randint(1, n+80))
lists = str(list).replace(',', '')  # меняем запятые разделители на пробелы
print(lists)

print(f'Минимальное число:', min(list))
print(f'Максимальное число:', max(list))


# def min_max(list):

# n = random.randrange(5,10) #задает рандомное количесво чисел в диапазоне от 2 до 10
# list = []
# for i in range(n):
#     list.append(random.randint(1, n+1))
#     lists  = str(list).replace(',','')
# print(lists)

# srt_list = min_max(list)
# print(min(srt_list)), max(srt_list)


# string = '49 25 46 7 4 3 8 5'

# def convert_to_int(str):
#     return [int(x) for x in str.split()]
#                  # Функция split сканирует всю строку и разделяет ее в случае нахождения разделителя.
# str_list = convert_to_int(string)
# print(min(str_list), max(str_list))

# l = list(range(1, 15))
# random.shuffle(l)
# for i in l:
#     print(i, end=' ')


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
