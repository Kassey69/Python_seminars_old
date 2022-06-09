'''
Задайте строку из набора чисел. Напишите программу, которая покажет
большее и меньшее число. В качестве символа-разделителя используйте пробел.
'''

# import random
#
# my_string = ' '.join([str(random.randint(1, 40)) for i in range(10)])
# print(my_string)
# print(f'max={max(map(int, my_string.split(" ")))} min={min(map(int, my_string.split(" ")))}')

'''
2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    1) с помощью математических формул нахождения корней квадратного уравнения
    2) с помощью дополнительных библиотек Python
'''

# a = 1
# b = 2
# c = -3
# a = float(a)
# b = float(b)
# c = float(c)
# discriminant = b ** 2 - 4 * a * c
# print('Дискриминант = ' + str(discriminant))
# if discriminant < 0:
#     print('Корней нет')
# elif discriminant == 0:
#     x = -b / (2 * a)
#     print('x = ' + str(x))
# else:
#     x1 = (-b + discriminant ** 0.5) / (2 * a)
#     x2 = (-b - discriminant ** 0.5) / (2 * a)
#     print('x₁ = ' + str(x1))
#     print('x₂ = ' + str(x2))
#
# import math
#
#
# def find_roots(a, b, c):
#     dis_form = b * b - 4 * a * c
#     sqrt_val = math.sqrt(abs(dis_form))
#
#     if dis_form > 0:
#         print(f'x₁ = {(-b + sqrt_val) / (2 * a)}')
#         print(f'x₂ = {(-b - sqrt_val) / (2 * a)}')
#     elif dis_form == 0:
#         print(f'x = {-b / (2 * a)}')
#     else:
#         print('Корней нет')
#
#
# find_roots(a, b, c)

'''
Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
'''

# def calculate_lcm(x, y):
#     greater = x if x > y else y
#     while True:
#         if (greater % x == 0) and(greater % y == 0):
#             lcm = greater
#             break
#         greater += 1
#     return lcm
#
#
# print(calculate_lcm(6, 8))
# print(calculate_lcm(4, 6))