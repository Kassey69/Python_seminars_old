# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# Пример:

# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

import math
x1 = float(input('Введите координаты х1 \n'))
x2 = float(input('Введите координаты х2 \n'))
y1 = float(input('Введите координаты y1 \n'))
y2 = float(input('Введите координаты y2 \n'))
result = round(math.sqrt((x2-x1)**2+(y2-y1)**2), 2)
print(result)
# print('{:.2f}'.format(result), sep='')


