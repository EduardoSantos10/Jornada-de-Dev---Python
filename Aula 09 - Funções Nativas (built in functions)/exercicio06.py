# EXERCICIO 06:

# SOLICITEI 4 NUMEROS FLOAT AO USUÁRIO
V1 = float(input("Informe um valor: "))
V2 = float(input("Informe um valor: "))
V3 = float(input("Informe um valor: "))
V4 = float(input("Informe um valor: "))

# DECLAREI UMA LISTA COM ESTES NUMEROS ARMAZENADOS
lista = [V1, V2, V3, V4]

# REALIZEI A SOMATORIA DESTA LISTA COM A FUNÇÃO "SUM()"
soma = sum(lista)

# IMPRIMI O RESULTADO COM A PRONUNCIA, FORMATADA EM F-STRING
print(f"A soma dos elementos desta lista é: {soma:.2f}")