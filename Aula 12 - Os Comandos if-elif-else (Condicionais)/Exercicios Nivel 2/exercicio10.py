# EXERCICIO 10:

# SOLICITE O ESTADO DE PACOTE DO FIREWALL
estado = input("Informe o estado do pacote do firewall: ").upper()

# INICIO DA ESTRUTURA CONDICIONAL IF-ELIF-ELSE
if (estado == "ESTABLISHED" or estado == "RELATED"): # OPERADOR LOGICO "OR" UTILIZADO
    print("Regra Firewall: PERMITIR (Conexão existente ou derivada).")
    
elif (estado == "NEW"):
    print("Regra Firewall: ANALISAR (Submeter às regras da tabela INPUT).")
    
elif (estado == "INVALID"):
    print("Regra Firewall: DROP (Pacote malformado ou fora do estado).")
    
else:
    print("Regra Firewall: REJECT (Notificar remetente com TCP RST).")