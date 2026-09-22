# EXERCICIO 02:

# SOLICITE A QUANTIDADE DE MEMÓRIA RAM LIVRE
mem = int(input("Informe a quantidade de memória RAM livre: "))

# SE A QUANTIDADE DE MEMORIA FOR MENOR QUE 4, ENTÃO:
if (mem < 4):
    print("ALERTA: Memória RAM crítica! Risco de Out-Of-Memory (OOM Killer).") # CONDIÇÃO VERDADEIRA
else: # SE NÃO
    print("Memória RAM suficiente para os processos atuais.") # CONDIÇÃO FALSA