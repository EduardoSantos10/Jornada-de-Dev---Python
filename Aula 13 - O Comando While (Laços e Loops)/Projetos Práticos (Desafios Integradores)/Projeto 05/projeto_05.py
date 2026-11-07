# PROJETO 05: AUDITORIA DE LOG DE TENTATIVAS DE INVASÃO (SECOPS PARSER)

# BLOCO 01:

# SOLICITA O IP DO ATACANTE
ip_verif = input("Informe um IP: ")

# DEFINE O LIMITE DE TENTATIVAS
LIMITE_ATAQUES = 5


# BLOCO 02:
# INICIALIZA O CONTADOR DE ATAQUES
contador_ataque = 0

# INICIALIZA A CONDIÇÃO DO FIREWALL
bloqueado_firewall = False


# BLOCO 03:
# ENQUANTO FIREWALL NÃO ESTIVER BLOQUEADO
while not bloqueado_firewall:
    # SOLICITE UM NUMERO DE REQUISIÇÃO
    req = int(input("Informe uma requisição (1 para ataque ou 0 para legitimo): "))
    
    # SE REQ FOR IGUAL A 1:
    if req == 1:
        print("Requisição maliciosa") # IMPRIMA REQUISIÇÃO MALICIOSA
        status = "Bloqueado com sucesso" # INFORMA QUE ESTÁ BLOQUEADO
        contador_ataque += 1 # INCREMENTA O CONTADOR
        
    else: # SE NÃO
        print("Tráfego seguro") # IMPRIMA TRÁFEGO SEGURO
        status = "Ativo no parametro" # INFORMA QUE ESTÁ COM PARAMETRO ATIVO
        
    # CONDIÇÃO PARA VALIDAR O NUMERO DE ATAQUES
    # SE CONTADOR_ATAQUE FOR MAIOR OU IGUAL A LIMITE_ATAQUES
    if contador_ataque >= LIMITE_ATAQUES:
        print("CONEXÃO BARRADA") # IMPRIMA CONEXÃO BARRAD
        bloqueado_firewall = True # ALTERA O STATUS DO FIREWALL
        
    else: # SENÃO
        print("PACOTE ESTÁ ATIVO, CONEXÃO SEGUE EM OBSERVAÇÃO") # IMPRIMI QUE ELE ESTÁ SENDO MONITORADO
        

# BLOCO 04:

# IMPRIMI O IP DO ATACANTE
print(f"O IP do atacante era o {ip_verif}")

# IMPRIMI O NÚMERO DE ATAQUES REALIZADOS
print(f"O total de requisições maliciosas interceptada foi de {contador_ataque}")

# INFORMA O STATUS ATUAL
print(f"O status firewall é: {status}")