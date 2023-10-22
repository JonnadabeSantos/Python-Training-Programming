from datetime import date

class Pessoa:
    ano_atual = date.today().year
    today = date.today().day

    def __init__(self, nome, idade, data):
        self.nome = nome
        self.idade = idade
        self.data = data

    def get_ano_nascimento(self):
        print(f'Today is {self.today}')
        print(self.ano_atual - self.idade)
        
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade, 26)



# p2 = Pessoa('jon', 32)
# print(p2.idade)
# p2.get_ano_nascimento()
# print()

# p1 = Pessoa.por_ano_nascimento('Luiz', 1985)
# print(p1.idade)
# p1.get_ano_nascimento()


print()
p1 = Pessoa.por_ano_nascimento('Irineu', 1912)
# print(p1.idade)
p1.get_ano_nascimento()
print(p1.data)