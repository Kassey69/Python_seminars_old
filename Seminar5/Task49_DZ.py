# 36.                    но сдал я ее как 35
# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

# A = '1 2 3 5 6 7 8 10'   2   A[i] - 1 = A[2] - 1 = 3 - 1 = 2   и  A[2 - 1] = A[1] = 2    2 == 2 уcловие правильное
# A[4] - 1 = A[]           3   A[i] - 1 = A[3] - 1 = 5 - 1 = 4   b  A[3 - 1] = A[2] = 3    4 != 3 цифра 4 пропущена


# lists = '1 2 3 5 6 7 8 10'
with open('49_natyr.txt', 'w') as data: # ну а тут открываем файл и принудительно записываем в него
    data.write('1 2 3 5 6 7 8 10')
# My_list = [int(x) for x in list.split()]
f1 =  open('49_natyr.txt') # считываем содержимое файла
pol = f1.read() # переписываем содержимое файла в pol
print((pol)) # 1 2 3 5 6 7 8 10
My_list = list(map(int, pol.split())) 
print((My_list)) # [1, 2, 3, 5, 6, 7, 8, 10] преобразованный  list = [] map(int split ) делают запятые 

# 2 вариант приготовления
with open('48_natyr.txt', 'w+') as data: # ну а тут открываем файл и принудительно записываем в него
    data.write('1 2 3 5 6 7 8 10')
    data.seek(0)
    result = []
    for line in data.readlines():
        result += [int(i) for i in line.split()]
    print(result) # [1, 2, 3, 5, 6, 7, 8, 10]

'''Set Python — это неупорядоченный и неиндексированный набор элементов.'''
#Источник: https://pythononline.ru/osnovy/set-python
def find_number(My_list):
    My_list1 = set(My_list) # основной список, set - неповторимые значения
    temp_list = set(list(range(My_list[0], My_list[-1]+1))) # список всех элементов от 0 до послед. элемента -1 + 1 до 10
                                            # потому что в range и с 0 начинаем. последний элемент будет меньша на 1
    res = temp_list - My_list1 # находим недостающие числа
    return f'Список: {temp_list}', f'Список2:{My_list1}', f'Результат: {sorted(res)}' 
 # ('Список: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}', 'Список2:{1, 2, 3, 5, 6, 7, 8, 10}', 'Результат: [4, 9]')

print(find_number(My_list))


'''2 вариант'''
with open('47_natyr.txt', 'w') as data: # ну а тут открываем файл и принудительно записываем в него
    data.write('1 2 3 5 6 7 8 10')

with open('47_natyr.txt') as data:
    # my_list = data.read()
    Mu_list = list(map(int, data.read().split())) # мы получим списко чисел которые записаны в файл сразу

                                            # 1 2 3 5 6 7 8 10
def find_number(Mu_list):
    result = []
    for i in range(len(Mu_list) - 1):
        # print(Mu_list[i], end=' ')
        if (Mu_list[i + 1] - Mu_list[i]) > 1:  # 5 - 3 = 2 это больше 1 а значит мы нашли недостающий элемент
            result.append(Mu_list[i] + 1) # вписываем недостающий эkемент в созданный список
        print(Mu_list[i], i)  # A[i] - 1 = A[i-1]
    return result
print (find_number(Mu_list,))
print("")

'''3 вариант'''
with open('47_natyr.txt', 'r') as data: # открыли
    l = list(map(int, data.read().split(' '))) #gjkexbkb список
set1 = set(l) # преобразуем список во множества
set2 = set(list(range(l[0], l[-1]+1))) # делаем множества с помощью функции range от 0 элемента и до последнего с шагом +1
print(set1)
print(set2)
print(sorted(set1- set2))  # [] пусто
print(sorted(set2 - set1)) # [4, 9]


'''4 вариант'''
