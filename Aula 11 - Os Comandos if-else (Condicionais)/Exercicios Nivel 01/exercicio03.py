# EXERCICIO 03:

# INFORME O TEMPO DE LATÊNCIA
temp = int(input("Informe a latência de rede em milissegundos: "))

# SE O TEMPO FOR MENOR OU IGUAL A 50, ENTÃO:
if (temp <= 50):
    print("Conexão de excelente qualidade (SLA cumprido).") # CONDIÇÃO VERDADEIRA
else: # SE NÃO
    print("Alta latência detectada! Rota de rede degradada.") # CONDIÇÃO FALSA