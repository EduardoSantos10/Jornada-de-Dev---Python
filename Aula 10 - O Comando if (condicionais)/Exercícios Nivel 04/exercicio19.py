# EXERCICIO 19:

# VOCê SOLICITA A FAIXA INICIAL DO IP AO USUÁRIO
seq = input("Informe a faixa inicial de IP: ")

# VOCÊ QUESTIONA SE O USUÁRIO ESTÁ AUTENTICADO
aut = input("O usuário está autenticado (S/N): ").upper()

# AGORA COMPARE, SE A SEQUENCIA DE IP NÃO FOR IGUAL A "10.0.0" E "AUT"
# NÃO FOR IGUAL A "S", IMPRIMA:
if not (seq == "10.0.0") and not (aut == "S"):
    print("Acesso bloqueado: Conexão externa não autenticada.")