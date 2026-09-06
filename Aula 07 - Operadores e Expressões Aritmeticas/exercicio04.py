# EXERCICIO 04:

# SOLICITE UMA QUANTIDADE DE DIAS AO USUARIO
dias = int(input("Informe uma quantidade total de dias: "))

# CALCULE E IMPRIMA A QUANTIDADE DE SEMANAS COMPLETAS
print(f"Esse dia representa {dias // 7} semanas completas")

# CALCULE E IMPRIMA A QUANTIDADE DE DIAS FORA DA SEMANA
print(f"Restam {dias % 7} dias fora das semanas completas")