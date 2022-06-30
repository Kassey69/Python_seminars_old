# Задача 2.
# Задайте список(произвольный). Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

'''import random

list = [2, 'r3', 4, 're7d', 5, 6, 't9', 'чис8ло'] 
print(list)
n = str(random.randrange(1,12)) # рандомное значечние делать строкой
#n = (input('Введите искомое число \n'))
print(n)
count = 0 # есть счетчик
for i in list: # тут list это сам список и он идет перебирает элементы списка
    # i = str(i) # свели все значения к строке,чтоб читались буквы, у нас встречаются и числа, поэтому переводим в строку
    # for x in i: # находим число в строках, если есть
    #     if n == x: 
        if n in str(i):   #сокракщаем три строчки разом
            print(f'число {n} найдено')
            count = 1   # если мы находим такое число в списке то счетсик равен 1
            break
if count == 0: # если мы не нашли такое число в списке счетчик по прежнему равен 0
# else:
    print(f'числа {n} отсутствует')'''

# Метод isdigit() возвращает True, если все символы в строке являются цифрами. Если нет, возвращается False.
# Источник: https://pythonstart.ru/string/isdigit-python

# import random

# n = random.randrange(2,10) #задает рандомное количесво чисел в диапазоне от 2 до 10
# list = []
# for i in range(n):
#     list.append(random.randint(1, n+1)) # заполняет числа рандомными значениями
# print(list)
# #list = [2, 3, 4, 5, 6, 9]
# for i in list:
#     if i == 3:
#         print('число найдено')2
#         break
# else:
#     print('числа 3 в уравнении нет')

# list = [2, 3, 4, 'red', 5, 6, 9, 'чис3ло']
# n = (input('Введите искомое число \n'))
# for i in list:
#     i = str(i)
#     if n == i:
#         print(f'число {n} найдено')
#         break
# else:
#     print(f'числа {n} в уравнении нет')


import random
import string
def generate_alphanum_random_string(length):
    length = random.randint(4,9)
    for i in range(length):
        # Чтобы сгенерировать буквенно-цифровую случайную строку в Python, 
        # используйте константы string.ascii_letters и string.digits, чтобы получить комбинации букв и цифр.-
        letters_and_digits = string.ascii_letters + string.digits
        rand_string = ''.join(random.sample(letters_and_digits, length))
        # print("Рандомная строка", length, "символов:", rand_string)
    return rand_string
my_list = []
# for i in generate_alphanum_random_string(my_list):
for i in generate_alphanum_random_string(my_list): # рандом готовит йчейки памяти --- 'length = random.randint(4,5)'
    my_list.append(generate_alphanum_random_string(my_list)) # ячейки памяти заполняются рандомными цифробуквенными элементами
print("Рандомная список строк", (my_list))

# my_list = ['ref', 3, '4', 'adw23essd', 'ljk9']
n = str(random.randint(2, 9))
print(n)
def chislo(my_list, n):
    count = 0 # есть счетчик
    for i in my_list:
        if n in str(i): # свели все значения к строке,чтоб читались буквы, у нас встречаются и числа, поэтому переводим в строку
            count = 1 # если мы находим такое число в списке то счетсик равен 1
            return (f' Число {n} присутствует в списке')
            # break

    else: # если мы не нашли такое число в списке счетчик по прежнему равен 0
        return (f' Число {n} нет в списке')
print(chislo(my_list, n))

print(" ")
# еще вариант 2
import random

def rand(My_list):
    N = str(random.randint(1,9)) # мы работаем со списком поэтому надо значение сделать стрингом, чтоб он нашел в списке
    print(N)
    for i in My_list: 
        if N in str(i): # мы работаем со списком поэтому надо индекс сделать стрингом
            return True
    return False
    
My_list = ['123', '234', '423', '5']
# N = str(random.randint(1,9)) # мы работаем со списком поэтому надо значение сделать стрингом, чтоб он нашел в списке
print(My_list)
print(rand(My_list)) # False или True


# еще вариант 3
My_list = ['123', '234', '423', '5']
print(My_list)
def is_number_in(number):
    for i in My_list:
        if str(number) in i:
            return True
    return False
print(is_number_in(8)) # варинат с цифрой в конце

# еще вариант 4

My_list = ['123', '234', '423', 5, '5']

def find_number(num, lst):
    return str(num) in lst or num in lst # благодаря тому что мы сделали и интовые с стринговые варианты
print(find_number(5, My_list)) # получаем отклик в списке и числа и строки
print(find_number(55, My_list))
print(find_number(123, My_list))