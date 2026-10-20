# PROJETO 01: MONITOR DE PACOTES PERDIDOS EM REDE (PING SWEEP)

# BLOCO 01:
# CAPTURA DE IP E QUANTIDADE TOTAL DE PACOTES
ip = input("Informe o IP do hostname: ")
pacotes_t = int(input("Informe a quantidade total de pacotes de teste: "))


# BLOCO 02:
# INICIALIZADORES: PACOTES ENVIADOS, RECEBIDOS E PERDIDOS
pct_env = 0
pct_receb = 0
pct_perd = 0


# BLOCO 03:
# PERCORRE A SEQUENCIA, ATÉ ATINGIR A QUANTIDADE ESTIPULADA NO BLOCO 01

# ENQUANTO "PCT_ENV" FOR MENOR QUE "PACOTES_T":
while pct_env < pacotes_t:
    pct_env += 1 # CONTADOR DE PACOTES ENVIADOS
    
    # "PACOTES_ATUAL" RECEBE O STATUS ATUAL DO PACOTE (0 OU 1)
    pacotes_atual = int(input("Informe o status do pacote atual: "))
    if pacotes_atual == 1: # SE PACOTES ATUAL FOR IGUAL A 1
        pct_receb +=1 #"PCT_RECEB" INCREMENTA 1
    else: # SE NÃO
        pct_perd +=1 #"PCT_PERD" INCREMENTA 1


# BLOCO 04:
# CALCULO DE PORCENTAGEM DE PERDA E CLISSIFICAÇÃO DO ESTADO OPERACIONAL DO LINK


# CALCULO DA PORCENTAGEM DE PERDA
# "TAXA_PERDA" RECEBE A DIVISÃO DE "PCT_PERD" E "PACOTES_T" MULTIPLICADO POR 100
taxa_perda = (pct_perd / pacotes_t) * 100

# IMPRMINDO O IP TESTADO
print(f"O IP testado foi: {ip}")

# IMPRIMINDO O TOTAL DE PACOTES ENVIADOS
print(f"O total de pacotes enviados foi: {pct_env}")

# IMPRIMINDO O TOTAL DE PACOTES RECEBIDOS
print(f"O total de pacotes recebidos foi: {pct_receb}")

# IMPRIMINDO O TOTAL DE PACOTES PERDIDOS
print(f"O total de pacotes perdidos foi: {pct_perd}")

# IMPRIMINDO A TAXA DE PERDA
print(f"A porcentagem calculada, é de: {taxa_perda}%")

# SE "TAXA_PERDA" FOR IGUAL A 0:
if taxa_perda == 0:
    print("EXCELENTE!")
elif taxa_perda <= 20: # SE "TAXA_PERDA" FOR MENOR IGUAL A 20
    print("INSTÁVEL!")
else: # SE NÃO
    print("INOPERANTE")