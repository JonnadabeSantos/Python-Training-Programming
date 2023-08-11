def notas(valor):
    while True:
        turma = dict()
        aluno = list()
       

        while True:    
            aluno.append(valor)            
            while True:
                new = input('Deseja informar outra nota [S/N] ?: ')
                if new in 'SsNn':
                    if new in 'Ss':
                        valor = float(input('Infome sua nota: $ '))
                    break
                else:
                    print('\nERROR ! Informe Sim ou Não: ')
            
            if new in 'Nn':
                break
            
        turma['total'] = len(aluno)
        turma['maior'] = max(aluno)
        turma['menor'] = min(aluno)
        turma['média'] = ( sum(aluno) / len(aluno) )

        print( '-' * 40 )
        print(turma)
        while True:
            perg = input('Deseja cadastrar um novo [S/N] ?: ')
            if perg in 'Ss':
                valor = float(input('Infome sua nota: @ '))
                break
            elif perg in 'Nn':
                break
            else:         
                print('\nERROR ! Informe Sim ou Não: ')
        
        if perg in 'Nn':
            break
            

infor = float(input('Infome sua nota: '))
notas(infor)
