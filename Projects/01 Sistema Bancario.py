cheque_especial = 600
saldo_conta_corrente = 2000
saldo_conta_universitaria = 950



menu_geral = """
[01] Conta Corrente 
[02] Conta Universitária

Selecione o Tipo de conta:"""



menu_conta_corrente = """
[01] Saque:
[02] Depósito:
[03] Saldo:
[04] Saldo Cheque Especial:

Selecione a Operação: """




operacao_principal = "inicie"
while operacao_principal == "inicie":


    operacao_principal = "pare"
    reset_programa = "pare"

    reset_operacao_conta_corrente = "pare"


    conta_corrente = False
    conta_universitaria = False      


# Validação Funcionou ==============================
   
    selecione_conta = input(f'{menu_geral} ')
    if selecione_conta.isdigit():
        selecione_conta = int(selecione_conta)
        
#====================================================

    if selecione_conta == 1:
        conta_corrente = True    

    elif selecione_conta == 2:
        conta_universitaria = True  

    else:
        print("\nNenhuma Conta Selecionada!\n")
        reset_programa = "inicie"



    if conta_corrente:      
      
        print("\nConta Corrente Selecionada! ")
        
        reset_operacao_conta_corrente = "inicie"
        while reset_operacao_conta_corrente == "inicie":
            
# Validação Funcionou =========================================================================================================

            operacao_conta_corrente = input(f'{menu_conta_corrente} ')
            if operacao_conta_corrente.isdigit():
                operacao_conta_corrente = int(operacao_conta_corrente)

#=============================================================================================================================

                
                if operacao_conta_corrente >= 1 and operacao_conta_corrente <= 4:
                    reset_operacao_conta_corrente = "pare"
                  
                if operacao_conta_corrente == 1:
                    print("\nSaque Selecionado!")
                                        
#Validação Funcionou =========================================================================================================
                    
                    reset_saque_conta_corrente = 'inicie'
                    while reset_saque_conta_corrente == 'inicie':
                        
                        saque_conta_corrente = input("Informe o Valor do Saque em sua conta corrente: ")
                        if saque_conta_corrente.isdigit():
                            saque_conta_corrente = int(saque_conta_corrente)
                            
