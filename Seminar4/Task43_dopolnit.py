# Найдите корни квадратного уравнения Ax^2 + Bx + C = 0 двумя способами:
# 1) С помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python

'''Формулы корней квадратных уравнений https://www.sites.google.com/site/kvadratnyeuravenia/information/standartnyj-vid'''
'''переходим на сайт через зажание снопки ALT + навести курсор мышки и нажать'''
'''D = b^2 - 4*a*c если   D < 0  то коня нео;   если  D = 0  то один корень и нахоится по формуле  (- b / 2 * a);'''
'''Если  D > 0  то получаются два корня ((-b + √ D) / (2 * a)) и ((-b - √ D) / (2 * a))'''

import math
import random
def rand(znach):
        znach = round(random.uniform(-10, 10),1) # вариант с вещественными числами
        if znach == 0: # вдруг попадается ноль мы крутим рандом по новой
            znach = round(random.uniform(1, 10),1)
        return znach 

def sqrt_dis(a,b,c):
    print(f' Находим корни квардратного уравнения: {a}x^2 + {b}x + {c} = 0')
    dis = b ** 2 - 4 * a * c
    print(f'Дискриминант: {round((dis),2)}')
    sqrt_val = math.sqrt(abs(dis)) # получаем корень и подставляем при желдании его везде

    if dis < 0:
        print(f'Корней нет') 
    elif dis == 0:
        kor = round((- b / 2 * a),4)
        print(f'Один корень: {kor}')
    elif dis > 0 :
        kor1 = round(((-b + sqrt_val) / (2 * a )),4)
        kor2 = round(((-b - sqrt_val) / (2 * a )),4)
        print(f'1 корень X1: {kor1} \n2 корень X2: {kor2}')

znachie = []  #слзхдаем список, в него будут переходить значения с функции rand рандома
a1 = rand(znachie) # нагружаем список рандомным значением от функции rand и передаем аргументам
b1 = rand(znachie) 
c1 = rand(znachie)
sqrt_dis(a1,b1,c1) # если работать без return то получается как в си шарпе void, мы подключаем все вычисления
# производимые в функции sqrt_dis к 3 значениям, функция получает значения рандомные и вычисляет изнутри себя
# выдает внутренние print
print(" ")


'''Вариант 2'''
from random import choice
import math
minValue = -10
maxValue = 10
indexes = []
for i in range(3):
    # indexes.append(random.randint(minValue, maxValue))
    indexes.append(choice([i for i in range(minValue, maxValue) if i not in [0]])) # мы используем метод рандома 
    # с искблючением нуля - from random import choice, сощдаем список 
print(
    f'Решаем квадратное уравнение {indexes[2]} X^2 + {indexes[1]}X + {indexes[0]} = 0')
'''Обычно выражение D = b^2 - 4*a*c обозначают буквой D и называют дискриминантом квадратного уравнения ax2 + bx + c = 0'''
discr = indexes[1]**2 - 4 * indexes[0] * indexes[2]
if discr < 0:
    print('корней не существует')
    
elif discr == 0: # то есть один корень и нахоится по формуле  (- b / 2 * a)
    print(f'Корень Х = {round(-indexes[1]/(2*indexes[2]),4)}')
else: # два корня по формуле ((-b + √ D) / (2 * a)) и ((-b - √ D) / (2 * a))
    print(f'Корень Х1 = {round((-indexes[1] + math.sqrt(discr)) / (2*indexes[2]),4)}')
    print(f'Корень Х2 = {round((-indexes[1] - math.sqrt(discr)) / (2*indexes[2]),4)}')
print("")

# 3 вариант - С помощью математических формул
a = 1
b = 2
c = 1
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
print("")


# 4 вариант
import math
a = 5
b = 5
c = -1
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