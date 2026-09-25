# EXERCICIO 08:

# SOLICITE O PROTOCOLO:
protocolo = input("Informe o nome do protocolo: ").upper()

# CONFIRME SE ESTA ORDEM É GARANTIDA OU NÃO:
garantia = input("Esta ordem é garantida (S/N): ").upper()

# INICIO DA ESTRUTURA CONDICIONAL IF-ELIF-ELSE
if (protocolo == "TCP" and garantia == "S"): # USO DO OPERADOR "AND"
    print("Protocolo Orientado à Conexão (Handshake 3-Way OK).")
    
elif (protocolo == "UDP" and garantia == "N"):
    print("Protocolo Não Orientado à Conexão (Foco em Baixa Latência / Streaming).")
    
elif (protocolo == "ICMP"):
    print("Protocolo de Controle e Diagnóstico de Rede (Ping / Traceroute).")
    
else:
    print("Combinação de protocolo e parâmetro de transporte inválida.")