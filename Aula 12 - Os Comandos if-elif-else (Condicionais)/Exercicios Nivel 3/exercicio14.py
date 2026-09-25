# EXERCICIO 14:

# SOLICITE A MÉDIA DA CPU:
med = float(input("Informe a média da CPU: "))

# INICIO DA ESTRUTURA CONDICIONAL IF-ELIF-ELSE
if (med < 20.0):
    print("Ação Auto Scaling: Scale-In (Reduzir 1 instância para economizar recursos).")
    
elif (med >= 20.0 and med <= 70.0): # USO DO OPERADOR LOGICO "AND"
    print("Ação Auto Scaling: Manter quantidade de instâncias estável.")
    
elif (med >= 70.1 and med <= 85.0):
    print("Ação Auto Scaling: Scale-Out Moderado (Adicionar 1 instância).")
    
else:
    print("Ação Auto Scaling: Scale-Out Crítico (Adicionar 3 instâncias imediatamente).")