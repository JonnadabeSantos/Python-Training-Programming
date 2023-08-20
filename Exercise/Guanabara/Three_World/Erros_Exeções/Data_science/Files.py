def arquivoExiste(arquivo):
    try:
        ar = open( arquivo, 'rt' ) # 'rt vai ler um arquivo de texto 
        ar.close() # fecha o arquivo
    except FileNotFoundError: # Arquivo não encontrado
        return False
    else:
        return True