# Пишем "компьютерный вирус". Запросите у пользователя любой текст. 
# Сохраните вторую с начала и третью с конца буквы в отдельные переменные (например a и b). 
# Замените во всём тексте букву из переменной a, на букву из переменной b 
# и выведите зашифрованный текст на экран. Пример до шифровки: 
# "Однажды, в студеную зимнюю пору, я из лесу вышел; был сильный мороз". 
# Пример после шифровки: "Орнажры, в стуреную зимнюю пору, я из лесу вышел; был сильный мороз".


text = list(input(f'Введите текст\n'))
#print(text)
a = (text[1]) 
b = (text[-3]) 
for i in range(len(text)): # len - возвращает количество элементов в контейнере
# range - это последовательность всех элементов, длина в for
    if text[i] == a:
         text[i] = b
    elif text[i] == b:
         text[i] = a
print(' ' .join(text))

# help (range)

