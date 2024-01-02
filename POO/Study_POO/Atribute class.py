class A:
    w = 123

    def __init__(self):
        self.w = 352

x = A()
y = A()

# A.w = 'Ui' # altera a var. da class

x.w = 854

print(x.__dict__) # achou e imprimiu a var.(w) na instacia
print(y.__dict__) # não achou a var.(w) 
print(A.__dict__) # nao achou na var. e buscou na Class

print()

print( x.w )
print( y.w )
print( A.w )
