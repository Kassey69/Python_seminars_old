# Задание 3.
# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет(по индексу).

# Пример:

# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

def spisok(my_list, n):
    count = 0 # включаем счетчик
    for i in range(len(my_list)): # Если нужно перебрать индексы элементов в списке, используем range(len(original_list))
        if n == my_list[i]: # мы перебираем индексы и поэтому можем в квадратные взять
            count += 1 #
            if count == 2:
                return f' позиция 2 вхождени равна индексу {i}' # i тут не элемент а индекс
    
    return f'-1'

my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
my_list1 =  ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
my_list2 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
my_list3 = ["123", "234", 123, "567"]
my_list4 = [123, 4, 123]
n = "qwe" 
n1 = "йцу"
n2 = "йцу"
n3 = "123"
n4 = 123
print(spisok(my_list, n))
print(spisok(my_list1, n1))
print(spisok(my_list2, n2))
print(spisok(my_list3, n3))
print(spisok(my_list4, n4))

# Вариант 2
n = 232
My_list = [123, 43, 545, 232, 5465, 232]

def find_number(My_list, n):
    return int(n) in My_list or n in My_list # чтобы и инт и стринг было решение, строк и чисел

print(find_number(My_list, n))

# Вариант 3
import random
def second_in(My_list, find): # создаем функцию по типу void, заполняем списком и искомым аргументом
    count = 0   # включаем счетчик
                                # https://pythonchik.ru/osnovy/python-range
    for i in range(len(My_list)): # перебирается цикл range  диапазон значений (len длины) списка, тут цикл идет по range
        #i = str(i)  #индексы списка должны быть целыми числами или срезами, а не str -- ОШИБКА!!!!!!!!!!
        if My_list[i] == find: # в цикле list ищем внутри каждого списка подсписок (индекс) list[i] = равный find
            count += 1 #  каждый раз когда мы находим искомый аргумент счетчик сприбавляет +1
            # нам нужно найти второе вхождение аргумента, и тут же выйти записав на каком месте он находится в списке
            if count == 2: 
                return i # как только получаем второе вхождение отправляем обратно позицию второго вхождения строки в списке
                # i начинается с 0 а не с 1
    if count < 2:
        return -1

'''My_list = list(map(str, input().split(', ')))''' #вводим значение str,
My_list = [123, 2, 5, 234]
# с помощью split разделяем текст через пробел или другой знак, с помощью map присваиваем значение int/str/float
# map() — это встроенная функция, которая позволяет обрабатывать и 
# преобразовывать все элементы в итерируемом объекте без использования явного цикла for, 
find = random.randint(1,5)
''' find = input('Введите значение \n')'''
print(second_in(My_list, find))

# list = ["123", "234", "123", "567"]
# find = "123"
# print(second_in(list, find))

# тут другое условие, сколько раз встречается а не второе касание
# value1 = 'as'
# value2 = 'sxascv acs asdf vsdg assd'
# n = 3
# def get_sec_entry(val1, val2):
#     start = val2.find(val1)
#     return val2.find(val1, start + 1)

# print(get_sec_entry(value1, value2))


from pprint import pprint

a = []

pprint(dir(a)) # смотрим  список методов, что можно исползовать, с двойными подчеркиваниями не смотрим
'''метод index - это метод, который принимает строку в себя, он еще принимат стартовый и конечный индекс 
откуда будет искать, и возвращает в ответе индекс'''


# Вариант 4

Mylist = ["qwe", "asd", "zxc", "qwe", "ertqwe","qwe"]
Mu_list1 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
znach = "qwe"
znach1 = "йцу"
def vhojdeine(Mylist, znach):
    for i in range(len(Mylist)):  
        if znach  in Mylist[i]:
            if Mylist.count(Mylist[i]) > 1:
                return (Mylist[i], Mylist.index(Mylist[i], i + 1))
    return -1
print(vhojdeine(Mylist, znach))
print(vhojdeine(Mu_list1 , znach1))
'''метод index - это метод, который принимает строку в себя, он еще принимат стартовый и конечный индекс 
откуда будет искать, и возвращает в ответе индекс'''
# list1.index - возвращает первый индекс по ключу и если такого индекса нет то будет ошибка

# Вариант 5
list1 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
znach = "йцу"
count = 0
for i in range(len(list1)):  
    # if str(znach) in list1[i]: # так будет искать совпадение элемента в списке заглядывая внутрь каждого элемента
    # "йцу" = "йцукен"
    if znach  == list1[i]: # наш вариант этот, нам нужно точное совпадение строк по элементно "йцу" = "йцу"
        count += 1 
    if count == 2: 
        print(' Вхождение индекса', list((list1[i], i))) # скобок надо двойные из за двух аргументов снутри, чтоб строка написана была целиком

''' Отвлеченный пример поиска одинаковых элементов'''
'''----------------------------------------------------'''
# def has1dup(lst):
#     setlst = list(set(lst)) # no duplicate elements
#     for i in range(len(setlst)): # while the setlist's element count, 
#         if lst.count(setlst[i]) > 1: # if the count of setlist[i] of lst is bigger than 1
#             return setlst[i] # return it
            
