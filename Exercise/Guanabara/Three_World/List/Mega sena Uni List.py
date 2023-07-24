from random import randint, shuffle
from time import sleep

listgame = []
temp = []

print('--' *30)
print(f'Game Mega Sena'.center(50) )
print('--' *30)

user = int(input('\nHow many games do you want?: '))


for quantidade in range(0,user):
    temp.clear()
    number = cont = 0
    while True:
        number = randint(1,61)
        if number not in temp:
            temp.append(number)
            cont += 1

        if cont == 6:
            break   
    temp.sort()
    listgame.append(temp[:])

print('\n You List is → ',listgame,'\n')
sleep(0.8)
print('\n','=-=' *5, f'Drawing {user} Games', '=-=' *5,'\n')

for ind, game in enumerate(listgame):
    print(f' Game {ind+1}: {game}')
    sleep(0.8)

print()
print('< Good Luck >'.center(40,'='))