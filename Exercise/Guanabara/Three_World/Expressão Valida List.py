exp = input('TYpe expression: ')
pilha = []

for simb in exp:
    if simb == '(':
        pilha.append('(')
    
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta válida !')
else:
    print('Sua expressão não esta válida !')

    