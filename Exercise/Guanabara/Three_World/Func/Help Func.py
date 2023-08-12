from time import sleep

def linha(mesg):
    if mesg in 'sair':
        text = 'Até Logo !'
        print( f'~' * ( len(text) + 4 ) )
        print(text.center( len(text) + 4 ))
        print( f'~' * ( len(text) + 4 ) )
    else:
        text = f'Acessando o Manual do comando >>  "{mesg}" '
        print( f'~' * ( len(text) + 4 ) )
        print(text.center( len(text) + 4 ))
        print( f'~' * ( len(text) + 4 ) )

def instruction(ajuda):
    help(ajuda)
   
   



while True:
    user = input('Função, Biblioteca ou Sair: ')
    if user in 'sair':
        linha(user)        
        break
    else:
        linha(user)
        sleep( 1 )
        print(instruction(user))

