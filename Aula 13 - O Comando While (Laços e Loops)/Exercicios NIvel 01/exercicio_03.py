# EXERCICIO 03: CONTADOR DE RETENTATIVAS DE CONEXÃO (RETRY POLICY)

# VARIÁVEL DE INICIO
tentativa = 1

# ENQUANTO TENTATIVA FOR MENOR QUE 5:
while tentativa <= 5:
    print(f"Tentando conectar ao servidor... Tentativa: {tentativa}/5") # IMPRIMIR A MENSAGEM COM O NÚMERO DE TENTATIVAS EFETUADAS
    tentativa += 1 # CONTADOR