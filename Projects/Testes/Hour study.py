from datetime import date
from time import sleep

print(title := '=' * 80, '\n')
sleep(1)

option = '''
[01] Python 
[02] Java
[03] Kotlin
[04] C++

'''
print(menu := 'NO WELCOME TO YOUR STUDY HOURS HISTORY !'.center(80))
sleep(2)

while True:
    print()
    language = input(f'{option}Inform the Languege: ')
    if language.isdigit():
        language = int(language)

        if language == 1:
                print('Select language is Python !')
                break
            
    else:
        print('x')    

   
