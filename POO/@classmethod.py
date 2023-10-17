from datetime import date

class Pessoa:
    ano_atual = date.today().year
    today = date.today().day

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def get_ano_nascimento(self):
        print(f'Today is {self.today}')
        print(self.ano_atual - self.idade)
        

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

p2 = Pessoa('jon', 32)
print(p2.idade)
p2.get_ano_nascimento()
print()

p1 = Pessoa.por_ano_nascimento('Luiz', 1985)
print(p1.idade)
p1.get_ano_nascimento()