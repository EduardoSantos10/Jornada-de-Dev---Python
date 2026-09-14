# EXERCICIO 17:

# VOCÊ SOLICITA A PORTA AO USUÁRIO
porta = int(input("Informe a porta que está sendo utlizada: "))

# VOCÊ SOLICITA O TIPO DE PROTOCOLO
protocolo = input("Informe o tipo de protocolo que está sendo utilizado: ").upper()

# AQUI VOCÊ FARÁ UMA VALIDAÇÃO DUPLA NA PRIMEIRA PARTE, VERIFICA-SE O PERTENCIMENTO DAS PORTAS
# SE "PORTA" É IGUAL A 80 OU PORTA É IGUAL A 443 E "PROTOCOLO" É IGUAL A TCP.
if (porta == 80 or porta == 443) and (protocolo == "TCP"):
    print("Tráfego web TCP autorizado pelo Firewall.")