# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# Примеры:

# 5, 25 -> да
# 4, 16 -> да
# 25, 5 -> да
# 8,9 -> нет


num1 = int(input('Введите 1 число \n'))
num2 = int(input('Введите 2 число \n'))
if num1**2 == num2 or num2**2 == num1:
    print(f' одно из двух чисел является квадратом другово')
else:
    print(f' не одно число не являектся квадратом другово')

'''варианты как выводить строки '''
a = 5 
s = f' a = {a}'
s = f' a = {a**2}'
f' a = {a**2}'
'''1 варпиант'''
s = 'a = {}'.format(a) # передаем аргумент позиционно
'''2 варпиант'''
s = 'a = {var}'.format(var = a) # именованно передаем аргумент
'''3 варпиант'''
'a = %d %s' % (a, 'wsefwefrw')



# first = int(input('Введите первое число \n'))
# second = int(input('Введите второе число \n'))
# if (first * first == second):
#     print(f'второе число {second} квадрат первое {first}')
# elif (first * first != second):
#     print(f'второе число {second} не квадрат первое {first}')
# else: # или просто else и то и то правильно
#     print(f'второе число {second} не квадрат первое {first}')

'''
1) Не писать код, нужно постоянно писать код
2) Распыляться, выбрать язык и изучать его глубоко
3) Нетерпение, писать код самому, не копипастить
4) Слишком глубоко разбираться, не нужно копаться слишком глубоко, из языка в математику и от туда я яденную физику
5) Боязнь общения, лучше если не получается попросить совета у своих сокурсников, 
   Правильный подход это подумать и спросить то что тебе непонятно
6) Не доводить работу до конца, все нужно довести до конца обязательно, до мельчайши деталей
7) Не искать работу, когда вполне готов.Как только научился и пошел работать.Не ждать пока выучишь все языки и инструменты
   Когда чистаешь описание вакансий и 8 из 10 фреймворков знаешь , тогда можно идти работаит

    9 советов новичку
   1) pep8 изучать, это стандарты в коде, чистый оптимизированный код, использовать линтеры, они все найдут и покажут где улучшить
   2) интерактивные курсы неплохое обучение
   3) конспектируйте материал
   4) используйте всю мощь языка, нужно знать сильные стороны, эффективынй и короткий код
   5) испольдзуйте pypi по максимуму, репозиторий pypi готовые модули, готовые решения и комьюнити, находить и применять
   6) развитие через боль - ставить сложные задачи и решать их как угодно, пусть неправильнои неэффективно, зато опыт бесценный
   7) гугл наше все, учимся гуглить, у питона огромное камьюнити, ответы на 99% уже есть
   8) научись задавать вопросы, правильно задавай вопрос и не копипастить код в тело поста
   9) не бойся делать ошибки!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Эксперт это тот кто уже допустил все возможные ошибки

'''