class People:

    def __init__(self, nome, idade, falando=False, comendo=False):
        self.nome = nome
        self.idade = idade
        self.falando = falando
        self.comendo = comendo
    


    def comer(self, alimento):
         if self.comendo:
            print(f'{self.nome} já esta comendo.')
            return

         print(f'{self.nome} está comendo {alimento}')
         self.comendo = True


    def ParaComer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        
        print(f'{self.nome} parou de comer !')
        self.comendo = False



    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} Não pode falar comendo.')
            return
        if self.falando:
            print(f'{self.nome} Já está falando.')

        print(f'{self.nome} Está falando sobre {assunto}')
        self.falando = True

    def PararFalar(self):
        if not self.falando:
            print(f'{self.nome} Não está falando !')
            return
        
        print(f'{self.nome} parou de falar !')
        self.falando = False