#=============================================================================================================================


                            if saque_conta_corrente > (saldo_conta_corrente + cheque_especial):
                                print("\nSaldo Insuficiênte !")
                                reset_saque_conta_corrente = 'pare'
                                reset_programa = "inicie"
                               


                            elif saque_conta_corrente > saldo_conta_corrente and saque_conta_corrente <= (saldo_conta_corrente + cheque_especial):
                                print("\nVocê está usando",(saque_conta_corrente - saldo_conta_corrente),"do seu Cheque especial deseja continuar? ")
                                reset_saque_conta_corrente = 'pare'
                                
                                reset_sim_ou_nao = "inicie"
                                while reset_sim_ou_nao == "inicie":
                                    continuar_saque = input("Escreva sim ou não: ").lower()
                                                              

                                    if continuar_saque == "sim":
                                        
                                        cheque_especial -= (saque_conta_corrente - saldo_conta_corrente) 
                                        saldo_conta_corrente = 0
                                        
                                        print("\nSaque realizado! seu saldo é",saldo_conta_corrente)                                   
                                        print("O Valor do seu Cheque Especial é",cheque_especial)
                                        reset_sim_ou_nao = "pare"
                                        reset_programa = "inicie"
                                       
                                        
                                    elif continuar_saque == "nao" or continuar_saque == "não":
                                        print("\nSaque Não Realizado !")
                                        reset_sim_ou_nao = "pare"
                                        reset_programa = "inicie"
                                        


                                    else:
                                        print("\nOpção Inválida! ")
                                                       
                                        


                            

                            elif saque_conta_corrente <= saldo_conta_corrente and saque_conta_corrente > 0:
                                saldo_conta_corrente -= saque_conta_corrente
                                print("\nSaque de",saque_conta_corrente,"realizado! seu saldo é",saldo_conta_corrente)
                                reset_saque_conta_corrente = 'pare'
                                reset_programa = "inicie"


                        
                            else:
                                print("\nValor Inválido! ")
                        
                        
                        
                        else:
                            print("\nOpção Inválida! Digite apenas números !")
            

    # Deposito conta corrente
            

                elif operacao_conta_corrente == 2:               
                    
                    print("Depósito Selecionado! \n")
                    deposito_conta_corrente = int(input("Informe o valor do depósito: "))

                    reset_deposito_conta_corrente = "inicie"
                    while reset_deposito_conta_corrente == "inicie":
                        

                        if deposito_conta_corrente > 0:
                            saldo_conta_corrente += deposito_conta_corrente
                            print("\nDepósito de",deposito_conta_corrente,"Realizado! seu saldo é",saldo_conta_corrente)                                                                
                            reset_deposito_conta_corrente = "pare"
                            reset_programa = "inicie"
                    
                        else:
                            print("\nOpção Inválida!")
                            deposito_conta_corrente = int(input("Informe Novamente o valor do depósito: "))

                       

    # Saldo conta corrente

                elif operacao_conta_corrente == 3:
                    print("\nSaldo Selecionado! \n")
                    print("Seu saldo é",saldo_conta_corrente,"\n")
                    reset_programa = "inicie"


    # Saldo Cheque especial

                elif operacao_conta_corrente == 4:
                    print("\nSaldo de Cheque Especial Selecionado! \n")
                    print("Seu saldo em cheque especial é",cheque_especial,"\n")
                    reset_programa = "inicie"
                    
                    
                else:
                    print("\nOperação Inválida!") 
            



    elif conta_universitaria:

        print("Conta Universitária Selecionada! ")

        reset_saq_dep_conta_universitaria = "inicie"
        while reset_saq_dep_conta_universitaria == "inicie":


            print("\nSelecione a Operação:\n[01] Saque:\n[02] Depósito:\n ")
            saq_dep_conta_universitaria = int(input(""))


            
            if saq_dep_conta_universitaria == 1 or saq_dep_conta_universitaria == 2:
                reset_saq_dep_conta_universitaria = "pare"

            if saq_dep_conta_universitaria == 1:
                print("Saque Selecionado!")
                saque_conta_universitaria = int(input("Informe o Valor do Saque em sua Conta: "))

                if saque_conta_universitaria > saldo_conta_universitaria:
                    print("\nSaldo Insuficiênte! ")
                    reset_programa = "inicie"



                elif saque_conta_universitaria <= saldo_conta_universitaria and saque_conta_universitaria > 0:
                    
                    saldo_conta_universitaria -= saque_conta_universitaria
                    print ("\n Saque de",saque_conta_universitaria,"Realizado! seu saldo é",saldo_conta_universitaria)                    
                    reset_programa = "inicie"



                else:
                    print("\nOreção Inválida! uv ")




    #Deposito Conta universitadade


            elif saq_dep_conta_universitaria == 2:
                print("Depósito Selecionado! \n")

                reset_deposito_conta_universitaria = "inicie"
                while reset_deposito_conta_universitaria == "inicie":
                    dep = int(input("Informe o valor do depósito: "))

                    if dep > 0:
                       
                        saldo_conta_universitaria += dep
                        print("\nDepósito de",dep,"Realizado! seu saldo é",saldo_conta_universitaria)
                        reset_deposito_conta_universitaria = "pare"
                        reset_programa = "inicie"
                        
                    
                    else:
                        print("\nOperação Inválida!\n")
                       

            else:
                print("\nOperação Inválida!")   

                            
#reset do programa:


    while reset_programa == "inicie":
       
        print("\nDeseja realizar uma nova operação ?\n[01] Sim\n[02] Não")
        reset_operecao_principal = int(input(""))
    


        if reset_operecao_principal == 1:
            reset_programa = "pare"
            operacao_principal = "inicie"
    
        elif reset_operecao_principal == 2:
            print("\nObrigado Volte Sempre!")
            reset_programa = "pare"
            operacao_principal = "pare"

        else:                      
            reset_operecao_principal = 0




        while reset_operecao_principal == 0:
        
            print("\nOpção Inválida !\n")
            print("\nDeseja realizar uma nova operação ?\n[01] Sim\n[02] Não")
            reset_operecao_principal = int(input(""))

            
            if reset_operecao_principal == 1:
                reset_programa = "pare" 
                operacao_principal = "inicie"
        
            elif reset_operecao_principal == 2:                
                print("\nObrigado Volte Sempre!")
                reset_programa = "pare"
                operacao_principal = "pare"

            else:
                reset_operecao_principal = 0
            

    
