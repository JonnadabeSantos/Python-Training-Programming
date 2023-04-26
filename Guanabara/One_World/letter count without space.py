nome = str(input('Digite seu nome: ')).strip()

print('Seu nome te ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras')

# Or

print('Your fist name have {} latters'.format(nome.find(' ')))

# The (name.find(' ') will count how many letters there are up to the first space