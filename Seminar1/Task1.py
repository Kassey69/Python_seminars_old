# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# Примеры:

# 5, 25 -> да
# 4, 16 -> да
# 25, 5 -> да
# 8,9 -> нет

first = int(input('Введите первое число '))
second = int(input('Введите второе число '))
if (first * first == second):
    print(f'второе число {second} квадрат первое {first}')
elif (first * first != second):
    print(f'второе число {second} не квадрат первое {first}')
else: # или просто else и то и то правильно
    print(f'второе число {second} не квадрат первое {first}')
