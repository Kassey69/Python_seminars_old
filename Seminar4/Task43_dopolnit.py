# Найдите корни квадратного уравнения Ax^2 + Bx + C = 0 двумя способами:
# 1) С помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python

# import random
# import math
# minValue = -10
# maxValue = 10
# indexes = []
# for i in range(3):
#     indexes.append(random.randint(minValue, maxValue))
# print(
#     f'Решаем квадратное уравнение {indexes[2]} X^2 + {indexes[1]}X + {indexes[0]} = 0')
# discr = indexes[1]**2 - 4 * indexes[0] * indexes[2]
# if discr < 0:
#     print('корней не существует')
# elif discr == 0:
#     print(f'Корень Х = {-indexes[1]/(2*indexes[2])}')
# else:
#     print(f'КОрень Х1 = {(-indexes[1] + math.sqrt(discr)) / (2*indexes[2])}')
#     print(f'КОрень Х2 = {(-indexes[1] - math.sqrt(discr)) / (2*indexes[2])}')

# 2 вариант - С помощью математических формул
a = 1
b = 2
c = -3
a = float(a)
b = float(b)
c = float(c)
discriminant = b ** 2 - 4 * a * c
print('Дискриминант = ' + str(discriminant))
if discriminant < 0:
    print('Корней нет')
elif discriminant == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print('x1 = ' + str(x1))
    print('x2 = ' + str(x2))
# 
# 3 вариант

import math
a = 1
b = 2
c = -3
def find_roots(a, b, c):
    dis_form = b * b - 4 * a * c   # получаем дискриминант
    sqrt_val = math.sqrt(abs(dis_form)) # получаем корень
    
    if dis_form > 0: # по формулам получаем корни
        print(f'x1 = {(-b + sqrt_val) / (2 * a)}')
        print(f'x1 = {(-b - sqrt_val) / (2 * a)}')
    elif dis_form == 0:
        print(f'x = {-b / (2 * a)}')
    else:
        print('Корней нет')


find_roots(a, b, c)