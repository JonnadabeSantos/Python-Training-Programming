from Class_People import People

def welcome(msg):
    print('-' * 40)
    print(msg.center(40))
    print('-' * 40)


welcome('Welcome a trainer POO')

while True:

    name = input('what your name ?: ')
    year_old = int(input('What your years old?: '))
    height = float(input('what your tall ?: '))
    work = input('What is your work ?: ')
    sex = input('Do you Man or Woman ?: ')

    p1 = People(name, year_old, height, work, sex)

    welcome('Main Menu')

    MenuLista = '''
    1 - Speak
    2 - Eat
    3 - Walk
    4 - Stop walk
    5 - Stop eat
    6 - Stop speak 
    '''
    while True:
        select = int(input(f'{MenuLista}Select opction: '))

        print()
        if select == 1:
            p1.Speak(input('Talk about the topic: '))

        elif select == 2:
            p1.Eat(input('What do you want to eat: '))

        elif select == 3:
            p1.Walk()

        elif select == 4:
            p1.StopWalk()

        elif select == 5:
            p1.StopEat()

        elif select == 6:
            p1.StopSpeak()

        else:
            break
    
    new_people = input('Do you want to register again [Y/N] ?: ')
    if new_people in 'Nn':
        break