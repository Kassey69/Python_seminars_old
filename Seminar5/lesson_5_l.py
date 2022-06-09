#В файле находится N натуральных чисел, записанных через пробел. Среди чисел не
# хватает одного, чтобы выполнялось условие A[i] - 1 = A[-i1]. Найти его.

# Информация по всем флагам
# https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-open/


# with open('ex_55_ingdgfdgdg.txt', 'w+') as F_N:
#     F_N.write('1 2 3 5 6 7 8 10')
#     F_N.seek(0)
#     result = []
#     for line in F_N.readlines():
#         result += [int(i) for i in line.split()]
#     print(result)

# with open('ex_55_in.txt', 'w') as F_N:
#     F_N.write('1 2 3 5 6 7 8 10')
#
# with open('ex_55_in.txt') as F_N:
#     my_list = list(map(int, F_N.read().split()))
#
#
# def find_number(my_list):
#     result = []
#     temp_list = list(range(my_list[0], my_list[-1]+1))
#     return temp_list
#
#
# print(find_number(my_list))


# with open('ex_55_in.txt', 'r') as F_N:
#     l = list(map(int, F_N.read().split(' ')))
# set1 = set(l)
# set2 = set(list(range(l[0], l[len(l)-1]+1)))
#
# print(set1 - set2) # Пусто
# print(set2 - set1) # Результат [1, 5, 2, 3, 4, 6, 1, 7]

# with open('ex_55_in.txt', 'w') as F_N:
#     F_N.write('1 2 3 5 6 7 8 10')
# numbers = []
# with open('ex_55_in.txt', 'r') as data:
#     for line in data:
#         numbers = [int(number) for number in line.split(' ')]
# result = [numbers[i]-1 for i in range(0, len(numbers)) if numbers[i]-1 != numbers[i-1] and i > 0]
#
# print(f'Выпавшие из последовательности {numbers} элементы: {result}')


def find_chain(numbers, chain, start_pos, find_length):
    global r
    if len(chain) == find_length:
        r += [chain[:]]
        chain.pop(-1)
        return
    for i in range(start_pos, len(numbers)):
        if len(chain) < find_length:
            if len(chain) > 0:
                if chain[len(chain) - 1] < numbers[i]:
                    chain.append(numbers[i])
                    find_chain(numbers, chain, i, find_length)
            else:
                chain.append(numbers[i])
                find_chain(numbers, chain, i, find_length)
    if len(chain) > 0:
        chain.pop(-1)


numbers = [1, 5, 2, 3, 4, 6, 1, 7]
chain = []
r = []
for find_length in range(2, len(numbers)):
    find_chain(numbers, chain, 0, find_length)
print(r)