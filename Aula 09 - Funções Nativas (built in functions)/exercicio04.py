# EXERCICIO 04:

# SOLICITE O NUMERO DE BITS DE BARRAMENTO
bits = int(input("Informe a quantidade de bits do barramento: "))

# UTILIZE A FUNÇÃO POW(2, BITS) PARA REALIZAR ESTE CALCULO
mem = pow(2, bits)

# IMPRIMA A MENSAGEM COM O RESULTADO
print("Essa arquitetura consegue mapear ", mem, "endereços!")