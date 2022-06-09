# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
''' lambda  все заменило'''
# def to_bool(x): ''' lambda  все заменило'''
#     if x == 0:
#         return False
#     return True
'''---------------------'''

def Ex2():
    # ¬(X ⋁ Y ) = ¬X ⋀ ¬Y 
    to_bool = lambda e: e != 0 # заменила верзние строки
    for ix in range(2):
        for iy in range(2):
            x = to_bool(ix)
            y = to_bool(iy)
            if not(not (x or y) == (not(x) and not(y))):
                return False
    return True  

if Ex2():
    print('Все ок')  
else:
    print('Все не ок')



















