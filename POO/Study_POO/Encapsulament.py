class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = { id: nome }
        else:
            self.__dados['clientes'].update( { id: nome } )

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(f'{id} - {nome}')
 
    def apaga_cliente(self, id ):
        del self.__dados['clientes'] [id]

bd = BaseDeDados()
bd.__dados = 'Teste error'
bd.inserir_cliente( 1, 'Belo' )
bd.inserir_cliente( 2, 'Brendo' )
bd.inserir_cliente( 3, 'Beca' )
bd.inserir_cliente( 4, 'Barbara' )
bd.lista_clientes()


print(bd._BaseDeDados__dados) #cod real do meu atributo
print(bd.dados) # GEt de dados encapsulado
