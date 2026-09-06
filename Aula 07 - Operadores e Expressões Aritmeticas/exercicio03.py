# EXERCICIO 03:

# SOLICITE O PREÇO DE UM PRODUTO
preco = float(input("Informe o preço de um produto: "))

# CALCULO DO PRODUTO COM 10% DE DESCONTO
print(f"O valor do produto com 10% de desconto é {preco * 0.90: .2f}")

# FORMULA PARA CALCULAR O VALOR DO PRODUTO COM 8% DE AUMENTO POR PARCELAMENTO
aumento = preco * 0.08
precoFinal = preco + aumento

# IMPRIMINDO O RESULTADO
print(f"O valor deste produto com 8% de aumento por parcelamento é {precoFinal: .2f}")
