# Реализовать алгоритм задания случайных чисел. 
# Без использования встроенного генератора псевдослучайных чисел

# from datetime import datetime as dt
# from random import random

# from Seminar2.Task22_DZ import My_list

# def my_random(min, max):
#     rnd = dt.now().microsecond
#     scale = max - min
#     return int(rnd/100000 + scale + min)

# print(my_random(10, 50)) # под вопросом это решение!!!!!!!!!


# 2 вариант

from datetime import datetime
def my_randing():
    multiplier = datetime.now().microsecond % 10 # рандом от 0 до 9
    return datetime.now().microsecond % 10 ** multiplier
print(my_randing())

print(int(str(datetime.now().timestamp()).replace('.', '')))

# '''datetime.now() - это текущая дата, она в каждый момент времени меняется'''
# '''timestamp -конкретная дата и время представлены в разных форматах.'''

# 3 вариант

from datetime import datetime
print(round(datetime.now().second/10 * 7))




# Реализовать алгоритм задания случайных чисел. 
# Без использования встроенного генератора псевдослучайных чисел
# 4 вариант
import random

def rand(My_list, N):
    for i in My_list: 
        if N in str(i): # мы работаем со списком поэтому надо индекс сделать стрингом
            return True
    else:
        return False
    
My_list = ['123', '234', '423', '5']
N = str(random.randint(1,9)) # мы работаем со списком поэтому надо значение сделать стрингом, чтоб он нашел в списке
print(N)
print(rand(My_list, N)) # False или True

