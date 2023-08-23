from Data_science.save_dados import *
from Data_science.Files import *

arq = 'Exercise\Guanabara\Three_World\Erros_Exeções\cx.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
  
  

while True:
    menu([ 'Ver Cadastrados', 'Novo Cadastro', 'Sair'])
    opc = int(input(f'Selecione uma Opção: '))
    if 3 >= opc > 0:
        if opc == 1:
            lerArquivo(arq)
                
        elif opc == 2:
            cabeçalho('NOVO CADASTRO')
            nome = input('Nome-: ')
            idade = int(input('Idade: '))
            cadastrarNovo( arq, nome, idade )

        elif opc == 3:
            sair()
            break
        else:
            print('\033[31m ERROR ! Digite um valor válido !\033[m')
        
           

 



