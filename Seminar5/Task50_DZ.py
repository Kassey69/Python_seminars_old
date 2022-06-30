# 44.                 н сдал как 43
# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10, 7] => [2, 10]

'''Класс Counter() модуля collections - это подкласс словаря dict для подсчета хеш-объектов 
(неизменяемых, таких как строки, числа, кортежи и т.д.). Это коллекция, в которой элементы хранятся 
в виде словарных ключей, а их счетчики хранятся в виде значений словаря.
Элементы считываются из итерируемой последовательности, инициализируются из другого словаря или счетчика Counter():'''

'''Метод Counter в Python https://pythonim.ru/osnovy/metod-counter-v-python
Counter - может удалять элемент из списка del counter['Unicorn']'''

'''Функция filter() в Python применяет другую функцию к заданному итерируемому объекту 
(список, строка, словарь и так далее), проверяя, нужно ли сохранить конкретный элемент или нет. 
Простыми словами, она отфильтровывает то, что не проходит и возвращает все остальное.'''

from collections import Counter
Mylist = [1, 2, 3, 5, 1, 5, 3, 10, 7]
print(Mylist)
f = Counter(Mylist) # сдесь counter разложил все элементы по количеству и присвоил их значение f
print(f) # Counter({1: 2, 3: 2, 5: 2, 2: 1, 10: 1, 7: 1})
res = list(filter(lambda x: f[x] == 1, Mylist)) # x у нас элемент, 
# f список с присвоенными значением количества каждого элемента, filter фильтрует все ненужное и оставляет за бортом
# в качестве первого аргумента мы передадим lambda x: f[x] == 1 оставлять элементы только с количеством 1
# d качестве 2 аргумента набор данных Mylist
print(res) # [2, 10, 7]

'''2 вариант'''
from collections import Counter
Mylist = [1, 2, 3, 5, 1, 5, 3, 10, 7]
def count(Mylist):
    f = Counter(Mylist)
    return [x for x in Mylist if f[x] == 1]
print(count(Mylist))
print("")

'''2 вариант'''
import random
def rand(n):
    return [random.randint(6,14) for i in range(n)]
def count(lst):
    return [a for a in set(lst) if lst.count(a) == 1] # lst.count(a) - тут просчитано количество подторений элементов
n = random.randint(5,12)
Mylist = rand(n)
print(f'Список рандомных элементов {Mylist} ') # [8, 13, 10, 13, 6, 6, 13]
print(f'Список уникальных элементов {count(Mylist)}') # [8, 10]


'''Немного на другую тему'''
'''Как найти все повторяющиеся элементы в списке и количество повторов?'''
def test(lst):
    return {a: lst.count(a) for a in set(lst) if lst.count(a) > 1}
print(test([10, 10, 23, 10, 123, 66, 78, 123])) # {10: 3, 123: 2}



'''3 вариант'''
myList = [1, 2, 3, 5, 1, 5, 3, 10, 7]
occurrences = []
print(f'Дана последовательность чисел: {myList}')
 
for i in myList:
    counts = 0
    for x in myList:
        if x == i: # если находится одинаковый элемент то 
            counts += 1 # присваивается ему count
    occurrences.append(counts) # составляем список count
# print(occurrences)
'''Set Python — это неупорядоченный и неиндексированный набор элементов.'''
#Источник: https://pythononline.ru/osnovy/set-python
duplicates = set()
index = 0
while index < len(myList):  # Функция len() возвращает длину (количество элементов) в объекте
    if occurrences[index] == 1: # если встречается среди индексов элемент равный 1 тогда
        duplicates.add(myList[index]) # myList[index] это уже элемент под индексом как в си шарпе
                                    # add() Добавляет элемент в набор
    index += 1
# Метод set.add() добавляет элемент elem в множество set. 
# Множества не поддерживают сортировку, по этому элемент elem добавляется в произвольное место, не обязательно в конец.
# Метод set.add() игнорирует добавление существующих элементов.
print(f'уникальных элементы: {duplicates}')

#Источник: https://tonais.ru/list/poisk-unikalnyh-i-povtoryayuschihsya-elementov-v-spiske-python


import time
import random

def unique_elements(Mylist):
    result_list = [] # с уникальными элементами
    for i in Mylist: 
        if i not in result_list: # ищем по списку отсутствующее число
            result_list.append(i) # если число отсутствует то мы его добавляем
    return result_list # значение возвращаем

def unique_elements_by_set(Mylist):
    #return list(set(list))
    #return [i for i in set(list)] # set неупорядоченная коллекция уникальных ссылок на обьекты
    return list(filter(lambda x: Mylist.count(x) == 1, Mylist)) # count вернет количество элементов в последовательности
    # функция filter берет по одному элементу из нашей последовательгности list(последний) и опрокидывает в lambda x
    # и проверяем list.count(x) == 1, если вернется истина Trye то значит все правильно нам подходит

tst_list = [1,2,3,5,1,5,3,10]
testing = unique_elements(tst_list)
print(unique_elements_by_set(testing))

'''Тесты'''
# Тест 1
tst_list = [1, 2, 3,5, 1, 5, 3, 10]
expected_result = [1, 2, 3, 5, 10]
actual_result = unique_elements(tst_list)
print('\n Тест 1')
print(f'Входной список: {tst_list}')
print(f'Результат: {actual_result}). Результат верен: {actual_result == expected_result}')

# Тест 2
tst_list = [1, -2, 1, -2, 0, 0]
expected_result = [1, -2, 0]
actual_result = unique_elements(tst_list)
print('\n Тест 2')
print(f'Входной список: {tst_list}')
print(f'Результат: {actual_result}). Результат верен: {actual_result == expected_result}')

# Тест 3 (производительность)
print('\n Тест 3 (производительность)')
for i in range(0, 3):
    n = 10000 * 10**i
    print(f'Количество элементов: {n}')
    tst_list = [random.randint(0, 100) for i in range(0, n)]
    start_time = time.time()
