# Задание 9.
# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

from math import lcm
import random

# Чтобы получить наименьшее общее кратное в Python, мы должны применить формулу.
'''НОК(a, b) = (a * b) / НОД(a, b)'''
# Какова логика для x, y = y, x для замены значений
# https://stackoverflow.com/questions/31374721/what-is-the-logic-for-x-y-y-x-to-swap-the-values


a = random.randrange(-10, 90)
b = random.randrange(-10, 90)
print(a, b)
# def get_lcm(a, b):
#     return lcm(a, b)
# print(get_lcm(a, b)

# проверяем корректность введенных данных
if (a <= 0) or (b <= 0):
    print("данные некорректны, ничего не гарантирую")

# определяем НОД чисел a и b
x, y = a, b
while (y > 0):
    x, y = y, x % y
print("НОД равен", x)

# вычисляем НОК
c = a * b / x

# выводим ответ
print("НОК равен", c)
