# Задайте список из целых и вещественных чисел. Отсортируйте его по возрастанию,
# от меньшего к большему и выведите в консоль. Зеркально разверните его и выведите на строке ниже.
# Пример: список -> [1,0.5,15,3.4] Сортировка - > [0.5,1,3.4,15] Разворот - > [15,3.4,1,0.5]

# string = [1, 4, 1.5, 5, False]
# print(string[:: -1])  # развернет список


# list = [1,0.5,15,3.4]
# list.sort() # сортирует все значения по возрастанию
# print(list)
# print()
# print(list[:: -1]) # первое и второе не меняем а последнее изменяет последовательность с конца

list = [1,0.5,15,3.4]
list.sort() # сортирует все значения по возрастанию
print(list)
print()
list.reverse() # обратный список, перевернуть
print(list)

