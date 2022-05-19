# Напишите программу, которая принимает на вход координаты точки (X и Y),
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3
numX = int(input('Введите координаты Х \n'))
numY = int(input('Введите координаты Y \n'))
if numX > 0 and numY > 0:
    print('Это 1 четверть')
elif numX < 0 and numY > 0:
    print('Это 2 четверть')
elif numX < 0 and numY < 0:
    print('Это 3 четверть')
elif numX > 0 and numY < 0:
    print('Это 4 четверть')
elif (numX == 0 and numY > 0) or (numX == 0 and numY < 0):
    print('Это ось Y')
elif (numX > 0 and numY == 0) or (numX < 0 and numY == 0):
    print('Это ось Х')
else:
    print('Введены некорректные данные')
    
