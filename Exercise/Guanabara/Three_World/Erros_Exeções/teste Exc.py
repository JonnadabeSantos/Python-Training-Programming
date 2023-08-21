# def arquivoExiste(nome):
#     try:        
#         ar = open(nome,'rt') # 'rt vai ler um arquivo de texto 
#         ar.close() # fecha o arquivo
#     except FileNotFoundError: # Arquivo não encontrado
#         return False
#     else:
#         return True
    

# arq = 'homeoffice.txt'
# if arquivoExiste(arq):
#     print('Aquivo encontrado com sucesso!')
# else:
#     print('Arquivo não encontrado! ')

with open('test.txt') as meuArquivo:
    cola = meuArquivo.readlines()
    print(cola)