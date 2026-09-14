# EXERCICIO 06:

# VALIDANDO ENTRADA BOOLEANA COM STRING
acesso = input("Informe o status do login (S/N): ")

# VALIDANDO ENTRADA COM TOKEN EM INT
token = int(input("Informe o seu token correspondente: "))

# SE "ACESSO" FOR IGUAL A "S" E (AND) "TOKEN" FOR IGUAL A "12345", ENTÃO, IMPRIMA:
if (acesso == "S") and (token == 12345):
    print("Acesso concedido ao painel administrativo.")
    
    
# OBS: VALIDANDO ENTRADA BOOLEANA COM NUMEROS:
"""
acesso = bool(int(input("Informe o status do login (1 para Ativo, 0 para Inativo): ")))
token = int(input("Informe o seu token correspondente: "))

if acesso and token == 12345:
    print("Acesso concedido ao painel administrativo.")
"""
