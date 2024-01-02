from datetime import date
from random import randint
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
        
    @staticmethod
    def id_CODE():
        return randint( 1000, 9999 )
    

print(Pessoa.id_CODE())
senha_jon = Pessoa.id_CODE()
senha_ny = Pessoa.id_CODE()
print()
print(senha_jon)
print()
print(senha_ny)