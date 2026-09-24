# EXERCICIO 05:

# SOLICITE A PONTUAÇÃO AO USUÁRIO
pont = float(input("Informe a pontuação da vulnerabilidade CVSS: "))

# ESTRUTURA CONDICIONAL IF-ELIF-ELSE
if (pont == 0.0):
    print("Severidade: Nenhuma (Informativo).")
    
elif (pont < 4.0):
    print("Severidade: Baixa (Low Risk).")
    
elif (pont < 7.0):
    print("Severidade: Média (Medium Risk).")
    
elif (pont < 9.0):
    print("Severidade: Alta (High Risk).")
    
else: # CASO NENHUMA DESSAS CONDIÇÕES SEJAM ATENDIDAS
    print("Severidade: CRÍTICA (Critical Risk - Patch Imediato Required).")