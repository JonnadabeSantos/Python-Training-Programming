from Data_science.save_dados import *
from Data_science.Files import *

arq = 'cx.txt'
if arquivoExiste(arq):
    print('Aquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado! ')
  
# menu([ 'Ver Cadastrados', 'Novo Cadastro', 'Sair'])

# while True:
#     try:
#         opc = int(input(f'Selecione uma Opção: '))
#         if 3 >= opc > 0:
#             break
#         else:
#             print('x')
           

#     except(ValueError):
#         print('\033[31m ERROR ! Digite um valor válido !\033[m')
 

# if opc == 1:
  
#     listar()
# elif opc == 2:
#     cadastrar()
# elif opc == 3:
#     sair()

# else:
#     print('r')
