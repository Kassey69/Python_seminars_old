# Реализуйте случайное перемешивания списка.

# *Пример:*
# Исходный вариант -> ['Веселый пианист', 250, 3.14, 'True '] Результат -> [250, 3.14, 'True ', 'Веселый пианист']

import random
My_list = ['Веселый пианист', 250, 3.14, 'True ']
print(My_list )
random.shuffle(My_list )
print(My_list )


# 2 вариант - вот так примерно работает как раз рандом
from datetime import datetime
def my_shuffle(x):
    def randbelow(n):
        multiplier = len(str(n)) # мы получаем мультипликатор который будет длиной числа
        r = datetime.now().microsecond % 10 ** multiplier # создаем переменную в которую помещаем
# datetime.new().microsecond - это некое число 37978, применяем к нему % 10 возведенный в степень мультипликатора
        while r >= n: # и бегаем в бесконечном цикле пока переменная не станет r >= n
            r = datetime.now().microsecond % 10 ** multiplier # если r !>= n то еприменяем вновь и вновь эту функцию
        return r
    for i in reversed(range(1, len(x))):
        j = randbelow(i + 1)
        x[i], x[j] = x[j], x[i]

My_list = ['Веселый пианист', 250, 3.14, 'True ']
my_shuffle(My_list)
print(My_list)