sey = input('Inform Your Sexy: ').strip() .upper() [0]

while sey not in 'MmFf':
    sey = input('Invalid Option! Inform Your Sexy: ').strip() .upper() [0]
print(f'Sexo {sey} Registrado com sucesso!')