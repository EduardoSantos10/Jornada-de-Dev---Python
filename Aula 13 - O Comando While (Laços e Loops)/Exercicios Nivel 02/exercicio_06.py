# EXERCICIO 06: SIMULADOR DE LOCKOUT POR TENTATIVAS EXCEDIDAS

# INICIALIZAÇÃO
tentativas = 0
senha_digitada = ""

# REGRAS DE NEGÓCIO
MAX_TENTATIVAS = 3
PIN = "2468"

# ENQUANTO "TENTATIVAS" FOR MENOR QUE "MAX_TENTATIVAS"
while tentativas < MAX_TENTATIVAS:
    senha_digitada = input("Digite o PIN de segurança: ") # SOLICITAÇÃO DE SENHA
    
    # SE "SENHA_DIGITADA" FOR IGUAL A "PIN"
    if senha_digitada == PIN:
        print("Acesso Liberado!") # MENSAGEM DE ACESSO LIBERADO
        break # BREAK
    
    else: # SE NÃO
        tentativas += 1 # INCREMENTA O CONTADOR CASO ELE ERRE
        restantes = MAX_TENTATIVAS - tentativas # "RESTANTES" RECEBE "MAX_TENTATIVAS" SUBTRAINDO "TENTATIVAS"
        
        # SE "RESTANTES" FOR MENOR 0:
        if restantes > 0:
            print(f"PIN Incorreto... Ainda Lhe Restam: {restantes}") # MENSAGEM: PIN INCORRETO, AINDA LHE RESTAM N TENTATIVAS
    
# SE "SENHA_DIGITADA" FOR IGUAL A "PIN"
if senha_digitada == PIN:
    print(f"Você conseguiu acessar o sistema com sucesso, com apenas {restantes}") # MENSAGEM DE SUCESSO
else: # SE NÃO
    print("Conta Bloqueada Por Excesso de Tentativas!") # MENSAGEM COM BLOQUEIO