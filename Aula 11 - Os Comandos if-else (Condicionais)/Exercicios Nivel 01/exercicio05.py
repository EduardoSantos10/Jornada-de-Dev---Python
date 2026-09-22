# EXERCICIO 05:

# SOLICITE O NUMERO DA PORTA SSH AO USUÁRIO
porta = int(input("Informe o número da porta SSH: "))

# SE O NUMERO DA PORTA FOR IGUAL A 22, ENTÃO:
if (porta == 22):
    print("Acesso direcionado para o serviço padrão SSH.") # CONDIÇÃO VERDADEIRA
else: # SE NÃO:
    print("Porta não padrão configurada para o serviço.") # CONDIÇÃO FALSA