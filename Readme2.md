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


весь курс тут:
https://geekbrainspro.notion.site/d6a1f6af984348ebb67e004a33f77735 - сайт по курсу гигбрейнс

весь курс тут:
https://geekbrainspro.notion.site/d6a1f6af984348ebb67e004a33f77735 - сайт по курсу гигбрейнс

весь курс тут:
https://geekbrainspro.notion.site/d6a1f6af984348ebb67e004a33f77735 - сайт по курсу гигбрейнс

весь курс тут:
https://geekbrainspro.notion.site/d6a1f6af984348ebb67e004a33f77735 - сайт по курсу гигбрейнс





colors = ['red', 'green', 'blue']
data = open('file.txt', 'w') #путь к файлу и мод с которым будем работать 
                            # a - дозапись, r - чтение, w - запись
# data.writelines(colors) # разделителей не будет
data.write('\nLINE 121\n')
data.write('LINE 131\n')
data.close()

#exit() # позволяет не выполнять код который дальше прописан
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
exit()

# СЛОВАРИ - неупорядщоченные коллекции произвольных объектов с доступом по ключу

distionary = {} #\ ставится если тяжело все описывать в рамках одной строки, это переноска на другую строку
distionary = \
    {
         'up': '↑',
         'left': '←',
         'down': '↓',
         'right': '→'
    }
#print(distionary) # { 'up': '↑','left': '←', 'down': '↓','right': '→'}
#print(distionary['left'])
# типы ключей могут отличаться

# for k in distionary.keys(): # ключи
for k in distionary.values(): # конкретные  значения
    print(k)

for v in distionary: # пробежимся по всем элементам нашего словаря
    print(v)

for v in distionary: 
    print(distionary[v]) # получаем только значения