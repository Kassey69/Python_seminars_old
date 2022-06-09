# 35.
# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

# A = '1 2 3 5 6 7 8 10'
# A[4] - 1 = A[]


lists = '1 2 3 5 6 7 8 10'
# My_list = [int(x) for x in list.split()]
My_list = list(map(int, lists.split()))


def find_number(My_list):
    My_list1 = set(My_list) # основной список
    temp_list = set(list(range(My_list[0], My_list[-1]+1))) # созданный список всех элементов
    res = temp_list - My_list1 # находим недостающие числа
    return f'Список: {temp_list}', f'Список2:{My_list}', f'Результат: {sorted(res)}' 

print(find_number(My_list))





# def find_number(My_list):
#     result = []
#     for i in range(len(My_list) - 1):
#         if My_list[i + 1] - My_list[i] > 1:
#             result.append(My_list[i] + 1)
#     return result

# print (find_number(My_list))