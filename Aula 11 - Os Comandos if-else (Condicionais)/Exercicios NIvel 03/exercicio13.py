# EXERCICIO 13:

# SOLICITE A PORCETAGEM DO ESPAÇO EM DISCO
porcetagem1 = float(input("Qual a porcentagem do espaço em disco: "))

# SOLICITE A PORCETAGEM DE INODES USADOS
porcetagem2 = float(input("Qual a porcentagem de Inodes usados: "))

# SE PORCENTAGEM DO ESPAÇO DE DISCO FOR MAIOR QUE 90.0 OU,
# PORCENTAGEM DE INODES FOR MAIOR QUE 90.0, ENTÃO:
if (porcetagem1 > 90.0 or porcetagem2 > 90.0): # OPERADOR LOGICO: OR
    print("ALERTA: Disco ou Inodes próximos do limite de exaustão!") # CONDIÇÃO VERDADEIRA
else: # SENÃO
    print("Armazenamento e Inodes em níveis saudáveis.") # CONDIÇÃO FALSA