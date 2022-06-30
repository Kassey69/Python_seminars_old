# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

table = [
    [False, False, False],
    [False, False, True],
    [False, True, False],
    [True, False, False],
    [True, True, False],
    [True, False, True],
    [False, True, True],
    [True, True, True],
]

result = True
for i in table:
    if not (not (i[0] or i[1] or i[2])) == (not i[0] and not i[1] and not i[2]):
        result = False
print(result)

''' lambda  все заменило'''
# def to_bool(x): ''' lambda  все заменило'''
#     if x == 0:
#         return False
#     return True
'''---------------------'''

# def Ex2():
#     # ¬(X ⋁ Y ) = ¬X ⋀ ¬Y 
#     to_bool = lambda e: e != 0 # заменила верзние строки
#     for ix in range(2):
#         for iy in range(2):
#             x = to_bool(ix)
#             y = to_bool(iy)
#             if not(not (x or y) == (not(x) and not(y))):
#                 return False
#     return True  

# if Ex2():
#     print('Все ок')  
# else:
#     print('Все не ок')


import zipfile
import os

dir_path = os.getcwd() # сдесь пишем путиь откуда запускаем файл
files_path = [file_path for file_path in os.listdir(dir_path) if os.path.isfile(file_path)]
zip_path = os.path.join(dir_path, 'new.zip')
# zip_file = zipfile.ZipFile(zip_path, 'w')
# for file_path in files_path:
#     zip_file.write(file_path)
# zip_file.close()
with zipfile.ZipFile(zip_path, 'w') as zip_file:
    for file_path in files_path:
        zip_file.write(file_path)


'''os.listdir(dir_path) - у нас возвращает сордержимое папки, с помощью listdir мы получили последовательность
содержимого папки на верзнем уровне, без вложенности. И мы начинаем по ним итерироваться
files_path = [file_path for file_path in os.listdir(dir_path) if os.path.isfile(file_path)] - 
сдесь мы получаем по сути список, из содержимого папки os.listdir(dir_path) если 
этот элемент является файлом os.path.isfile(file_path) -- os.path.isfile - проверяем является ли он файлом
и так мы набиваем список файлов которые лежат в текущей директории ile_path

затем нам надо прописать путь к нашему зип файлу =  zip_path = os.path.join(dir_path, 'new.zip')
для этого мы с помощью  os.path.join (join объединение) мы обьединяем путь dir_path до нашей папки под названием 'new.zip'
и построится путь

далее создаем zip_file = zipfile.ZipFile(zip_path, 'w') с помощью модуля zipfile и класса ZipFile в который
мы передаем путь до нашего зи пайла zip_path, который создастся автоматически если его нет и w запись и он пишщет
и дальше бгаем по путям этих файлов for file_path in files_path: и передаем методом write(передаем путь к файлу
zip_file.write(file_path) который хотим поместить в зим архив

и так как у нас файл for file_path  открыт то его нужно закрыть zip_file.close()
но если его не закрыть то в виндовсе нельзя будет зайти в директорию с файлом потому что он открыт


менеджер контекста используются для открытия файлов, для открытия соединений например с базой данных
смысл такой
мы пищем  ключевое слово WIth а затем прописываем что мы хотим открыть zipfile.ZipFile(zip_path, 'w')
чтобы это обязательно закрылось и сдесь мы создадим псевданим as zip_file:  и это все поместим в менеджер контекста
и уберем лишнее закоментируем и перенесем'''

















