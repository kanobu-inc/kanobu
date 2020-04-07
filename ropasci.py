import random     # для бота
import time       # для эффекта выбора ботом числа

print('КАМЕНЬ-НОЖНИЦЫ-БУМАГА')

print('---------------------')
print('------НАЧАТЬ(1)------')
print('---------------------')

q = int(input())

while q == 1:    # начало игры

    print('---------------------')
    print('------КАМЕНЬ(1)------')
    print('-----НОЖНИЦЫ(2)------')
    print('------БУМАГА(3)------')
    print('---------------------')

    player = int(input('Выбор: '))   # выбор игрока
    print('BOT выбирает...')
    time.sleep(2)
    bot = random.randint(1, 3)       # "выбор" бота

    if bot == 1 and player == 3:
     print('У бота был камень. Вы победили!')
    if bot == 1 and player == 2:
     print('У бота был камень. Вы проиграли!')
    if bot == 1 and player == 1:
     print('У бота был камень. Ничья!')

    if bot == 2 and player == 3:
     print('У бота были ножницы. Вы проиграли!')
    if bot == 2 and player == 2:
     print('У бота были ножницы. Ничья!')
    if bot == 2 and player == 1:
     print('У бота были ножницы. Вы выиграли!')

    if bot == 3 and player == 3:
     print('У бота была бумага. Ничья!')
    if bot == 3 and player == 2:
     print('У бота была бумага. Вы выиграли!')
    if bot == 3 and player == 1:
     print('У бота была бумага. Вы проиграли!')

    print('Играть дальше?') # повторение игры
    print('1 ДА')
    print('2 HET')

    e = int(input(''))
    
    if e >= 2:
        break