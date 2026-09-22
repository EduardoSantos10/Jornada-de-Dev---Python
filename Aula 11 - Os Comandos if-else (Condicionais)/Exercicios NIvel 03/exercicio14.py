# EXERCICIO 14:

# SOLICITE A VOLTAGEM DE REDE
volts = int(input("Informe a voltagem eletrica em Volts: "))

# SOLICITE A CARGA DA BATERIA
bateria = int(input("Informe a carga da bateria: "))

# SE VOLTS FOR MENOR QUE 100 OU BATERIA FOR MENOR QUE 20, ENTÃO:
if (volts < 100 or bateria < 20): # OPERADOR LOGICO OR
    print("Disparando gerador auxiliar ou iniciando shutdown gracioso.") # CONDIÇÃO VERDADEIRA
else: # SENÃO
    print("Alimentação elétrica estável.") # CONDIÇÃO FALSA