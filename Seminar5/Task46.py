# Вычислить число pi  c заданной точностью d
#     Пример: при d = 0.001,  pi = 3.141. 10^-1  <= d <= 10^-10

# Различные методы обеспечения точности
# Следующие методы поставляются с математическим модулем.

# trunc() – метод trunc() удаляет все десятичные точки из числа с плавающей запятой. 
# Он возвращает целочисленное значение без десятичной части.
# ceil() – этот метод печатает наименьшее целое число, большее заданного числа.
# floor() – этот метод печатает наибольшее целое число, меньшее целого.
# Источник: https://pythonpip.ru/osnovy/tochnost-python


def bbp(n): # сделали функцию которая считает число pi по одной из формул, формулы произвольно взяты
    # формулы отсюда взяты http://www.swsys.ru/files/2018-2/409-413.pdf
    pi = 0
    k = 0 # счетчик 
    while k < n:
        pi += (1/(16**k))*(4/(8*k+1)-2/(8*k+4)-1 / (8*k+5)-1/(8*k+6)) # одна из формул вычисления значения пи 
        k += 1 # добавляем следующую итерацию к
    return pi

d = 5  # количество знаков после запятой
print(f'pi = {round(bbp(d), d)}') # сдесь мы делаем округление полученного числа пи



# 2 вариант ( НЕНУЖНАЯ ЗАМОРОЧКА)
def CalculatePi(accuracy):
    myPi = 3
    temp = 0
    myAccuracy = 10 ** (-accuracy)
    i = 2
    sign = 1
    while abs(myPi - temp) > myAccuracy:
        temp = myPi
        myPi = myPi + sign * 4 / (i * (i +1) * (i + 2))
        sign = - sign
        i += 2
    return round(myPi, accuracy)

try:
    accuracy = 10
    if 0 < accuracy <= 10:
        print (f' Число  pi = {CalculatePi(accuracy)} ')
    else:
        print('Значение точности должно быть от 1 до 10')
except ValueError:
    print('Введено не число')



# 3 вариант

import math
from math import pi

n = pi
print(n)

# 4 вариант  Формула Бэйли — Боруэйна — Плаффа

n = 100
my_pi = sum(1/16**x*(4/(8*x + 1) -2 /(8*x + 4) -1 /(8*x + 5) -1 /(8*x + 6)) for x in range(n))

print(my_pi)

# Ряд Лейбница

# n = 20000000

# mypi = 4 * (sum(1/x for x in range(1, n + 1, 4)) +
# sum(-1/x for x in range(3, n + 1, 4)))

# print(format(mypi, '.100'))


