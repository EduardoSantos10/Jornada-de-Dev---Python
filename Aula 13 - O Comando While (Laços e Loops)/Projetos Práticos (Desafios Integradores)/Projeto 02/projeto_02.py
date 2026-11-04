# PROJETO 02: SISTEMA DE COLETA DE MÉTRICAS MULTISERVIDOR (SRE DASHBOARD)

# BLOCO 01:

# INFORME A QUANTIDADE DE SERVIDORES QUE SERÃO AUDITADOS
servidores = int(input("Informe a quantidade total de servidores a serem auditados: "))

# BLOCO 02:

# CONTADOR DE SERVIDORES OPERANDO NORMALMENTE
serv_ok = 0

# CONTADOR DE SERVIDORES EM ALERTA
serv_alertas = 0

# CONTADOR DE SERVIDORES EM CRITICIDADE
serv_criticos = 0

# CONTADOR DE CONTROLE (VOLTAS DO LAÇO)
cont = 1


# BLOCO 03:

# ENQUANTO VARREDURA FOR MENOR OU IGUAL A SERVIDORES
while cont <= servidores:
    hostname = input("Informe o Hostname: ") # INFORME O HOSTNAME DESTE SERVIDOR
    cpu = int(input("Informe o consumo de CPU: ")) # INFORME O CONSUMO DE CPU
    cont +=1 # INCREMENTADOR DE VOLTAS
    
    if cpu < 70: # SE CPU FOR MENOR QUE 70
        print("OK") # IMPRIME OK
        serv_ok +=1 # INCREMENTA +1 NO CONTADOR DE SERVIDOR OK
    # SE NÃO SE, CPU FOR MAIOR OU IGUAL A 70, OU CPU FOR MENOR OU IGUAL 85:    
    elif cpu >= 70 and cpu <= 85:
        print("ALERTA!") # IMPRIME MENSAGEM DE ALERTA
        serv_alertas +=1 # INCREMENTA +1 NO CONTADOR DE SERVIDORES ALERTA
        
    else: # SE NÃO
        print("CRÍTICO!") # IMPRIME MENSAGEM DE CRÍTICO
        serv_criticos +=1 # INCREMENTA +1 NO CONTADOR DE SERVIDORES CRITICOS


# BLOCO 04:

# IMPRIMINDO ENUNCIADOS DE SERVIDORES OK, CRITICO OU EM ALERTA
print(f"No momento tem {serv_ok} servidores operando normalmente!")

print(f"No momento tem {serv_alertas} servidores em estado de alerta!")

print(f"Exatamente {serv_criticos} servidores estão em estado crítico. Necessário validação!")