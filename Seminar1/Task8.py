# Напишите программу, которая проверит истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y

x = input()
y = input()
if not(x or y) == (not(x) and not(y)):
    print('Выражение истинно')
else:
    print('Выражение ложно')