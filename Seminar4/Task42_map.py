# пояснение что такое  map

l = [2, 3, 5, 9, 3, 5]

def my_map(f ,i):
    my_list = []
    for el in i:
        my_list.append(f(el))
    return my_list

print(list(my_map(str, l)))

'''map(функция, последовательности)'''