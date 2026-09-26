# EXERCICIO 20:

# SOLICITE A LATENCIA DA REPLICAÇÃO:
lat = float(input("Informe a latência da replicação em segundos: "))

# SOLICITE A DISPONIBILIDADE SECUNDARIA:
sec = input("Informe a disponibilidade da rede secundária: ")

# INICIO DA ESTRUTURA IF-ELIF-ELSE
if (lat <= 1.0 and sec == "S"): # USO DO OPERADOR LOGICO "AND"
    print("Failover Automático Seguro: Promovendo réplica para nó Primário sem perda de dados.")

elif (lat <= 10.0 and sec == "S"):
    print("Failover Manual Requerido: Risco baixo de divergência de transações (Lag aceitável).")
    
elif (sec == "N"):
    print("Failover Abortado: Link com datacenter secundário indisponível!")
    
else:
    print("CRÍTICO: Replicação altamente dessincronizada (Lag elevado)! Intervenção de DBA necessária.")