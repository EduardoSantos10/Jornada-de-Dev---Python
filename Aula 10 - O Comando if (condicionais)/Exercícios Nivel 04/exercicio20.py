# EXERCICIO 20:

# SOLICITE SE O BANCO DE DADOS ESTÁ ATIVO
status_banco = input("O banco de dados está ativo (S/N): ").upper()

# SOLICITE SE A API ESTÁ ATIVA
status_api = input("A API está ativa (S/N): ").upper()

# INFORME O USO DE DISCO
disco = float(input("Informe o uso de disco: "))

# CONDIÇÃO: SE O BD FOR IGUAL A "S" E API FOR IGUAL A "S" E DISCO FOR MENOR QUE "80.0", ENTAO:
if (status_banco == "S") and (status_api == "S") and (disco < 80.0):
    print("Servidor 100% íntegro e pronto para receber a nova versão!")