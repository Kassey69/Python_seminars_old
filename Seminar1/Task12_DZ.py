# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# Пример:

# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

import math
Ax1 = float(input('Введите координаты Aх1 \n'))
Ay1 = float(input('Введите координаты Ay1 \n'))
Bx2 = float(input('Введите координаты Bx2 \n'))
By2 = float(input('Введите координаты By2 \n'))
result = round(math.sqrt((Bx2-Ax1)**2+(By2-Ay1)**2), 2)
print(result)
# print('{:.2f}'.format(result), sep='')
