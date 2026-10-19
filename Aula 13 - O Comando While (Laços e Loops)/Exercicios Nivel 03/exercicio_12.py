# EXERCICIO 12: MONITOR DE CARGA DE CPU COM MÉDIA MÓVEL

# INICIALIZAÇÃO DAS VARIÁVEIS

# CRIE UMA VARIAVÉL ACUMULADORA
soma_cpu = 0.0

# CRIE UMA VARIAVÉL CONTADORA
total_leituras = 0

# CRIE UMA VARIÁVEL PARA ARMAZENAR O VALOR
media_cpu = 0.0

# ENQUANTO "MEDIA_CPU" FOR MENOR OU IGUAL A 80.0
while media_cpu <= 85.0:
    leitura_atual = float(input("Qual o percentual de CPU consumido: ")) # LEITURA_ATUAL RECEBE O PERCENTUAL DA CPU CONSUMIDO
    total_leituras += 1 # CONTADOR PARA CONTINUAR LENDO ATÉ SER MAIOR OU IGUAL A 85.0
    
    # SOMAR O ACUMULADOR
    soma_cpu += leitura_atual
    
    # CALCULAR A MÉDIA, DIVIDINDO A SOMA DA CPU PELO TOTAL DE LEITURAS
    media_cpu = soma_cpu / total_leituras
    
    # IMPRIMA O ATUAL ESTADO DA CPU
    print(f"A média da CPU está em: {media_cpu:.2f}")
    
# IMPRIMA A MENSAGEM INFORMANDO O ATUAL ESTADO DA CPU
print(f"ALERTA: Saturação identificada! CPU atualmente em {media_cpu:.2f}")