# Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр(отсекаем минус, считаем все в плюс).

# Пример:

# 67,82 -> 23
# 0,56 -> 11


n = float(input('Введите число \n'))
num = str(abs(n)).replace('.','')
sum = 0
for i in range(len(num)):  # len - возвращает количество элементов в контейнере
                        # range - это последовательность всех элементов, длина в for
    sum += int(num[i])
print(sum)








# n = float(input('Введите число \n'))
# def sum_digit(n):
#     return sum(map(int, list(str(abs(n)).replace('.',''))))
# print(sum_digit(n))



# Ключевое слово def в начале функции сообщает интерпретатору о том, 
# что следующий за ним код — есть её определение. Всё вместе — это объявление функции.

# # объявим функцию my_function()
# def my_function():
#     # тело функции

# input() --> для ввода
# list(input()) --> разбить введенное на цифры
# map(int, list(input())) --> каждую цифру привести к целому (у нас ведь изначально текст)
# sum(map(int, list(input()))) --> посчитать сумму цифр
# print(sum(map(int, list(input())))) --> вывести сумму
# str — Строка, к которой применяется метод (тип данных string).
# str(n).replace('.','') -> означает в строке заменяем все точки на ничего. Удаляем все точки и получаем целове 





# from random import uniform
# n = round(uniform(1, 100), 3)
# def sum_digit(n):
#     return sum(map(int, list(str(n).replace('.',''))))
# print(n)
# print(sum_digit(n))