def notacomplex(note):
    while True:
        turma = dict()
        aluno = list()
        large = small = note
        cont = total = 0
        while True:
                        
            if note > large:
                large = note
            elif note < small:
                small = note
                    
            aluno.append(note)
            cont += 1
            total += note
            while True:
                new = input('Do you want to enter a new note [ Y/N ]?: ')
                if new in 'YyNn':
                    if new in 'Yy':
                        note = float(input('Type New Note: '))
                    break
                else:
                    print('\nError! Type [ Y ou N ]: ')

            if new in 'Nn':
                break
        
        turma['Total'] = cont
        turma['Maior'] = large
        turma['Menor'] = small
        turma['Média'] = total / cont

        print( '-' * 40 )
        print(turma)
        while True:
            perg = input('Do you want to report a new registration? [ Y / N ]: ')
            if perg in 'YyNn':
                if perg in 'Yy':
                    note = float(input('Type new note: '))
                break

        if perg in 'Nn':
            break

        

user = float(input('Type Note: '))
notacomplex(user)