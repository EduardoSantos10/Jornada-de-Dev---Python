# EXERCICIO 01:

# SOLICITE O USO DA CPU
porc = float(input("Informe o consumo da CPU: "))

# SE A PORCENTAGEM FOR MAIOR QUE 80.0, ENTÃO:
if (porc >= 80.0):
    print("ALERTA: CPU sobrecarregada! Disparando escalonamento") # CONDIÇÃO VERDADEIRA
else: # SE NÃO
    print("CPU em níveis operacionais normais") # CONDIÇÃO FALSA