class peolpe:
    def __init__(self, men, weman, child, animals):
        self.men = men
        self.weman = weman
        self.child = child
        self.anamals = animals


    def buscar(self):
        mainMenu = [f'{key}' for key in self.__dict__.keys()]
        for ind, item in enumerate(mainMenu):
            print(f'{ ind + 1} -- {item}')
    
        try:
            search = int(input(f'select what you want to search [ 1 to {len(mainMenu)}]: '))
        except:
            print('error !')
        else:                 

            if 0 < search <= len(mainMenu):
                if search == 1:
                    for i, p in enumerate(self.men):
                        if i == len(self.men) - 1:
                            print(f'{p}') 
                        else:
                            print(f'{p}', end=' → ') 
                
                elif search == 2:
                    for i, p in enumerate(self.weman):
                            if i == len(self.weman) - 1:
                                print(f'{p}') 
                            else:
                                print(f'{p}', end=' → ')  

                elif search == 3:
                    for i, p in enumerate(self.child):
                        if i == len(self.child) - 1:
                            print(f'{p}') 
                        else:
                            print(f'{p}', end=' → ') 

                elif search == 4:
                    for i, p in enumerate(self.anamals):
                        if i == len(self.anamals) - 1:
                            print(f'{p}')
                        else:
                            print(f'{p}', end=' → ')

            else:
                print(f'Type number between 1 to {len(mainMenu)}')    
   
  
    def __str__(self):
        return f'{self.__class__.__name__}: {", ".join( [ f"{ chave } = { valor }" for chave, valor in self.__dict__.items() ] )}'
        





test = peolpe(['bio','deco','caneco','fio'], ['liza','luiza','miliza','suiça'], ['bilio','sico','zico'], ['ema','max','fred','olaf','betove'])
# test.buscar()
print(test)