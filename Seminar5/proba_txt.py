# Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.

# Создаем рандомное значение для 2-х многочленов)
from random import randint
def rand(num):    
    num = randint(1,10)
    return num

# Создаем 2 многочлена)
def polynomial(k):
    Mylist = ''
    for i in range(k, -1, -1):  # создаем многочлен с диапазоном от к до -1 ( -1 для  условия i == 0 ) с шагом -1
        a =  str(randint(0,100))
        if a == 0 or a == 1:
            a = random.randint(2,100) 
        if i == 1:
           Mylist += str(a) + '*x' + ' + ' # у нас идет цикл, поэтому += мы результаты складываем
        elif i == 0:
            Mylist += str(a)
        else:
            Mylist += str(a) + '*x^' + str(i) + ' + '
    return "".join(map(str, Mylist)) + ' = 0'
num = []
file1 = polynomial(rand(num))
file2 = polynomial(rand(num))


with open('51_Polynomial.txt', 'w') as data: # ну а тут открываем файл и принудительно записываем в него
    data.write(file1)
with open('52_Polynomial.txt', 'w') as data: # ну а тут открываем файл и принудительно записываем в него
    data.write(file2)


file1 = '51_Polynomial.txt'
file2 = '52_Polynomial.txt'

def read_pol(file):
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol

import itertools
import re

# Получение списка кортежей каждого (<коэффициент>, <степень>)
def convert_pol(pol):
    pol = pol.replace('= 0', '')
    pol = re.sub("[*|^| ]", " ", pol).split('+')
    pol = [char.split(' ') for char in pol]
    pol = [[x for x in list if x] for list in pol]
    for i in pol:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
    return pol

# Получение списка кортежей суммы (<коэф1 + коэф2>, <степень>)     
def poly_add(x, y):
    cartage = []
    # for i in range(len(x)):
    # for j in range(len(y)):
    i=0
    j=0
    while i<len(x) and j<len(y):
            if (x[i][1]) == (y[j][1]):
                cartage.append(x[i][0] + y[j][0])
                i=i+1
                j=j+1
            elif x[i][1]>y[j][1]:
                cartage.append((x[i][0]))
                i=i+1
            elif x[i][1]<y[j][1]:
                 cartage.append((y[j][0]))
                 j=j+1
    result = [(cartage[i],i) for i in range(len(cartage)) if cartage[i]!=0]
    # print(res)
    return result 

# Составление итогового многочлена
def result_polynomial(cartage):
    My_polynomial = ''
    for i in range(len(cartage)):
        i = cartage[-i-1][1] # перевернули индекс
        a = cartage[-i-1][0] # перевернули число
        if i == 1:
           My_polynomial += str(a) + '*x' + ' + ' # e нас идет цикл, поэтому += мы результаты складываем
        elif i == 0:
            My_polynomial += str(a)
        else:
            My_polynomial += (str(a) + '*x^' + str(i) + ' + ')
    return "".join(map(str, My_polynomial)) + ' = 0'


file_sum = '54_Polynomial.txt'

def write_to_file(file, pol):
    with open(file, 'w') as data:
        data.write(pol)
        
# f1 =  open(file1) 
# pol1 = f1.read()
# print((pol1))
# f2 =  open(file2) 
# pol2 = f2.read()
# print((pol2))

h1 = convert_pol(read_pol(file1))
h2 = convert_pol(read_pol(file2))
My_polynomial = result_polynomial(poly_add(h1, h2))
print(read_pol(file1))
print(read_pol(file2))
print(My_polynomial) 






'''            18*x^3 + 55*x^2 + 58*x + 13 = 0
        97*x^4 + 5*x^3 + 70*x^2 + 9*x + 89 = 0'''

from random import randint, random
import itertools
from collections import Counter
import collections
import re


def convert_pol(pol):
    pol = pol.replace('= 0', '')
    pol = re.sub("[*|^| ]", " ", pol).split('+')
    pol = [char.split(' ') for char in pol]
    pol = [[x for x in list if x] for list in pol]
    for i in pol:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
    return pol


