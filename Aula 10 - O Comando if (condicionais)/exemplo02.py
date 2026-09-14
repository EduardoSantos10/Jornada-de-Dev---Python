# EXEMPLO 02:

# SOLICITE UMA NOTA AO USUÁRIO
nota = float(input("Informe a sua nota: "))

# SE A NOTA FOR MENOR QUE 7.0, E SIMULTANEAMENTE MENOR OU IGUAL A 4.0
# ELE TEM DIREITO A EXAME
if (nota < 7.0) and (nota >= 4.0):
    print("Tem direito a exame!")
