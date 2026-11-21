# EXERCICIO 07: ITERAÇÃO COM PASSO DINÂMICO (INÍCIO, FIM, PASSO)

# INFORME O INICIO DO LAÇO
inicio = int(input("Informe o número de início: "))

# INFORME O FIM DO LAÇO
fim = int(input("Informe o número do fim: "))

# INFORME O PASSO DO LAÇO
passo = int(input("Informe o número de passo: "))

# CRIE O LAÇO FOR
for i in range(inicio, fim, passo):
    print(f"O inicio, fim e passo deste laço, gerou a seguinte sequência: {i}")