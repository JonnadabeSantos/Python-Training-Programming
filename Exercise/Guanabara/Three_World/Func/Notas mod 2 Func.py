def notas( * valor, sit=False ):
    """
    Função para obter resuldado dos alunos

    valor : é os valores recebidos
    site: valor opcional que vai mostrar o resultado
    retorn: o dicionário com todas as informações
    """                
    large = small = cont = total = 0
    for note in valor:
            for ind, tur in enumerate(note):
                  if ind == 0:
                        large = small = tur                       
                  else:                  
                        if tur > large:
                              large = tur                   
                        elif tur < small:
                              small = tur                                               
                  total += tur
                  cont += 1

    turma['Total'] = cont
    turma['Maior'] = large
    turma['Menor'] = small
    turma['Média'] = (total / cont)

    show = input('Do you want to show the situation [ Y/N ]?: ')
    if show in 'Yy':
        sit = True
        if sit:
            if turma['Média'] >= 7:
                turma['situação'] = 'Excelente!'

            elif turma['Média'] >= 6:
                turma['situação'] = 'Razoável!'

            elif turma['Média'] >= 5:
                turma['situação'] =  'Ruim!' 
            else:
                turma['situação'] = 'Péssimo!'

                  
    return turma

            
turma = dict()
aluno = list() 

while True:
      now = float(input('Type Note: '))
      aluno.append(now)   
      perg = input('Do you wnat a new note [ Y/N ] ?: ')
      if perg in 'Nn':
            break

# help(notas)
print(notas(aluno))
