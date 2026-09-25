# EXERCICIO 11:

# INFORME O NIVEL DE IMPACTO
imp = int(input("Informe o nivel de impacto (1 a 3): "))

# INFORME A URGÊNCIA
urg = int(input("Informe a urgência do chamado (1 a 3): "))

# REALIZE O CALCULO DE IMPACTO + URGENCIA E ATRIBUA O RESULTADO A SOMA
soma = imp + urg

# INICIO DA ESTRUTURA CONDICIONAL IF-ELIF-ELSE
if (soma == 2):
    print("Prioridade P1 (Crítica): SLA de resolução em 1 hora (War Room ativada).")
    
elif (soma == 3 or soma == 4): # USO DO OPERADOR LOGICO "OR"
    print("Prioridade P2 (Alta): SLA de resolução em 4 horas.")
    
elif (soma == 5):
    print("Prioridade P3 (Média): SLA de resolução em 24 horas.")
    
else:
    print("Prioridade P4 (Baixa): SLA de resolução em 72 horas.")