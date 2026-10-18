# EXERCICIO 10: LEITOR DE LOGS COM FILTRO DE ERROS (CONTINUE)

# VARIAVÉL ACUMULADORA
erros_crit = 0

# ENQUANTO FOR VERDADEIRO:
while True:
    nivel = input("Informe o nível da log atual: ").upper() # INFORME O NIVEL DA LOG ATUAL: INFO, ERROR OU WARNING
    
    if nivel == "SAIR": # SE FOR IGUAL A SAIR, ELE FINALIZA O SISTEMA
        print("Sistema de Leitura de Logs Encerrado!") # INFORMA A MENSAGEM
        break # PARA O LAÇO
    
    elif nivel == "INFO": # SE FOR IGUAL A INFO
        print("Evento Rotineiro Ignorado Pelo Filtro") # INFORMA A MENSAGEM
        continue # CONTINUA O LAÇO
    
    elif nivel == "ERROR": # SE FOR IGUAL A ERRO
        print("Erro! Falha Crítica!") # INFORMA A MENSAGEM
        erros_crit += 1 # ERROS_CRIT ACUMULA O TANTO DE ERROR INFORMADO COMO CONTADOR
        
    else: # SE NÃO
        print("Erro de Digitação ao Sistema!") # MENSAGEM INFORMADA
        
print(f"Foi monitorado um total de {erros_crit} logs críticas") # MENSAGEM FINAL COM O TANTO DE ERROS REGISTRADOS