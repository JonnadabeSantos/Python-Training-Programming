def notas(valor):
    while True:
        turma = dict()
        aluno = list()

        while True:            
            aluno.append(valor)
            new = input('Deseja informar outra nota [S/N] ?: ')
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
