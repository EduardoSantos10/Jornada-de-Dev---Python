# EXERCICIO 09:

# SOLICITE A HORA
time = int(input("Informe a hora atual: "))

# SOLICITE O STATUS DOS TESTES UNITARIOS
status = input("Os testes unitários podem prosseguir?(S/N): ")

# SE A HORA FOR MENOR QUE 18 E (AND) STATUS FOR IGUAL A "S", ENTÃO:
if (time < 18 and status == "S"): # OPERADOR LOGICO AND
    print("Iniciando pipeline de Deploy em produção.") # CONDIÇÃO VERDADEIRA
else:
    print("Deploy bloqueado: Fora da janela permitida ou testes com falha.") # CONDIÇÃO FALSA