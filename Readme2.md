# типы данных и переменные
# int, float, boolean, str, list, None

# a = input()  # это строковый формат
# a = int(input())  # 'это численный формат

print(f'{a} - {b} - {s}') # вариант с интерполяцией

c = a * b
c = a / b
c = a //b # деление в целых числах
c = a % b  # остаток от деления
c = a ** b # возведение в степень
c = round(a * b,3) # такая команда округлит число и черзе запятую с дробью, с каким то количчеством знаков
s = round(a * b, 6) # столько поставим столько и будет знаков после запятой в запписимости от числа на которое множим
print(s)

import math
result = round(math.sqrt((x2-x1)**2+(y2-y1)**2), 2)
print(result)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and,or - не путрать с &, |, ^
# Кое что еще: is, is not, in, not in

# проверка четность числа
is_odd = f[0] % 2 == 0 # первое значение индекса равно 1 . 
# остаток от деления не будет равен 0, потмоу что 1 число не четное
print(is_odd)
is_odd =  not f[0] % 2 # это тоже самое, более пайтоновский вариант записи
print(is_odd)

# Цикл while
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
    print(original)
else:
    print('Пожалуй хватит')
print(inverted)

# Управляющие конструкции:
# for
for i in 1, 2, 3, 4, 5:
    print(i**2)
list = [1, 2, 3, 4, 5]
for i in list:
    print(i)
# r = range(10)
# for i in r:
# for i in range(10): #от 0 до 9
# for i in range(1, 5): # от 1 до 4
for i in range(1, 10, 2): # от 1 до 9 и приращение 2, и получим нечетные сисла 1 + 2 = 3, 3 + 2 = 5, 5 + 2 = 7, 7 + 2 =  9 
    print(i)
for i in 'ewr  - + sd': # побуквенная разбивка
    print(i)

# Преобразование строки в число!
 1. def string_to_number(s):
    return int(s)

 2. string_to_number = lambda n: int(n)

 3. def string_to_number(s):
    i = int(s)
    return i

 4. def string_to_number(string):
    string = int(string)
    return string

    a = string_to_number("1234")
    b = string_to_number("605")
    c = string_to_number("1405")
    d = string_to_number("-7")


# len - возвращает количество элементов в контейнере
# range - это последовательность всех элементов, длина в for
    for i in range(3, 100, 25):
    print(i)
Если ваш шаг равен 25, то выдача вашего цикла будет выглядеть вот так:
3
28
53
78
