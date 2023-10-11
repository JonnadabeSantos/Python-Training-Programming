from Class_People import People

def welcome(msg):
    print('-' * 40)
    print(msg.center(40))
    print('-' * 40)


welcome('Welcome a trainer POO')
people_list = []

while True:
    dic = {}

    dic['name'] = input('what your name ?: ')
    dic['year_old'] = int(input('What your years old?: '))
    dic['height'] = float(input('what your tall ?: '))
    dic['work'] = input('What is your work ?: ')
    dic['sex'] = input('Do you Man or Woman ?: ')

    people_list.append(dic.copy())
    print(people_list[0]['name'])

    new_people = input('\nDo you want register again ?: ')
    if new_people in 'Nn':
        break

    for x in range(0, len(new_people)):
        pass
    # p1 = People(name, year_old, height, work, sex)

    # welcome('Main Menu')

    # MenuLista = '''
    # 1 - Speak
    # 2 - Eat
    # 3 - Walk
    # 4 - Stop walk
    # 5 - Stop eat
    # 6 - Stop speak 
    # '''
    # while True:
    #     select = int(input(f'{MenuLista}Select opction: '))

    #     print()
    #     if select == 1:
    #         p1.Speak(input('Talk about the topic: '))

    #     elif select == 2:
    #         p1.Eat(input('What do you want to eat: '))

    #     elif select == 3:
    #         p1.Walk()

    #     elif select == 4:
    #         p1.StopWalk()

    #     elif select == 5:
    #         p1.StopEat()

    #     elif select == 6:
    #         p1.StopSpeak()

    #     else:
    #         break
    
    # new_people = input('Do you want to register again [Y/N] ?: ')
    # if new_people in 'Nn':
    #     break