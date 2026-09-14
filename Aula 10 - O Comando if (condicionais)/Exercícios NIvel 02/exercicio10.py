# EXERCICIO 10:

# INFORME O NÚMERO DE UMA PORTA
portas = int(input("Informe o número da porta: "))

# SE ESSA PORTA FOR MAIOR OU IGUAL A 49152 E MENOR OU IGUAL A 65535, ENTÃO, IMPRIMA
if(portas >= 49152) and (portas <= 65535):
    print("Porta pertencente ao intervalo de portas efêmeras/dinâmicas.")