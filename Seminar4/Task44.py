# чтобы узнать что представляет из себя итератор - функеция map из этого разряда

class Counter:
    def __init__(self, low, high):
        self.current = low - 1 # self.current это текущее значение равное = минимальному значению - 1
        self.high = high # есть self.high - максимальное значение которое мы передаем
    # В Python наличие пар знаков подчеркивания спереди и сзади в имени метода говорит о том, 
    # что он принадлежит к группе методов перегрузки операторов. https://younglinux.info/oopython/init
    def __iter__(self):
        return self # объект итеракт возвращает самого себя
        # и когда цикл for вызывает __iter__ от последовательно начинает вызывать функцию __next__ 
        # у того что вернет нам функция __iter__
    def __next__(self):
        self.current += 1 # мы значение увекличсиваем на 1 и проверяем
        if self.current < self.high: # если текущее значение меньше чем максимальное мы возвращаем некущее self.current
            return self.current # мы возвращаем некущее self.current
        raise StopIteration # иначе останавливаем цикл

for i in Counter(1, 5):
    print(i)

    # метод _itit__ это метод который вызывается при инициализации класса 
    # и то что мы будем передавать внутрь класса мы можем сдесь прописать, в него, в инит
class Range:
    def __init__(self, high, low=None, step=None): # low=None - необязательный, high обязательный,step=None,self,
        self.current = low - step if low != 0 else 0 - step
        self.high = high # ставим что self.high = high
        self.low = low if low is not None else 0
        self.step = step

    def __iter__(self):
        return self
    
    def __next__(self):
        self.current += self.step 
        if self.current < self.high: 
            return self.current 
        raise StopIteration
    
# for i in Range(low=0, high=10, step=2):
#     print(i)
# print(list(Range(low=0, high=10, step=2)))

i = Range(low=0, high=10, step=2).__iter__()
while True:
    try:
        print(next(i))
    except StopIteration as e: # (as - как) переводится
        print('error', e.args)
        break


class Map:
    def __init__(self, function, iter_obj): # мы принимаем функцию и объект
        self.function = function
        self.iter_obj = iter_obj.__iter__() 

    def __iter__(self): 
        return self  # при итерацуи мы возвращаем
    
    def __next__(self):
        return self.function(next(self.iter_obj)) # мы применили функцию которую передали в class к следующему
                                                  # элементу итерируемой последовательности

l = [1,2,3,4]
for i in Map(str,l):
    print(i, type(i)) # 1 <class 'str'> 2 <class 'str'> 3 <class 'str'> 4 <class 'str'>

print(list(Map(str,l))) # мы применили функцию которую передали в class ['1', '2', '3', '4']
