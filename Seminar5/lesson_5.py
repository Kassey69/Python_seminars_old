#В файле находится N натуральных чисел, записанных через пробел. Среди чисел не
# хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

# with open('ex_55_in.txt', 'w') as F_N:
#     F_N.write('1 2 3 5 6 7 8 10')
# numbers = []
# with open('ex_55_in.txt', 'r') as data:
#     for line in data:
#         numbers = [int(number) for number in line.split(' ')]
# result = [numbers[i]-1 for i in range(0, len(numbers)) if numbers[i]-1 != numbers[i-1] and i > 0]
#
# print(f'Выпавшие из последовательности {numbers} элементы: {result}')

# 56. Дан список чисел. Выделить среди них числа, удовлетворяющие условию: следующее больше предыдущего.
# > Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

def find_chain(numbers, chain, start_pos, find_length):
    global result
    if len(chain) == find_length:
        result += [chain[:]]
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
    if len(chain) > 0: chain.pop(-1)


numbers = [1, 5, 2, 3]
chain = []
result = []
print(f'Заданный список: {numbers}')
for i in range(2, len(numbers)):
    find_chain(numbers, chain, 0, i)
print(f'Последовательности удовлетворяющие условию задачи: {result}')

# Дан список чисел. Выделить среди них максимальное количество чисел, удовлетворяющих
# условию предыдущей задачи. > Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]

# def find_chain(numbers, chain, start_pos, find_length):
#     global result
#     global exit
#     if len(chain) == find_length:
#         result = chain[:]
#         exit = True
#         return
#     for i in range(start_pos, len(numbers)):
#         if exit: break
#         if len(chain) < find_length:
#             if len(chain) > 0:
#                 if chain[len(chain) - 1] < numbers[i]:
#                     chain.append(numbers[i])
#                     find_chain(numbers, chain, i, find_length)
#             else:
#                 chain.append(numbers[i])
#                 find_chain(numbers, chain, i, find_length)
#     if len(chain) > 0: chain.pop(-1)
#
# numbers = [1, 5, 2, 3, 4, 6, 1, 7]
# chain = []
# result = []
# exit = False
# print(f'Заданный список: {numbers}')
# for i in range(len(numbers), 1, -1):
#     if exit:
#         break
#     find_chain(numbers, chain, 0, i)
# print(f'Последовательности удовлетворяющие условию задачи: {result}')