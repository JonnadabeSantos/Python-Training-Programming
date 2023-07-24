characters = ('Tranquilo','Bonito','Facinante','Otimizado','Improvisado','Melancolia','Jesus')

for text in characters:
    print(f'\nNa palavra {text.upper()} temos: ', end='')
    
    for letra in text:
        if letra in 'aeiou':
            print(f'{letra}', end=' ')