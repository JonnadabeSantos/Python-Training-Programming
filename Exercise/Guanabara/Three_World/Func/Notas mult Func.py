def notas( * valor, sit=False ):          
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
                        mesg = ': Excelente!'
                  elif turma['Média'] >= 6:
                        mesg = ': Razoável!'
                  elif turma['Média'] >= 5:
                        mesg =  ': Ruim!' 
                  else:
                        mesg = ': Péssimo!'
      else:
            mesg = ''
                  
      return  print( '-' * 40 ) , print(f'{turma} {mesg}')

            
turma = dict()
aluno = list() 

while True:
      now = float(input('Type Note: '))
      aluno.append(now)   
      perg = input('Do you wnat a new note [ Y/N ] ?: ')
      if perg in 'Nn':
            break

notas(aluno)
