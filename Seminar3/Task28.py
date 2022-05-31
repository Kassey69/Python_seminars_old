# Задача 3.
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Каждая позиция хранится отдельной строкой в файле file.txt.



import random
pos = ('0\n', '3')
data = open('e:/Programming/Visual_Studio_Code/Python_seminars/Seminar3/file.txt', 'w')
data.writelines(pos)
data.close

N = int(input('Введите число\n'))
spisok = []
for i in range(N):
    spisok.append(random.randint(-N, N+1)) 
print(spisok)

data = open('e:/Programming/Visual_Studio_Code/Python_seminars/Seminar3/file.txt', 'r')
proizv = 1
for i in data:
    proizv = proizv * spisok[int(i)]
print(f'{spisok[int(0)]} * {spisok[int(3)]} = {proizv}')        
data.close





