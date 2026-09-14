# EXERCICIO 07:

# SOLICITE A HORA AO USUÁRIO
hora = int(input("Informe a hora atual: "))

# SOLICITE O CONSUMO DE CPU
consumo = float(input("Informe o consumo da CPU: "))

# SE A HORA FOR MAIOR OU IGUAL A ZERO E MENOR OU IGUAL A 5 E
# CONSUMO FOR MENOR QUE 30.0, ENTÃO, IMPRIMA:
if (hora >= 0 and hora <= 5) and (consumo < 30.0):
    print("Condições ideais: Iniciando rotina de backup.")