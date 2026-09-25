# EXERCICIO 13:

# SOLICITE O TEMPO DE RESPOSTA
temp = int(input("Informe o tempo de resposta (ms): "))

# SOLIICTE A PORCETAGEM DE ERROS
porc = float(input("Informe a porcentagem de erros: "))

# INICIO DA ESTRUTURA CONDICIONAL IF-ELIF-ELSE
if (temp < 100 and porc < 1.0):
    print("Nó 100% Saudável: Mantendo peso total no Pool (Weight 100).")
    
elif (temp < 500 and porc < 5.0): # USO DO OPERADOR "AND"
    print("Nó Degradado: Reduzindo peso no Pool (Weight 50).")
    
elif (porc >= 5.0):
    print("Nó Inoperante: Removendo do Pool (Deregister Target).")
    
else:
    print("Nó sob Alta Carga: Drenando conexões atuais (Draining Mode).")