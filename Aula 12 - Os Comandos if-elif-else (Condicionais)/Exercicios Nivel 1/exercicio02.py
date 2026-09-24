# EXERCICIO 02:

# VOCÊ SOLICITA AO COLABORADOR A LATÊNCIA
latencia = int(input("Informe a latência: "))

# AQUI IRÁ AVALIAR SE ELA É MENOR OU IGUAL A 20
if (latencia <= 20):
    print("Conexão Ultra-Rápida (Datacenter / Lan Local).")
    
elif (latencia <= 80): # AQUI IRÁ AVALIAR SE ELA É MENOR OU IGUAL A 80
    print("Latência Aceitável (SLA Normal).")
    
elif (latencia <= 200): # AQUI IRÁ AVALIAR SE ELA É MENOR OU IGUAL A 200
    print("Latência Alta (Alerta de Degradação de Rota).")
    
else:# CASO NÃO SEJA NENHUM DOS VALORES ACIMA
    print("TIMEOUT: Latência Crítica / Perda de Pacotes Elevada.")