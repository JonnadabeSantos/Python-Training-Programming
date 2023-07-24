from random import randint, shuffle
from time import sleep
listgame = []
print('--' *30)
print(f'Game Mega Sena'.center(50) )
print('--' *30)

user = int(input('\nHow many games do you want?: '))
sleep(0.2)
print(f'\n','=-=' *5, 'Drawing {user} Games', '=-=' *5,'\n')
for quantidade in range(0,user):
    listgame.clear()
    for game in range(0,6):
        listgame.append(randint(1,61))
    sleep(0.4)
    print(f'Game {quantidade+1}: ', listgame)

print(f'< Good Luck >'.center(40,'=:='))