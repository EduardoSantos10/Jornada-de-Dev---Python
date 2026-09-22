# EXERCICIO 08:

# SOLICITE A FAIXA DE IP
faixa = input("Informe a faixa de IP: ")

# INFORME A PORTA DE DESTINO
porta = int(input("Informe a porta de destino: "))

# SE FAIXA DE IP FOR IGUAL A "10.0.0.50" E (AND) A PORTA FOR IGUAL "3306", ENTÃO
if (faixa == "10.0.0.50" and porta == 3306): # OPERADOR LOGICO AND
    print("Tráfego de Banco de Dados autorizado pelo Firewall.") # CONDIÇÃO VERDADEIRA
else:
    print("Conexão bloqueada pela política padrão do Firewall.") # CONDIÃO FALSA