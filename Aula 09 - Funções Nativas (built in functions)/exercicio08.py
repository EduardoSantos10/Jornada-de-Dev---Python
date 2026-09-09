# EXERCICIO 08:

# SOLICITE UM NUMERO INT AO USUÁRIO
numero = int(input("Informe um numero: "))

# SOLICITE UM NUMERO FLOAT
dado = float(input("Digite um determinado numero: "))

# SOLICITE UMA FRASE, O INPUT ORIGINALMENTE JÁ CONVERTE O TEXTO EM STRING
frase = input("Digite uma frase: ")

# IMPRIMA A FRASE, JUNTO DO TIPO QUE ELA CORRESPONDE, FORMATADO EM
# F-STRING
print(f"Essa variavel é do tipo: {type(numero)}")

print(f"Este numero é do tipo: {type(dado)}")
print(f"Essa frase é do tipo: {type(frase)}")