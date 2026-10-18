# EXERCICIO 04: MENU INTERATIVO DE SUPORTE TÉCNICO (CLI)

# CRIAÇÃO DO MENU DE OPÇÕES
print("Menu de Opções para Chamado")
print("1 - Reset de Senha")
print("2 - Consultar chamado")
print("3 - Encerramento do Chamado")
print("0 - Sair do Sistema")

# CRIAÇÃO DO CONTADOR
cont = 1

# CASO O WHILE SEJA TRUE, ELE CONTINUARA EXECUTANDO
while True:
    opcao = int(input("Informe uma opção: ")) # CAPTANDO A OPÇÃO
    
    if opcao == 0: # SE A OPÇÃO FOR IGUAL A "0"
            print("Saindo do Sistema de Chamados")
            break # BREAK PARA SAIR DO SISTEMA
    
    elif opcao == 1: # CASO A OPÇÃO SEJA 1
        print("Solicitação de Reset de Senha Gerada!")
        cont += 1 # UTILIZE O CONTADOR PARA CONTINUAR ITERANDO SOBRE O SISTEMA
        
    elif opcao == 2: # CASO A OPÇÃO SEJA 2
        print("Consulta de Chamado sendo processada...")
        cont += 1 # CONTADOR PARA CONTINUAR ITERANDO SOBRE O SISTEMA
    
    elif opcao == 3: # CASO A OPÇÃO SEJA 3
        print("Chamado será encerrado!")
        cont += 1 # CONTADOR CONTINUAR ITERANDO SOBRE O SISTEMA
        
    else: # CASO NÃO SEJA NENHUM DESSES 3, APARECE A MENSAGEM DE ERRO
        print("Dígito Errado... Escolha entre 0 e 3")