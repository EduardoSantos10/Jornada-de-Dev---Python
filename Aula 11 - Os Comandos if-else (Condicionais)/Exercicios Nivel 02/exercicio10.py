# EXERCICIO 10:

# SOLICITE O CONSUMO DE BANDA
consumo = float(input("Informe o consumo de banda: "))

# INFORME A PRIORIDADE DO PACOTE
pacote = int(input("Informe a prioridade do pacote: "))

# SE O CONSUMO FOR MAIOR QUE 100.0 E (AND) PACOTE FOR MENOR QUE 3, ENTÃO:
if (consumo > 100.0 and pacote < 3): # OPERADOR LOGICO AND
    print("Aplicando Traffic Shaping (Limitação de Banda).") # CONDIÇÃO VERDADEIRA
else: # SE NÃO
    print("Banda liberada sem restrições de QoS.") # CONDIÇÃO FALSA