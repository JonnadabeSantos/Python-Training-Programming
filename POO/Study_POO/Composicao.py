class Cliente:
    def __init__( self, nome, idade ) -> None:
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco( self, cidade, estado ):
        self.enderecos.append( Endereco( cidade, estado ) ) # append recebe um objeto ( a class ), Endereco necessita instanciar 2 atributos, por isso append parece ter "recebido" mais de um "atributo" 

    def lista_enderecos( self ):
        for endereco in self.enderecos:
            print( endereco.cidade, endereco.estado ) # ^>


class Endereco:
    def __init__( self, cidade, estado ):
        self.cidade = cidade # ^>
        self.estado = estado # ^>


c1 = Cliente( 'Luiz', 32 )
print( c1.nome )
c1.insere_endereco( 'Belo Horizonte', 'MG' )
c1.lista_enderecos()
print()

c2 = Cliente( 'Maria', 24 )
print( c2.nome )
c2.insere_endereco( 'Salvador', 'BA' )
c2.insere_endereco( 'Rio de Janeiro', 'RJ' )
print()

c3 = Cliente( 'Jão', 19 )
c3.insere_endereco( 'São Paulo', 'SP')
print( c3.nome )
c3.lista_enderecos()
print()

