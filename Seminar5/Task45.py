'''lambda функции, map'''

def myPow(x): # название функции и аргумент
    return x * x # возвращаемое значние 

myPow2 = lambda x: x * x

res1 = myPow(2)

res2 = myPow2(2)

li = [1,2,5,3,8,6]
print(li)
li2 = []
for item in li:
    # li2.append(item*item) #тоже самое что и ниже
    li2.append(myPow(item))
print(li2)


res = list(map(myPow, li)) # три строчки выше превращаются в одну li2 = [];   for item in li:;  li2.append(myPow(item))
print(res)


#Упрошщение всего что выше через lambda
res2 = list(map(lambda e: e**2, li)) # функция lambda e: e**2 будет применена к этому набору данных li 
                                    # и результатом будет какой то список lis
print(res2)

# В этом случае красота лямд теряется
f1 = lambda r: r+2 # сначала одно действие применяем
res2 = list(map(lambda e:f1(e)**2, li)) # потом применяем это действие в контексте лямды
print(res2)


'''пример lambda функции списки'''

l = [[1,2,3], [4,5,6],[7,8,9]]
res = list(filter(lambda x: max(x) > 5, l))
print(res)

# СОздать рандомный список в количестве 10 , представляем функцию мар
'''map можно представить как цикл, который к каждому элеенту применяет функцию'''
'''к любому обьекту который мы можем пройти цимклом for мы можем применить функцию map'''

import random
l = []
l2 = [str(random.randint(1, 10)) for i in range(10)] # сдесь вместо чисел строки
for i in l2:
    l.append(int(i)) # сдесь вместо строк меняем на числа
m_obj = map(int, l2) # и получим обьект который содержит какое то количество чисел не строки
print(m_obj, * m_obj)
print(l2) # сдесь вместо чисел строки
print(l) # сдесь числа

''' * означает что мы принимаем  в переменную args неограниченное количество аргументов'''
def f(*args): #''' * означает что мы принимаем  в переменную args неограниченное количество аргументов'''
    print(args, type(args), sep='==>')
    print(*args, type(args), sep='==>')
f(1, 2, 'asa', {'qwq', 'qwqwd'}, {'qwedqw: 1'})

'''kwargs аргументы'''
def f(**kwargs): # две ** мы передаем как именованные аргументы и мы получим по сути словарь
    print(kwargs, type(kwargs), sep='==>')
f(name = 1, integral = 2, string = 'dsfsdf', set = {'qwq', 'qwqwd'}, my_dirt = {'qwedqw: 1'})   

#пример
class A:
    def my_f(self, arg, key=None):
        return arg, key

class B(A): # наследует аргумент А
    def my_f(self, *args, **kwargs):
        res = super(B, self).my_f(*args, **kwargs)

