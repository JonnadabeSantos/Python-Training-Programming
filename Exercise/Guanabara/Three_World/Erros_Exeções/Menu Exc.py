from Data_science.save_dados import cadastrar, listar, sair

linha = '-' * 40
princ = 'MENU PRINCIPAL'.center(40)

menu = f'''
{linha}
{princ}
{linha}
01 Ver Cadastrados
02 Novo Cadastro
03 Sair

'''

while True:
    try:
        opc = int(input(f'{menu}'))
        if 3 >= opc > 0:
            break
        else:
            print('x')
           

    except(ValueError):
        print('\033[31m ERROR ! Digite um valor válido !\033[m')
 

if opc == 1:
  
    listar()
elif opc == 2:
    cadastrar()
elif opc == 3:
    sair()

else:
    print('r')
