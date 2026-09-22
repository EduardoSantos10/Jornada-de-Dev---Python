# EXERCICIO 12:

# SOLICITE SE O IP VEIO DE ACESSO DESCONHECIDO
acesso = input("O acesso veio de um IP desconhecido?(S/N): ").upper()

# SOLICITE SE O HORÁRIO FOI DE MADRUGADA
time = input("O horário foi de madrugada?(S/N): ").upper()

# SE ACESSO FOR IGUAL A "S" OU (OR) TIME FOR IGUAL A "S", ENTÃO:
if (acesso == "S" or time == "S"): # OPERADOR LOGICO OR
    print("Iniciando verificação de segurança reforçada (MFA obrigatório).") # CONDIÇÃO VERDADEIRA
else: # SENÃO
    print("Acesso padrão liberado sem desafios adicionais.") # CONDIÇÃO FALSA