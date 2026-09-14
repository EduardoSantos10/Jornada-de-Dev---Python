# EXERCÍCIO 13:

# SOLICITE UMA PORTA AO COLABORADOR
porta = int(input("Informe uma porta em uso: "))

# SE A PORTA INFORMADO FOR IGUAL A 21(FTP) OU IGUAL A 23(TELNET), ENTÃO, IMPRIMA:
if (porta == 21) or (porta == 23):
    print("ALERTA DE SEGURANÇA: Protocolo não criptografado em uso!")