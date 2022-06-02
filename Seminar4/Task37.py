''' Задание 4.'''
# Программа "Именной фильтр". Напишите функцию, которая принимает на вход список с именами людей 
# и возвращает новый список с именами, которые начинаются на гласную букву. 
# В новом списке имя должно начинаться с прописной (большой) буквы, 
# даже если изначально было написано со строчной(маленькой).
# Пример:

# Введите имена через пробел: Никонор иван Харитон Ульяна яков
# Функция вернула ['Иван', 'Ульяна', 'Яков']


def new_sort(list):
    vowels_set = ['А', 'Е', 'О', 'Э', 'Я', 'И', 'Ю', 'У']
    list2 = []
    for i in list:
        i = i.capitalize() # делает первую букву заглавной 
        if i[0] in vowels_set: # сопоставляем первые буквы 
            list2.append(i) # Метод append() в Python добавляет элемент в конец списка.
             # Если вам нужно добавить элементы списка в другой список (а не в сам список), используйте метод extend().
                                  #  Источник: https://pythonstart.ru/list/append-extend-python                 
    return list2
# Таблица "Функции и методы строк" - https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html
list = ['Никонор', 'иван', 'Харитон', 'Ульяна', 'яков']
print(list, end=' ')
print()
print(new_sort(list))

# 2 вариант

def filter(list):
    list2 = []
    for i in list:
        if i[0] in 'АОУЕИЯ':
            list2.append(i)
    return list2
list = input('Введите имена через пробел:').title().split() # Метод title() возвращает строку с заглавной 
                                                            # первой буквой каждого слова в верхний регистр.
    # Метод split() -  Когда вам нужно разбить строку на подстроки, вы можете использовать метод split().
                            # Источник: https://pythonist.ru/strokovye-metody-split-i-join-v-python/
print('Функция вернула имена:', filter(list))

# 3 вариант
spisok = ['А', 'Е', 'О', 'Э', 'Я', 'И', 'Ю', 'У', 'а', 'е', 'о', 'э', 'я', 'и', 'ю', 'у']
spisok2 = ['Никонор', 'иван', 'Харитон', 'Ульяна', 'яков']
print(spisok2)
for i in spisok2:
    if i[0] not in spisok:
        spisok2.remove(i) # Метод remove() — это встроенный метод, который удаляет первый совпадающий элемент из списка.
                    # Синтаксис: list.remove(element). https://pythonru.com/osnovy/kak-udalit-element-iz-spiska-python
for i in range(len(spisok2)):
    spisok2[i] = spisok2[i].capitalize()
print(spisok2)





# list = ['Никонор', 'иван', 'Харитон', 'Ульяна', 'яков']
# print(list, end=' ')
# print()
# list2 = []
# vowels_set = ['А', 'Е', 'О', 'Э', 'Я', 'И', 'Ю', 'У']
# for i in list:
#     i = i.capitalize()
#     for x in i:
#         if x[0] in vowels_set:
#             list2.append(i)                   
# print(list2)
# Таблица "Функции и методы строк" - https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html
