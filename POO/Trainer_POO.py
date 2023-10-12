from Class_People import People

def welcome(msg):
    print('-' * 40)
    print(msg.center(40))
    print('-' * 40)



welcome('Welcome a trainer POO')
people_list = []
dictclass = {}

while True:
    dic = {}

    dic['name'] = input('what your name  ')
    dic['year_old'] = int(input('What your years old?: '))
    dic['height'] = float(input('what your tall ?: '))
    dic['work'] = input('What is your work ?: ')
    dic['sex'] = input('Do you Man or Woman ?: ')

    people_list.append(dic.copy())
    new_people = input('\nDo you want register again ?: ')

    if new_people in 'Nn':
        for ind in range(0, len(people_list)):
            Name = people_list[ind]['name']
            Year_old = people_list[ind]['year_old']
            Height = people_list[ind]['height']
            Work = people_list[ind]['work']
            Sex = people_list[ind]['sex']
            
            dictclass[Name] = People(Name, Year_old, Height, Work, Sex)         

    
        while True:      
    
            welcome('Select People')

            cont = 1
            for k in dictclass.keys():
                print(f'{cont} - {k}')
                cont += 1
            
            select = int(input('Select People: '))
            welcome(f'You select {people_list[select -1]["name"]}')
            # user = dictclass[people_list[select -1]['name']]
            
            
            while True:

                MenuLista = ['Speak', 'Eat', 'Walk', 'Stop walk', 'Stop eat', 'Stop speak ']
                print()
                for i, x in enumerate( MenuLista ):
                    print(f'{i +1} - {x}')

                Menu_select = int(input(f'Select opction: '))

                print()
                if Menu_select == 1:
                    dictclass[people_list[select -1]['name']].Speak(input('Talk about the topic: '))

                elif Menu_select == 2:
                    dictclass[people_list[select -1]['name']].Eat(input('What do you want to eat: '))

                elif Menu_select == 3:
                    dictclass[people_list[select -1]['name']].Walk()

                elif Menu_select == 4:
                    dictclass[people_list[select -1]['name']].StopWalk()

                elif Menu_select == 5:
                    dictclass[people_list[select -1]['name']].StopEat()

                elif Menu_select == 6:
                    dictclass[people_list[select -1]['name']].StopSpeak()

                else:
                    break
            
            new_people = input('Do you want to register again [Y/N] ?: ')
            if new_people in 'Nn':
                break
    
        break


           

            

