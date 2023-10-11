from Class_People import People

def welcome(msg):
    print('-' * 40)
    print(msg.center(40))
    print('-' * 40)


welcome('Welcome a trainer POO')

name = input('what your name ?: ')
idade = int(input('What your years old?: '))
altura = float(input('what your tall ?: '))
trabalho = input('What is your work ?: ')
sexo = input('Do you Man or Woman ?: ')

p1 = People(name, idade, altura, trabalho, sexo)

welcome('Main Menu')

MenuLista = '''
1 - Falar
2 - Comer
3 - andar
'''
while True:
    select = int(input(f'{MenuLista}Select opction: '))

    print()
    if select == 1:
        p1.falar(input('Talk about the topic: '))

    elif select == 2:
        p1.comer(input('What do you want to eat: '))

    elif select == 3:
        p1.a