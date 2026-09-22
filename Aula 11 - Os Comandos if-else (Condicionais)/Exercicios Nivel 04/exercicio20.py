# EXERCICIO 20: NEGAÇÃO E LÓGICA COMPOSTA

# SOLIICITE O STATUS DO LOAD BALANCER
status = input("Informe o status do Load Balancer (S/N): ").upper()

# SOLICITE O STATUS DO BANCO DE DADOS
bd = input("Informe o status do banco de dados (S/N): ")

# INFORME QA QUANTIDADE DA CPU
quantidade = float(input("Informe o uso de CPU: "))

# NESSE CASO VAMOS AVALIAR 3 CONDIÇÕES
# SE STATUS FOR IGUAL A "S" E BD FOR IGUAL A "S" E QUANTIDADE FOR MENOR QUE 85.0, ENTÃO
if (status == "S" and bd == "S" and quantidade < 85.0): # OPERADOR LOGICO: AND 3X
    print("STATUS 200 OK: Infraestrutura saudável.") # CONDIÇÃO VERDADEIRA
else: # SENÃO
    print("STATUS 503 Service Unavailable: Falha em componente crítico.") # CONDIÇÃO FALSA