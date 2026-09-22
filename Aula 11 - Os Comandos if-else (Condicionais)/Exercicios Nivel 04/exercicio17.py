# EXERCICIO 17: NEGAÇÕES E LÓGICA COMPOSTA

# SOLICITE O PROTOCOLO DE REDE
protocolo = input("Informe o protocolo: ").upper()

# SOLICITE A PORTA DE REDE
porta = int(input("Informe a porta de rede: "))

# SE PROTOCOLO FOR IGUAL A "TCP" E PORTA FOR IGUAL A "80" OU "443"
if (protocolo == "TCP") and (porta == 80 or porta == 443): # OPERADOR LOGICO "OR" E "AND"
    print("Pacote Web TCP permitido!") # CONDIÇÃO VERDADEIRA
else: # SENÃO
    print("Pacote rejeitado pela regra de filtragem L4.") # CONDIÇÃO FALSA