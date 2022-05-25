# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений подстроки в строку.

# Пример:

# "Проснувшись однажды утром после беспокойного сна."
# "Проснувшись однажды утром"
# Количество вхождений - 1

text1 = input(f'Введите полную фразу\n')
text2 = input(f'Введите отрезок\n')
text = text1.count(text2) 
print(text)

# Метод count() возвращает количество раз, когда указанный элемент появляется в списке.
# Источник: https://pythonstart.ru/list/count-python