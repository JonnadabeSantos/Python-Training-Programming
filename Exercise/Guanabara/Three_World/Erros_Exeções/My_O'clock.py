from Data_science.save_dados import *
from Data_science.Files import *

arq = 'Exercise\Guanabara\Three_World\Erros_Exeções\Study_hours.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
  
  

while True:
    menu([ 'Python', 'Java_Script', 'Java', 'C#', 'Sair'])
    opc = int(input(f'Selecione uma Opção: '))
    if 5 >= opc > 0:
        if opc == 1:
            lerArquivo(arq)
                
        elif opc == 2:
            cabeçalho(F'ADIÇÃO DE HORAS EM ')
            nome = input('Nome-: ')
            idade = int(input('Idade: '))
            cadastrarNovo( arq, nome, idade )

        elif opc == 5:
            sair()
            break
        else:
            print('\033[31m ERROR ! Digite um valor válido !\033[m')
        
           

 



