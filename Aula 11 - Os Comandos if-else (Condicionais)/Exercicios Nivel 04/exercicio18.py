# EXERCICIO 18: NEGAÇÕES E LÓGICO COMPOSTA

# SOLICITE SE ELE TEM PRIVILÉGIO DE SUPERUSUÁRIO
script = input("Este script possui privilégio de superusuário (S/N): ").upper()

# SOLICITE SE ELE ESTÁ RODANDO EM CONTAINER
container = input("Ele está rodando em container isolado (S/N): ").upper()

# SE SCRIPT FOR IGUAL A "S" E HOUVER A NEGAÇÃO DE CONTAINER, CASO ELE SEJA VERDADEIRO,
# ELE VIRARÁ FALSO, ENTÃO:
if (script == "S") and not (container == "S"): # OPERADORES LOGICOS: AND E NOT
    print("EXECUÇÃO BLOQUEADA: Risco de comprometimento do Kernel do Host!") # CONDIÇÃO VERDADEIRA, VIRA FALSA
else: # SENÃO
    print("Execução permitida no ambiente seguro.") # CONDIÇÃO FALSA, VIRA VERDADEIRA