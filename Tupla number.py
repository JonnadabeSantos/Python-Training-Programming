number = ( 'Zero', 'One', 'Two', 'Three', 'For', 'Five', 'Sex', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Forteen', 'Fiveteen', 'Sixteen', 'Seventeen', 'eighteen', 'Nineteen', 'Twenty' )

while True:
    index = input('Type number [0 - 20]: ')
    if index.isdigit():
        numero = int(index)
        if 0 <= numero <= 20:
            print('!')    
            break

        else:
            print('\nType number [0 - 20] please!')    
    else:
        print('type number !')    
