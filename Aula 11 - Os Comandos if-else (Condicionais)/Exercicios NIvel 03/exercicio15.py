# EXERCICIO 15:

# SOLICITE A QUANTIDADE DE DIAS DESDE QUANDO FOI ALTERADA A SENHA
dias = int(input("Quantos dias se passou desde a última alteração de senha: "))

# SOLIICITE SE A CONTA ESTA INATIVA OU ATIVA
status = input("A conta está inativa?(S/N): ").upper()

# SE DIAS FOR MAIOR QUE 90 OU (OR) STATUS FOR IGUAL A "S", ENTÃO:
if (dias > 90 or status == "S"): # OPERADOR LOGICO OR
    print("Conta bloqueada por políticas de conformidade e segurança.") # CONDIÇÃO VERDADEIRA
else: # SENÃO
    print("Conta ativa e regularizada.") # CONDIÇÃO FALSA