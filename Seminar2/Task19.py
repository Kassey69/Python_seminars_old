# Задать список из n чисел последовательности $(1+\frac 1n)^n$ и вывести на экран их сумму


import random
n = random.randint(2, 8)
my_list = [round(((1 + 1 /i) ** i),2) for i in range(1, n+1)] #списк с вычислением, округленный в цикле 
print(my_list)
# my_list = list(map(float, my_list))
print(f'Сумма: {round(sum(my_list), 2)}') # функцияы sum c округлением
