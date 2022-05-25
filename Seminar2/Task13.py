# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

# Пример:

# Для N = 5: 1, -3, 9, -27, 81

# N = int(input('Введите число \n'))
# a = 1
# print(1, end=' ')
# for i in range(1, N):
#     a = a * (-3)
#     print(a, end=' ')

N = int(input('Введите число \n'))
for i in range(N):
    result = (-3)**i        #   выражение (-3)**0  = 1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    print(result, end=' ')

# второй вариант с рандомом

# from random import randint
# N = int(input('Введите число \n'))
# for i in range(N):
#     print(randint(-100, 100), end=' ')
