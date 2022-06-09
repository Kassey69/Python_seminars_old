# Задание 9.
# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

from math import lcm
import random

# Чтобы получить наименьшее общее кратное в Python, мы должны применить формулу.
# наименьшее общее кратное это то число которое делится на то и другое без остатка
'''НОК(a, b) = (a * b) / НОД(a, b)'''
# Какова логика для x, y = y, x для замены значений
# https://stackoverflow.com/questions/31374721/what-is-the-logic-for-x-y-y-x-to-swap-the-values


a = random.randrange(-10, 90)
b = random.randrange(-10, 90)
print(a, b)
# a, b = list(map(int, input().split()))
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

'''пояснение
x, y = 4, 6 --> 12
g = 6
if g % x and g % y
12 % 4 and 12 % 6
'''

def calculate_lcm(x , y):
    greater = x if x > y else y # если х больше чем у то мы меняем числа и получаем самое большое числа
    while True: # запускаем цикл где проверяем если большее число без остатка делится на х и на у то    
        if (greater % x == 0) and (greater % y == 0): 
            lcm = greater   # то мы записываем результат в переменную lcm   
            break           # и выходиим из цикла
        greater += 1        # иначе увеличиваем большее число на 1
    return lcm

print(calculate_lcm(6, 8))
print(calculate_lcm(4, 6))




