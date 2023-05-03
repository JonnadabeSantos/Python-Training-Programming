frase = input('Type text: ').strip() .upper()

# este mecanismo é usado para retirar espaços ou pa adicionar elementos entre em vez dos espaços ===========

latter = frase.split() #divide em block de listas
juntar = '-'.join(latter) # juntar os espaços das palavras

# ==========================================================================================================

inverso = juntar[::-1] # metodo fatiamento
enverso = ''



if inverso == juntar:
    print('Temos um palíndromo!')

else: 
    print('Não temos um palíndromo! Tente novamente !')

#   metodo For !

    refrase = input('Type text: ').strip() .upper()
    reletter = refrase.split()
    rejuntar = ''.join(reletter)
    reinverso = ''
    
    for text in range( len(rejuntar) - 1, -1, -1 ):
        reinverso += rejuntar[text]
    
    
    if reinverso == rejuntar:
        print(f'Temos um palíndromo pos {refrase} é = a {reinverso}')

    else: 
        print(f'Mais uma vez não temos um palíndromo! Infelizmente !')
