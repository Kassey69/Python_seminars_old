# 43.
# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10, 7] => [2, 10]

# from collections import Counter
# some_list = [1, 2, 3, 5, 1, 5, 3, 10, 7]
# c = Counter(some_list)
# res = list(filter(lambda x: c[x] == 1, some_list))
# print(res)
        

myList = [1, 2, 3, 5, 1, 5, 3, 10, 7]
occurrences = []
print(f'Дана последовательность чисел: {myList}')
 
for i in myList:
    count = 0
    for x in myList:
        if x == i: # если назодится одинаковый элемент то 
            count += 1 # присваивается ему count
    occurrences.append(count) # составляем список count
print(occurrences)

duplicates = set()
index = 0
while index < len(myList):
    if occurrences[index] == 1:
        duplicates.add(myList[index])
    index += 1

print(f'уникальных элементы: {duplicates}')

#Источник: https://tonais.ru/list/poisk-unikalnyh-i-povtoryayuschihsya-elementov-v-spiske-python










# import time
# import random

# def unique_elements(list):
#     result_list = [] # с уникальными элементами
#     for i in list: 
#         if i not in result_list: # ищем по списку отсутствующее число
#             result_list.append(i) # если число отсутствует то мы его добавляем
#     return result_list # значение возвращаем

# def unique_elements_by_set(list):
#     #return list(set(list))
#     #return [i for i in set(list)] # set неупорядоченная коллекция уникальных ссылок на обьекты
#     return list(filter(lambda x: list.count(x) == 1, list)) # count вернет количество элементов в последовательности
#     # функция filter берет по одному элементу из нашей последовательгности list(последний) и опрокидывает в lambda x
#     # и проверяем list.count(x) == 1, если вернется истина Trye то значит все правильно нам подходит

# #Тест 1
# tst_list = [1,2,3,5,1,5,3,10]



