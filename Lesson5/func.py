from random import randint
import time


def InputName(a):
    igrok1 = input('Введите имя 1-го играющего ')
    igrok2 = input('Введите имя 2-го играющего ')
    game(igrok1,igrok2)

def game(a, b):
    score1 = 0
    score2 = 0
    wins1 = 0
    wins2 = 0
    i = 0
    fora=0
    fora=int(input('Введите количество игр:'))
    while fora !=0:
        fora-=1
        print('Раунд ', i + 1)
        print('Кубик бросает', a)
        n1 = randint(1, 6)
        score1 += n1
        time.sleep(0.5)

        print('Выпало:', n1)
        print('Кубик бросает', b)
        n2 = randint(1, 6)
        score2 += n2
        time.sleep(0.5)
        print('Выпало:', n2)
        i += 1
        time.sleep(0.5)

        if n1 > n2:
            print('Выиграл', a, ' ', n1)
            wins1 += 1
        elif n1 < n2:
            print('Выиграл', b, ' ', n2)
            wins2 += 1
        else:
            print('Ничья')
            wins2 += 1
            wins2 += 1
        print('---------------')
    print(' ')
    # Определение результата (3 возможных варианта)
    print('Статистика игры:')
    if score1 > score2:
        print('Выиграл', a, ' Очки:', score1, ' Выйгрышных раундов ', wins1)
    elif n1 < n2:
        print('Выиграл', b, ' Очки:', score2, ' Выйгрышных раундов ', wins2)
    else:
        print('Ничья')