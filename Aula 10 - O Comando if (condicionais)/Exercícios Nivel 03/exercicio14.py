# EXERCICIO 14:

mem = float(input("Informe o consumo de memória: "))

req = int(input("Informe o número de requisições com erro: "))

if (mem > 90.0) or (req > 100):
    print("Comando emitido: Reiniciando contêiner do serviço.")