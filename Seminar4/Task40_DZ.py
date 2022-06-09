# Задание 7.
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#:~:text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%2C%20%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87%D0%B8%D1%81%D0%B5%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8.

# import random
# def fibonach(list):
#     list = [0,1]
#     list2 = [1]
#     fib_sum = 0
#     fib1 = 1
#     fib2 = 1
#     for i in range(n):
#         if i  % 2 != 0:          # проверяес индекс на четность
#             list2[i] = -list2[i] # присваиваем всем числам с нечетным индексам минус
#         list.append(fib2)
#         list2.append(fib2)
#         fib_sum = fib1 + fib2    # вычисляем последовательность фибоначи
#         fib1 = fib2
#         fib2 = fib_sum
#     return list2[::-1] + list    # переворачиваем строку в обратную сторону

# n = int(random.randrange(5, 10))
# print(n)
# print(fibonach(n))


def fib(n: int) -> list: # n должно быть целым числом  и что функция должна возвращать list (-> list)
    if n == 0:
        return[0]
    elif n == 1:
        return [0, 1]
    elif n == 2:
        return [0, 1, 1]

    li = fib(n-1)
    li.append(li[-1] + li[-2]) #вот list  и возвращается тут li.append
    return li
print(fib(9)) #обычный фибоначи через рекурсию

def recursive_fib(n):
    fib_list = fib(n)
    negative_fib_list = []  # пустой отдельный список для негативных чсел фибоначи
    for i in range(1, len(fib_list)):  # проходим цикл от 1 до длины списка
        if i % 2 == 0:  # если индекс списка без остатка делится на 2, проверяес индекс на четность
            # присваиваем всем числам с нечетным индексам минус
            negative_fib_list.append(fib_list[i] * -1)
        else:
            # в противнос случае присваиваем i элемент из списка
            negative_fib_list.append(fib_list[i])
    # переворачиваем полученную строку в обратную сторону
    return negative_fib_list[::-1] + fib_list
    
print(recursive_fib(9))


# import random

# def fibo(n):
#     if n >= 0:
#         idx = range(n+1)
#         x = [0, 1]
#         for k in idx[2:]:
#             x.append(x[k-1] + x[k-2])
#         return x[n]
#     else:
#         n = -(n-1)
#         idx = range(n+1)
#         x = [1, 0]
#         for k in idx[2:]:
#             x.append(x[k-2] - x[k-1])
#         x.reverse()
#     return x[0]


# for i in range(-8, 9):
#     print( fibo(i), end=" ")

# n = random.randrange(2,10) #задает рандомное количесво чисел в диапазоне от 2 до 10
# list = []
# for i in range(n):
#     list.append(random.randint(1, n+1)) # заполняет числа рандомными значениями
#     if i  % 2 != 0:
#         list[i] = -i
# print(list)
