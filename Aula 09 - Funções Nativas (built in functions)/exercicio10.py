# EXERCICIO 10:

# PEÇA UMA LETRA AO USUÁRIO
letra = input("Informe uma letra: ")

# ATRAVES DA FUNÇÃO "ORD()" CONVERTA A LETRA EM CODIGO ASCII
codigo = ord(letra)

# SOLICITE UM NUMERO AO USUARIO
numero = int(input("Informe um numero: "))

# ATRAVES DA FUNÇÃO "CHR()" CONVERTA A LETRA EM NUMERO INTEIRO
caractere = chr(numero)

# IMPRIMA A MENSAGEM COM O NUMERO DA TABELA ASCII
print("Esta letra correspondente na tabela ASCII: ", codigo)

# IMPRIMA A MENSAGEM COM O CARACTERE CORRESPONDENTE
print("Este codigo numerico representa o caractere: ", caractere)