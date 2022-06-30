# Запись данных в файл Task24_file.txt

# with open('Task24_file.txt','w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')
colors = ['red', 'green', 'blue']
data = open('E:\Programming\Visual_Studio_Code\Python_seminars\Seminar3\Task24_file.txt', 'w') #сдесь указываем режим, в котором будем работать
data.writelines(colors) # разделителей не будет
data.close()

path = 'Task24_file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()


#Словари
colors = {  
    'bla-bla': 100,
    101 : 'ключ'
}
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

print(get_key(colors, 100))

'''Метод items() ------------ https://pythonru.com/osnovy/python-dict
Этот метод возвращает итерируемый объект. Такой объект содержит пары ключ-значение для словаря 
по аналогии с кортежами в списке. Метод используется, когда нужно перебрать значения словаря.

Этот метод нужно вызывать вместе со словарем, как в примере ниже:

dict_sample = {
  "Company": "Toyota", 
  "model": "Premio", 
  "year": 2012 
} 

for k, v in dict_sample.items(): 
    print(k, v)'''

'''
Вы можете использовать распаковку кортежей для перебора ключей и значений словаря. 
Для этого вам просто нужно распаковать элементы каждого элемента в две разные переменные, 
представляющие ключ и значение:

>>> for key, value in a_dict.items():
...     print(key, '->', value)
...
color -> blue
fruit -> apple
pet -> dog

Здесь, переменные key и value в заголовке вашего цикла for распаковываются. 
Каждый раз, когда цикл запускается, key будет хранить ключ, а value будет хранить значение элемента, 
который был обработан. Таким образом, у вас будет больше контроля над элементами словаря, 
и вы сможете обрабатывать ключи и значения отдельно.
                https://webdevblog.ru/kak-perebrat-slovar-v-python/

        Варианты
        Итерация по .values()
>>> for key, value in a_dict.items():
...     print(key, '->', value)

>>> for value in a_dict.values():
...     print(value)

    Итерация через .keys()
>>> for key in a_dict.keys():
...     print(key, '->', a_dict[key])

>>> for key in a_dict.keys():
...     print(key)

>>> a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> keys = a_dict.keys()

>>> for key in a_dict.keys():
...     print(key, '->', a_dict[key])
'''