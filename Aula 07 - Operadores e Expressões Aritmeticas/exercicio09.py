# EXERCICIO 04:

# SOLICITE O TOTAL DE PEÇAS FÁBRICADAS
pecas_totais = int(input("Informe a quantidade total de peças fábricadas: "))

# INICIALIZE AS VÁRIAVEIS "CAIXAS" E "SOBRAS" COM "PECAS_TOTAIS"
caixas = pecas_totais
sobra = pecas_totais

# REALIZE A ATRIBUIÇÃO DA DIVISÃO INTEIRA
caixas //= 6

# REALIZE A ATRIBUIÇÃO DO RESTO DA DIVISÃO
sobra %= 6

# IMPRIMA QUANTAS CAIXAS SERÃO NECESSÁRIAS
print(f"Será necessárias {caixas} caixas cheias")

# QUANTAS PEÇAS IRÁ SOBRAR
print(f"Irá sobrar um total de {sobra} peças")