# EXERCICIO 03:

# PEÇA AO USUARIO A PRIMEIRA NOTA E CONVERTA PARA FLOAT COM CASTING
nota1 = float(input("Digite a primeira nota: "))

# PEÇA AO USUARIO A SEGUNDA NOTA E CONVERTA PARA FLOAT COM CASTING
nota2 = float(input("Digite a segunda nota: "))

# REALIZE O CALCULO DA MEDIA
media = (nota1 + nota2) / 2

# IMPRIMA ESTE RESULTADO COM A FORMATAÇÃO F-STRING
print(f"A média do aluno é: {media:.1f}")