# EXERCICIO 18:

# SOLICITE O STATUS DO POD:
status = input("Informe o status do pod: ")

# INICIO DA ESTRUTURA CONDICIONAL IF-ELIF-ELSE
if (status == "Running"):
    print("Estado Pod: Executando normalmente e pronto para receber requisições.")
    
elif (status == "Pending"):
    print("Estado Pod: Aguardando alocação de recursos pelo K8s Scheduler.")
    
elif (status == "CrashLoopBackOff"):
    print("Estado Pod: Falha contínua no processo! Verifique os logs do container.")
    
elif (status == "Terminating"):
    print("Estado Pod: Encerrando graciosamente conexões (SIGTERM).")
    
else:
    print("Estado do Pod desconhecido pelo cluster.")