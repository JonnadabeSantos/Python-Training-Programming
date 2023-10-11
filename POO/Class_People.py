from datetime import datetime

class People: 
    corrent_year = datetime.now().year

    def __init__(self, nome, idade, altura, trabalho, sexo, falando=False, comendo=False, andando=False,):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.trabalho = trabalho
        self.sexo = sexo
        self.falando = falando
        self.comendo = comendo
        self.anando = andando
    


    def comer(self, alimento):
         if self.comendo:
            print(f'{self.nome} já esta comendo.')
            return
         if self.falando:
             print(f'{self.nome} Não pode comer falando !')
             return

         print(f'{self.nome} está comendo {alimento}')
         self.comendo = True


    def ParaComer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        
        print(f'{self.nome} stopped eating !')
        self.comendo = False



    def falar(self, assunto):
        if self.comendo:
            print(f"{self.nome} Can't talk while eating.")
            return
        if self.falando:
            print(f'{self.nome} Already talking.')

        print(f'{self.nome} Is talking about {assunto}')
        self.falando = True

    def PararFalar(self):
        if not self.falando:
            print(f'{self.nome} Not talking !')
            return
        
        print(f'{self.nome} Stopped talking !')
        self.falando = False

    def Andar(self):
        if self.anando:
            print('You are already walking: ')

    def Get_corrent_year(self):
        return self.corrent_year - self.idade