from Data_science.save_dados import *
from Data_science.Files_2 import *

arq = 'Exercise\Guanabara\Three_World\Erros_Exeções\cx.txt'
if arquivoExiste(arq):
    print('Aquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado! ')
    criarArquivo(arq)
  