def add(p1,p2):
    x = [0]*(max(p1[0][1] + 1 ,p2[0][1])+1) # [0] = max(p1[0][1],p2[0][1])+1 = [5] p1[0][1] = 3    p2[0][1] = 4
# p1[0] = (18, 3)  p1[1] = (55, 2)  p1[2] = (58, 1)  p1[3] = (13, 0)
# певые квадратные скобки показывают сразу два эдемента в скобках p1[0] = (18, 3) 
# вторые квадратные скобки глубже раскрываются- имеют значение только [0] или [1] 18*x^3, первое число это 0, второе 1

# p1[0][1] = 3 это означает что элемент p1[0] это 3 индекс, индексивароние идет с 0, 
# поэтому лучше добавить + 1 в конце уровнения max(p1[0][1] + 1, p2[0][1]) + 1

# p1[2] = (58, 1),  p1[2][0] = 58, а p1[2][1] = 1
    #print(x) # x = [0, 0, 0, 0, 0] - x это созданные пять ячеек для выходного уравнения обнуленные
    # x это ячейка памяти на 5 элементов в джанном варианте, список
    # print(x) # 3
    for i in p1+p2:
        # print(x[i[1]], end=' ')
                            #      0   1    0   1  0   1   0   1      0  1   0  1   0   1   0  1   0   1
        # print(x, end=' ') # i = (18, 3) (55, 2) (58, 1) (13, 0)   (97, 4) (5, 3) (70, 2) (9, 1) (89, 0)
        x[i[1]]+=i[0] # x[]- это ячейки, заполняем их элементами складывая, если там уже что то имеется x[i[1]] = x[i[1]] + i[0] 
        # print(x, end=' ') # x[i[1]] = 18 55 58 13   97 23 125 67 102    i[0] = 18 55 58 13   97 5 70 9 89  
                               #  [i[1]] =  3  2  1  0   4  3   2  1   0     i[1] =  3  2  1  0   4  3  2 1  0
    '''Если в ячейки х добавить i[1] индексы '''
    res =  [(x[i],i) for i in range(len(x)) if x[i]!=0]
    res.sort(key = lambda r: r[1], reverse= True)
    # print(res) # [(97, 4), (23, 3), (125, 2), (67, 1), (102, 0)]
    return res

def get_sum_pol(pol):
    var = ['*x^'] * len(pol)
    coefs = [x[0] for x in pol]
    degrees = [x[1] for x in pol][::-1] # перевернули индекс
    new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
    for x in new_pol:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1': 
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_pol = list(itertools.chain(*new_pol))
    new_pol[-1] = ' = 0'
    return "".join(map(str, new_pol))

# h1 = convert_pol(pol1)
# h2 = convert_pol(pol2)
# s = add(h1, h2)

# b =  get_sum_pol(poly_add(h1, h2))
# print((b))






# def addpoly(p1,p2):
#     i=0
#     su=0
#     j=0
#     c=[]
#     if len(p1)==0:
#         #if p1 empty
#         return p2
#     if len(p2)==0:
#         #if p2 is empty
#         return p1
#     while i<len(p1) and j<len(p2):
#         if int(p1[i][1])==int(p2[j][1]):
#             su=p1[i][0]+p2[j][0]
#             if su !=0:
#                 c.append((su,p1[i][1]))
#             i=i+1
#             j=j+1
#         elif p1[i][1]>p2[j][1]:
#             c.append((p1[i]))
#             i=i+1
#         elif p1[i][1]<p2[j][1]:
#             c.append((p2[j]))
#             j=j+1
#     if p1[i:]!=[]:
#         for k in p1[i:]:
#             c.append(k)
#     if p2[j:]!=[]:
#         for k in p2[j:]:
#             c.append(k)
#     print(c)
#     return c 

# addpoly(pol1,pol2)