# lst = [344, 344, 590]
# print(has1dup(lst)) # 344
'''------------------------------------------------------------------------------------------'''

# Вариант 6
Mu_list = ["qwe", "asd", "zxc", "qwe", "ertqwe", "qwe"] #, ищем: "qwe", ответ: 3
Mu_list1 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"] #, ищем: "йцу", ответ: 5
Mu_list2 = ["йцу", "фыв", "ячс", "цук", "йцукен"] #, ищем: "йцу", ответ: -1
Mu_list3 = ["123", "234", 123, "567"] #, ищем: "123", ответ: -1
Mu_list4 = [] #, ищем: "123", ответ: -1

def find_second(lst):
    for i in range(len(lst)): # позволяет перебрать индексы элементов в списке
        if lst.count(lst[i]) > 1: # Метод подсчитывает количество вхождений повторящегося элемента lst[i] в список lst. 
         # lst - список, lst[i] - элемент списка с индексом который мы включили выше командой range(len(lst)
            print(f' Количество вхождений  {lst.count(lst[i])}') #  Количество вхождений  
            return (lst[i], lst.index(lst[i], i + 1)) # возвращаем сам элемент, 
                # подсчет индекса эдемента в строке от начала старта нулевого индекса и до конечного с шагом + 1
    return "-1"
'''метод index - это метод, который принимает строку в себя, он еще принимат стартовый и конечный индекс 
откуда будет искать, и возвращает в ответе индекс'''

print(find_second(Mu_list)) # ('qwe', 3)
print(find_second(Mu_list1)) # ('йцу', 5)
print(find_second(Mu_list2)) # -1
print(find_second(Mu_list3)) # -1
print(find_second(Mu_list4)) # -1

'''Пояснения lst.count(setlst[i])'''
'''list.count(x) Метод подсчитывает количество вхождений элемента x в list.'''
#>>> lst = [1, 2, 42, 2, 1, 42, 42]
#>>> lst.count(42)
#3
#>>> lst.count(2)
#2


# Вариант 7
Mi_list = ["qwe", "asd", "zxc", "qwe", "ertqwe", "qwe"] #, ищем: "qwe", ответ: 3
Mi_list1 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"] #, ищем: "йцу", ответ: 5
Mi_list2 = ["йцу", "фыв", "ячс", "цук", "йцукен"] #, ищем: "йцу", ответ: -1
Mi_list3 = ["123", "234", 123, "567"] #, ищем: "123", ответ: -1
Mi_list4 = [] #, ищем: "123", ответ: -1
b = "qwe" 
b1 = "йцу"
b2 = "йцу"
b3 = "123"
b4 = 123
def find_seconf(spisok, stroka):
    if spisok.count(stroka) > 1: # Метод подсчитывает количество вхождений повторящегося элемента stroka в списке spisok 
         # spisok - список, stroka - элемент списка с индексом который мы считаем
        return (stroka, spisok.index(stroka, spisok.index(stroka) + 1)) # в списке используем метод индекс, 
        # который принимает строку в себя, он принимает стартовый и конечный индекс где ищет и возвращает в ответ индекс
    return "-1"

print(find_seconf(Mi_list, b))
print(find_seconf(Mi_list1, b1))
print(find_seconf(Mi_list2, b2))
print(find_seconf(Mi_list3, b3))
print(find_seconf(Mi_list4, b4))
'''метод index - это метод, который принимает строку в себя, он еще принимат стартовый и конечный индекс 
откуда будет искать, и возвращает в ответе индекс'''


# Вариант 8

Mb_list = ["qwe", "asd", "zxc", "qwe", "ertqwe", "qwe"] #, ищем: "qwe", ответ: 3
Mb_list1 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"] #, ищем: "йцу", ответ: 5
Mb_list2 = ["йцу", "фыв", "ячс", "цук", "йцукен"] #, ищем: "йцу", ответ: -1
Mb_list3 = ["123", "234", 123, "567"] #, ищем: "123", ответ: -1
Mb_list4 = [] #, ищем: "123", ответ: -1
v = "qwe" 
v1 = "йцу"
v2 = "йцу"
v3 = "123"
v4 = 123


def strings(val, l):
    if not val in l: # если нет ключа в списке то возвращаем
        return -1
    start = l.index(val) # мы берем стартовый индекс
    return (val, l[start+1:].index(val) + 1 if val in l[start +1:] else -1) 
''' мы проверяем индекс у среза списка # список[каждый элемент строки + 1 и : - означает всю строку] + 1 следущий элемент
    стартуя с стартового индекса + 1 -> l[start+1:].index(val) <- и прибавляем к нему единицу
    если у нас ключ присутствует в срезе списка от стартого индекса +1 и до конца -> if val in l[start +1:] <-
    иначе возвращаем -1 '''

print(strings(v, Mb_list))
print(strings(v1, Mb_list1))
print(strings(v2, Mb_list2))
print(strings(v3, Mb_list3))
print(strings(v4, Mb_list4))
    
