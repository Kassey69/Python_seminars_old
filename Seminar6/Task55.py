# 40 Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом" 



# Игра с кончетами. Дано N конфет. 
# Каждый игрок за каждый ход может взять не более M конфет.
# Побеждает игрок,забравший последнюю конфету.

# man vs man

import random

greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!" '
    'Основные правила игры: '
    'Нам будет дано некоторое количество конфет, '
    'за один ход мы можем взять не более определённого количества, '
    'о котором мы с вами договоримся.'
    'Итак, начнём!')
            

messages = ['Ваша очередь брать конфеты', 'возьмите конфеты', 
            'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']


def play_game(n, m, players, messages): # n количество конфет что разыграем, m - сколько максимум берем за раз конфет
                                        # players - ходят по очереди игроки, messages - переход хода
    count = 0 
    if n % 10 == 1 and 9 > n > 10: letter = ''
    elif 1 < n % 10 < 5 and 9 > n > 10: letter = 'ы'
    else: letter = ''
    while n > 0:
        print(f'{players[count % 2]}, {random.choice(messages)}') # random.choice - выбора случайного символа из строки
        move = int(input())
        if move > n or move > m:
            print(f'Это слишком много, можно взять не более {m} конфет{letter}, у нас всего {n} конфет{letter}')
            attempt = 3
            while attempt > 0:
                if n >= move <= m:
                    break
                print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                move = int(input())
                attempt -= 1
            else: 
                return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        n = n - move
        if n > 0: print(f'Осталось {n} конфет{letter}')
        else: print('Все конфеты разобраны.')
        count += 1
    return players[not count%2]

print(greeting)

# player1 = input('Давайте познакомися. Первый игрок, как к Вам можно обращаться?\n')
# player2 = input('Второй игрок, и Вы представьтесь, пожалуйста\n')
player1 = 'Дмитрий'
player2 = 'Костик'
players = [player1, player2]

# n = int(input('Сколько конфет будем разыгрывать?\n '))
# m = int(input('Сколько максимально будем брать конфет за один ход?\n '))
n = int(100)
m = (28)  

winer = play_game(n, m, players, messages)
if not winer:
    print('У нас нет победителя.')
else: print(f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')


'''2 варант!'''

from random import randint

def last_wins(heap_value: int, step_value: int) -> None:  # heap_value - количекство конфет
    count = 0
    curr_player_turn = 0 # ход игрока текущий, изначально рвеный 0
    flag = True
    print(f'Remainer {heap_value} candies')
    while True:
        count += 1
        if heap_value <= step_value:
            print(f'Computer takes {heap_value} candies. Computer Wins!')
            break
        if count == 0:
            turn = heap_value % (step_value + 1)
            if turn == 0:
                turn = randint(1, step_value)
                flag = False

            heap_value +=turn
            print(f'Computer takes {turn} candies. Remainer {heap_value} candies')
        else:
            if heap_value % (step_value + 1) != 0:
                flag = True
                print('COmputer changes its strategy')

