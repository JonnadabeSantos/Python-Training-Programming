class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome:<9} - {self.matricula} - {self.escola}" # Forma como será printado


def mostrar_valores(*objs): # mostra todos os valores da classe
    for obj in objs:
        print('-')
        print(obj)


aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)

mostrar_valores(aluno_1, aluno_2)

aluno_3 = Estudante("Chappie", 3)
aluno_3.escola = 'ETEpd'

mostrar_valores(aluno_1, aluno_2, aluno_3)

Estudante.escola = "Python" # mundando a Variavel (escola)

aluno_4 = Estudante("Nicolas", 4)
mostrar_valores(aluno_1, aluno_2, aluno_3, aluno_4)
