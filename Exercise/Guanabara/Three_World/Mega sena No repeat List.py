from random import randint, shuffle
from time import sleep

listgame = []

print('--' *30)
print(f'Game Mega Sena'.center(50) )
print('--' *30)

user = int(input('\nHow many games do you want?: '))
sleep(0.2)
print('\n','=-=' *5, f'Drawing {user} Games', '=-=' *5,'\n')

for quantidade in range(0,user):
    listgame.clear()
    number = cont = 0
    while True:
        number = randint(1,61)
        if number not in listgame:
            listgame.append(number)
            cont += 1

        if cont == 6:
            break

    sleep(0.4)
    listgame.sort()
    print(f'Game {quantidade+1}: ', listgame)

print('< Good Luck >'.center(40,'='))