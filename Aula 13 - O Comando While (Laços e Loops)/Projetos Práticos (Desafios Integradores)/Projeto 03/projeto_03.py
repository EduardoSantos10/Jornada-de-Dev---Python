# PROJETO 03:

# BLOCO 01:

# VOCÊ SOLICITA A CAPACIDADE DE DISCO EM GB
disc_backup = int(input("Informe a capacidade do disco em GB: "))


# BLOCO 02:

# INICIALIZA DUAS CONSTANTES EM 0
espaco_usado = 0
qtd_arquivos = 0


# BLOCO 03:

# ENQUANTO FOR VERDADEIRO
while True:
    # INFORME A QUANTIDADE DO PRÓXIMO ARQUIVO A SER GRAVADO
    arq_backup = int(input("Informe o tamanho do próximo arquivo a ser gravado em GB: "))
    
    # FAÇA A SOMA DO ESPAÇO USADO COM PRÓXIMO ARQUIVO QUE FOI GRAVADO
    backup = espaco_usado + arq_backup
    
    # SE A SOMA TOTAL DO ESPAÇO USADO E O SEGUNDO VALOR INFORMADO FOI MAIOR QUE A MEMÓRIO TOTAL
    if backup > disc_backup:
        print("Espaço insufuciente na mídia!") # IMPRIME A MENSAGEM DE ESPAÇO INSUFUCUENTE
    
        break # AO ESTOURAR, O LAÇO IRÁ PARAR

    else:
        # SE NÃO, ENQUANTO NÃO ESTOURAR, ACUMULE O CONTADOR DE ESPAÇO USADO E A QUANTIDADE DE ARQUIVOS QUE PASSOU SEM ESTOURAR
        espaco_usado += arq_backup
        qtd_arquivos += 1
        
    
    
# BLOCO 04:
# FAÇA O CALCULO DO ESPAÇO USADO DIVIDIDO PELO DISCO TOTAL MULTIPLICADO POR 100, E ACUMULE EM MEMORIA TOTAL
memoria_total = espaco_usado / disc_backup * 100

# IMPRIMA O PERCENTUAL TOTAL DA MEMÓRIA
print(f"O percentual de ocupação final foi de {memoria_total}")

# IMPRIMA A QUANTIDADE DE ARQUIVOS QUE PASSOU SEM ESTOURAR
print(f"A quantidade de arquivos salvos foi de {qtd_arquivos}")