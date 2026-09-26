# EXERCICIO 19:

# SOLICITE A PRESENÇA DO CABEÇALHO HSTS:
cab = input("Informe a presença do cabeçalho 'Strict-Transport-Security' (S/N): ").upper()

# SOLICITE A PRESENÇA DO CABEÇALHO CSP:
cab2 = input("Informe a presença do cabeçalho 'Content-Security-Policy' (S/N): ").upper()

# INICIO DA ESTRUTURA CONDICIONAL IF-ELSE-ELIF
if (cab == "S" and cab2 == "S"): # OPERADOR "AND"
    print("Nível de Segurança Web: EXCELENTE (Proteção HSTS e anti-XSS ativa).")
    
elif (cab == "S" and not cab2 == "S"): # OPERADOR "NOT"
    print("Nível de Segurança Web: MÉDIO (Proteção HTTPS forçada, mas vulnerável a XSS).")
    
elif (not cab == "S" and cab2 == "S"):
    print("Nível de Segurança Web: MÉDIO (Proteção anti-XSS ativa, mas sem HSTS forçado).")
    
else:
    print("ALERTA DE SEGURANÇA: Cabeçalhos defensivos ausentes! Vulnerável a MitM e XSS.")