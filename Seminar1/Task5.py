# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# num = int(input('Введите число \n')) 
# if (num % 5 == 0 or num % 10 == 0 or num % 15 == 0) and num % 30 != 0:
#     print(f'число {num} кратное заданному ')
# else:
#     print('число не кратно')



# Ключевое слово def в начале функции сообщает интерпретатору о том, 
# что следующий за ним код — есть её определение. Всё вместе — это объявление функции.

# объявим функцию my_function()
# def my_function():
    # тело функции


num = int(input('Введите число:\n '))
def n(num):
    return ((num % 5 == 0 and num % 10 == 0) or num % 15 == 0) and not num % 30 == 0
       # return (num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and num % 30 !=0
print(n(num))

# import random
# num = random.randint(5,300)
# print((num))
# # num = int(input('Введите число:\n '))
# def n(num):
#     return ((num % 5 == 0 and num % 10 == 0) or num % 15 == 0) and not num % 30 == 0
#        # return (num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and num % 30 !=0
# print(n(num))


  


