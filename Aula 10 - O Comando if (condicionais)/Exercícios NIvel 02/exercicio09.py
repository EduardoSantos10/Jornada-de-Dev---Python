# EXERCICIO 09:

# INFORME O RANGE DE IP
seq = input("Informe a sequência do IP: ")

# INFORME O TAMANHO DO PACOTE EM BYTES
pacote = int(input("Informe o tamanho do pacote: "))

# SE A SEQUENCIA DE IP FOR IGUAL AO PREFIXADO E O TAMANHO DO PACOTE FOR MAIOR QUE 1500
# ENTÃO, IMPRIMA:
if(seq == "192.168.1.100") and (pacote > 1500):
    print("ALERTA: Pacote fragmentado detectado da máquina confiável.")