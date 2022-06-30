# 39. Напишите программу, удаляющую из текста все слова содержащие "абв".

'''Сдесь мы удаляем все слова где всстречается любая буква из трех абв'''

txt = 'грибы сушились на веревке на абв улице около дома'
print(f"Исходный текст: {txt}")
def worlds(txt):
    vowels_set = ['а','б','в']
    lst = [i for i in txt.split() if all(chr not in i for chr in vowels_set)]
    return lst
print(f'Результат: {" ".join(worlds(txt))}') # Результат: сушились улице около
print("")


'''2 вариант'''
mu_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
 этого абв текста все вабвс слова, содерабващие содержащие "абв"'
print(f"Исходный текст: {mu_text}")

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)
mu_text = del_some_words(mu_text)
print(f'выходной текст {mu_text}')
print("")


'''3 вариант'''
# txt = input("Введите текст через пробел:\n")
txt = 'грибы сушилисьабв на веревке на абв улице около дома'
print(f"Исходный текст: {txt}")
def print_text(list):
    vowels_set = 'абв'
   
    lst = [i for i in txt.split() if str(vowels_set) not in i]
    return lst
print(f'Результат: {" ".join(print_text(txt))}')

'''Функция chr()
Принимает целое число i и преобразует его в символ c , поэтому возвращает строку символов.
Как перевести символ в число python - https://programka.com.ua/rukovodstvo/klaster/kak-perevesti-simvol-v-chislo-python'''
