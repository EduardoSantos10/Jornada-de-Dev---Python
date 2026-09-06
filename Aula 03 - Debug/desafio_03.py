# DESAFIO DE DEBUG 03

soma = 0

for i in range(1, 4):
    numero = int(input(f"Digite o {i}° numero: "))
    soma = numero # DICA: O QUE ACONTECE COM O ACUMULADOR 'soma' A CADA CICLO?

print(f"A soma total é: {soma}")