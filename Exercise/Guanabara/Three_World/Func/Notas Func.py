def notas(valor):
    while True:
        turma = dict()
        aluno = list()
        new = ' '
        if perg in 'Ss':
            new = 's'

        while True:
            if new in 'Ss':
                othe = float(input('Infome sua nota: '))            
                aluno.append(othe)
            else:
                aluno.append(valor)
            
            while True:
                new = input('Deseja informar outra nota [S/N] ?: ')
                if new in 'SsNn':
                    break
            
            if new in 'Nn':
                break
            
        turma['total'] = len(aluno)
        turma['maior'] = max(aluno)
        turma['menor'] = min(aluno)
        turma['média'] = ( sum(aluno) / len(aluno) )

        print( '-' * 40 )
        print(turma)
        perg = input('Deseja cadastrar um novo [S/N] ?: ')
        
        if perg in 'Nn':
            break
        

infor = float(input('Infome sua nota: '))
notas(infor)
