from Finac.Dinheiro import moeda

def validar( * xval ):

    if len(xval) > 1:
        lista = []       
        for id, v in enumerate(xval):
            v = str(v)
            if id == 0:
                if ',' in v:
                    v = v.replace(',','.')                            
                    lista.append(v)                                                       
                    print('x')          

                elif '.' in v:                    
                    print('+')
                    v = float(v)
                    lista.append(v)

                elif v.isdigit():                                     
                        lista.append(v)                                                       
                        print('z')
                else:
                    print(f'Error!: "{v}" é um preço inválido * ')
                        
            elif id > 0:
                                 
                if ',' in v:
                    v = v.replace(',','.')
                    print('/')
                    v = float(v)
                    lista.append(int(v))

                elif '.' in v:                    
                    print('+')
                    v = float(v)
                    lista.append(int(v))
                
                elif v.isdigit():
                    lista.append(int(v))                                                       
                    print('kk')
                 
                else:
                    print(f'Error!: "{v}" é um preço inválido /! ')


            else:
                print(f'Error!: "{v}" é um preço inválido +- ')
        
        for ind, inf in enumerate(lista):
             if ind == 0:
                  d1 = float(inf)
                  print('a')
             elif ind == 1:
                  d2 = inf
                  print('b')
             elif ind == 2:
                  d3 = inf
                  print('c')
         
        return moeda.resumo( d1, d2, d3 )   

