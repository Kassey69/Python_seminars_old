'''Для натурального N создать множество 1, -3, 9, -27'''
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

N = 5
My_list = [1]
a = 1
for i in range(1, N):
    a *= 3
    if i % 2 != 0: # если индекс от деления не равен 0 то  умножаем на -1, все индексы неченые будут с минусом
        My_list.append(a * -1)
    else:
        My_list.append(a)
print(My_list)

# вариант 2
N = 5
My_list = []
a = 0
for i in range(0, N):
    a = (-3)**i  # ** означает степень
    My_list.append(a)
print(My_list)


# вариант 3 функция сборная, самое короткое решение
def naturN(n):
    return [(-3)**i for i in range(n)] # [] это сокращение My_list.append(аргумент)
print(naturN(5))


file_name = 'E:\Programming\Visual_Studio_Code\Python_seminars\Seminar3\Task24_file.txt'
lst = naturN(5) # получили список с помощью функции 
with open(file_name, 'w') as file: # открыли файл и 'w' Только для записи.
    for item in lst: # и начинаем бещагнть в цикле for по списку
        file.write(f'{item}\n') # записываем {item}\n
        '''print(item, file = file, end=' ') # записываем в строчку'''

'''УЗНАТЬ КАК ДЕЛАТЬ ПРОБЕЛ МЕЖДУ СТРОКАМИ В ТЕКСТОВОМ ФАЙЛЕ С ДАННЫМИ'''

'''https://pythonru.com/osnovy/fajly-v-python-vvod-vyvod'''
file_name = 'E:\Programming\Visual_Studio_Code\Python_seminars\Seminar3\Task24_file.txt'
lst = naturN(5) # получили список с помощью функции 
with open(file_name, 'a') as file: # открыли файл и командой 'а' добавили содержимое
    for item in lst: # и начинаем бещагнть в цикле for по списку
       
        print(item, file = file, end=' ')



# вариант функция 4 через список
def nat(n):
    My_list = []
    i = 0
    while i < n:
        a = (-3)**i 
        My_list.append(a)
        i += 1
    return My_list
print(f'Цикл While', nat(5))


# вариант функция 5 через string
def nat(n):
    string = ''
    a = 1
    for i in list(range(1,n+1)):
        string = string + str(a) + ','
        a = (-3)**i 
    return [string]
print(f'Цикл for {nat(5)}')

# вариант 6
n = 5
for i in range(0, n):
    # a = (-3)**i
    # print(a)
    print((-3)**i, end=' ')
print("") # Пропуск строки!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# вариант 7
n = 5
record = []
for i in range(0, n):
    a = (-3)**i
    record.append(a)
    print(a, end=' ')
    # print((-3)**i)

file_name = 'E:\Programming\Visual_Studio_Code\Python_seminars\Seminar3\Task24_file2.txt'
lst = record
with open(file_name, 'w') as file:
    for item in lst:
        file.write(f'{item}\n')

print("")



# вариант 8 - самы быстрой способ решения
n = 5

with open('E:\Programming\Visual_Studio_Code\Python_seminars\Seminar3\Task24_file2.txt', 'a') as file:
    def openfile(n):
        for i in range(n):
            file.write(str((-3)**i) + '\n')
        return [(-3)**i for i in range(n)]
    print(openfile(n))


# вариант 9 

n = 5
def openfile2(n):
    file_name = 'E:\Programming\Visual_Studio_Code\Python_seminars\Seminar3\Task24_file2.txt'
    with open('E:\Programming\Visual_Studio_Code\Python_seminars\Seminar3\Task24_file2.txt','a') as file:
        # print(dir(file.flush())) # просматриваем методы, их много и все можно использовать в разных случаях
        # flush() к примеру
        for i in range(n):
            file.write(f'{(-3)**i}\n ')
    return [(-3)**i for i in range(n)]
print(openfile2(n))


# вариант 10
def openfile3(n):
    file = open('E:\Programming\Visual_Studio_Code\Python_seminars\Seminar3\Task24_file2.txt', 'a')
    # n = int(input('Введите размер списка: '))
    # for i in list(range(1, n+1)):
    #     file.write(f'{(-3)**i} ') 
    # file.writelines(list(map(str, range(1, n+1))))
    file.writelines([f'{(-3)**i} ' for i in list(range(n))]) #стрингом f'{(-3)**i} ' записать по циклу
    file.close()
    return [(-3)**i for i in range(n)]
n = 5
print(openfile3(n))

'''-----------------------------------------------------------------------------------------'''
# from pprint import pprint
# a = []
# pprint(dir(a)) # дает возможность увидеть все команды dir


from datetime import datetime, timedelta
from pyexpat import features # библиотека позволяющая очень удобно работать с датами

now = datetime.now() # текущая дата
feature = now + timedelta(days = 160) # мы можем получить будущую дату = бурем текущую дату и 
                                      # прибавляем к примеру 160 дней вперед                           
print(now, feature) 
print(now < feature) # сравниваем now меньше чем будущее feature или нет  True False
print(feature.strftime('%d--%m-->%Y %H:%M')) # с помощью данного метода красиво выводится дата 03--12-->2022 22:33

p = now - timedelta(days = 160)
if  now < p + timedelta(days=159):
    print('Пора оплачивать подписку ')
