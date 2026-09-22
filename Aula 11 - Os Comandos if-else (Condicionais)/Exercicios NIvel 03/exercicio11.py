# EXERCICIO 11:

# SOLICITE O STATUS DO NODE PRINCIPAL
node1 = input("Qual status do Node Principal(A/B): ").upper()

# SOLICITE O STATUS DO NODE SECUNDÁRIO
node2 = input("Qual status do Node Secundário(A/B): ").upper()

# SE O NODE 1 FOR IGUAL A "ATIVO" OU (OR) O NODE 2 FOR IGUAL A "ATIVO", ENTÃO:
if (node1 == "A" or node2 == "A"): # SE UMA CONDIÇÃO FOR VERDADEIRA, A EXPRESSÃO SE TORNA VERDADEIRA
    print("Cluster de Banco de Dados operacional.") # CONDIÇÃO VERDADEIRA
else:
    print("ALERTA CRÍTICO: Todos os nós do cluster estão indisponíveis! (Downtime)") # CONDIÇÃO FALSA