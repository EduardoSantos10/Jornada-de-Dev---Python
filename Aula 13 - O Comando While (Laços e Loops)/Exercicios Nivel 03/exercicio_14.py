# EXERCICIO 14: GERADOR DE HASH DE PROTOCOLO DE ATENDIMENTO

# VARIAVEL DE INICIO, QUE ARMAZENARA O PROTOCOLO INICIANDO EM 1001
prot = 1001

# VARIAVEL DE CONTROLE DE DECISÃO DO OPERADOR
continuar = "S"

# ENQUANTO "CONTINUAR" FOR IGUAL A "S"
while continuar == "S":
    nome = input("Informe o seu nome: ") # SOLIICITE O NOME DO COLABORADOR
    print(f"O número do protocolo atual é o {prot}") # INFORME O PROTOCOLO ATUAL DELE
    
    prot += 1 # CONTADOR PARA O PROTOCOLO CONTINUAR INCREMENTANDO, CASO O ATENDIMENTO CONTINUE
    
    continuar = (input("Deseja seguir com o atendimento (S/N): ")).upper() # PERGUNTE SE ELE DESEJA SEGUIR COM O ATENDIMENTO
    
print("A sua rotina de atendimento foi finalizada com sucesso!") # MENSAGEM INFORMANDO QUE O ATENDIMENTO FOI ANALISADO COM SUCESSO!