# EXERCICIO 05: CALCULADORA DE MÉDIA DE LATÊNCIA DE PING

# SOLICITE OS TEMPOS DE LATÊNCIA
ms = float(input("Informe os tempos de latência: "))

# INICIANDO O CONTADOR EM 0
quantidade_pings = 0

# INICIANDO A SOMA DAS LATÊNCIAS EM 0
soma_latencias = 0

# ENQUANTO MS FOR DIFERENTE DE -1.0
while ms != -1.0:
    print(f"  [✓] Ping #{quantidade_pings} registrado: {ms:.1f} ms") # IMPRIMINDO A QUANTIDADE DE PINGS REGISTRADOS E AS LATÊNCIAS
    soma_latencias += ms # CAPTANDO A QUANTIDADE DE SOMA DAS LATÊNCIAS
    quantidade_pings += 1 # CONTADOR ITERANDO
    
    ms = float(input("Informe a próxima latência em ms (ou -1 para encerrar): ")) # CASO SEJA DIFERENTE DE -1


# Proteção contra divisão por zero
if quantidade_pings > 0:
    media_latencia = soma_latencias / quantidade_pings
    print(f"\nA média das latências foi de {media_latencia:.2f} ms")
    print(f"A quantidade total de pings registrados foi de {quantidade_pings} pings.")
else:
    print("\nNenhuma medição válida foi inserida.")
    
# IMPRIMINDO A MÉDIA DAS LATÊNCIAS    
print(f"A média das latências foi de {media_latencia}")

# IMPRIMINDO A QUANTIDADE DE PINGS
print(f"A quantidade total de pings regitrados foram de {quantidade_pings} pings")