# EXERCICIO 02: LEITOR DE TEMPERATURA DE DATACENTER

# SOLICITANDO A TEMPERATURA AO USUÁRIO
temp = float(input("Informe a temperatura do servidor: "))

# DEFININFO A CONSTANTE DE TEMPERATURA IDEAL
TEMPERATURA_IDEAL = 80.0

# DEFININDO O CONTADOR DE VALIDAÇÕES
validacoes = 1

# ENQUANTO A temp FOR MAIOR OU IGUAL A 80.0
while temp >= 80.0:
    print("ALERTA: Superaquecimento Detectado!") # MENSAGEM DE ALERTA SOBRE O SERVIDOR SUPERARQUECIDO
    validacoes += 1 # NUMERO DE VALIDAÇÕES
    
    temp = float(input("Informe a temperatura novamente: ")) # INFORMANDO A TEMPERATURA NOVAMENTE
    
print("Temperatura ideal para o servidor!") # MENSAGEM SOBRE A TEMPERATURA IDEAL
print(f"A temperatura está em: {temp} °C") # INFORMANDO A TEMPERATURA
print(f"Foram necessárias {validacoes} valdidações de temperatura") # INFORMANDO O NÚMERO NECESSÁRIO DE VALIDAÇÕES